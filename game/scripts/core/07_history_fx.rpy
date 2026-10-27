## 07_history_fx.rpy - 历史记录页：过场时间、音效、滚动规则
##
## 规则（都是可调的，常量在最上面）：
##   · 唤出（↑ / 上滚轮）：书本摩擦声响起的同时开始淡入，淡入时长 == 音效时长
##   · 退出（右键 / 空格 / ESC）：瞬间切回游戏，不淡出 + 一声"咔"
##   · 已经滚到最下方时继续"往下"（↓ / 下滚轮 / PgDn）：同样直接回到游戏
##   · 页内每一次滚动（滚轮 / ↑↓ / PgUp·PgDn / 拖滚动条）：一声打字机拨片，
##     多个通道轮转播放，连着滚也不会互相打断/吞声；滚太快时按最小间隔限频，
##     多出来的请求直接丢掉，声音压成一个稳定节奏（不重叠、不发糊）
##
## 音效全部走 sfx 混音通道，受设置里的"音效音量"控制。

## 历史页用到的音效
## 原素材 audio/sfx/sfx_page_turn.ogg 解码后前 40ms 是完全静音、40-140ms 只有
## 满量程 1%-9% 的能量（峰值在 308ms），所以"按键到听见"那一百多毫秒是素材自带的。
## 用 test/tools/trim_sfx.py 剪掉前 100ms 并把起手抬 2.2 倍，另存为 *_trim.wav：
## 现在 0.9ms 就出声、20ms 达到可闻，全长 0.6247s（淡入时长跟着它走）。
define HIST_SFX_OPEN = "audio/sfx/sfx_page_turn_trim.wav"
define HIST_SFX_TICK = "audio/sfx/blip_default.ogg"        # 打字机拨片
define HIST_SFX_CLOSE = "audio/sfx/ui_history_close.wav"   # "咔"（tools/gen_ui_sfx.py 生成）

## 唤出淡入时长：None = 自动等于书本音效的实际长度（两者同时开始、同时结束）。
## 想强制指定就写成秒数，例如 0.45。
define HIST_ENTER_DISSOLVE = None

## 读不出音效长度时的兜底值（秒）
define HIST_ENTER_DISSOLVE_FALLBACK = 0.7

## 滚动音效的增益：1.0 = 原始音量，越大越明显（历史页期间背景音乐会被压到
## HIST_DUCK_VOLUME，所以两者叠加后这一声是很清楚的）
define HIST_TICK_VOLUME = 3

## 滚动音效轮转使用的通道（在 01_config.rpy 里注册）
define HIST_TICK_CHANNELS = ("ui_tick_0", "ui_tick_1", "ui_tick_2")

## 唤出（书本声）的增益：1.0 = 原始音量。翻页声本身偏响，压到 0.6 左右更不抢戏
define HIST_OPEN_VOLUME = 0.6

## 滚动音效的最小间隔（秒）：None = 自动取"音效长度 + 一点点"。
## 快速连滚时滚动请求来得比这密得多，多出来的请求会被直接丢掉（不排队），
## 于是声音被压成一个稳定的节奏：既不会一声没播完就被下一声顶掉（重叠/发糊），
## 也不会因为密集触发而破音、卡顿。
define HIST_TICK_MIN_GAP = None

## 读不出滚动音效长度时的兜底值（秒）
define HIST_TICK_SFX_FALLBACK = 0.052

init -1 python:

    import struct
    import time

    ## ---- 音效长度 ---------------------------------------------------------
    ## 淡入要跟音效等长，所以直接读文件头算时长。
    ## 支持 wav（RIFF，读 data 块大小）、ogg/Opus（granule 固定按 48kHz）、
    ## ogg/Vorbis（读头里的采样率）。

    _hist_open_len = []

    def audio_file_length(path):
        """返回音效文件时长（秒），读不出来返回 None。"""

        try:
            f = renpy.open_file(path)
            if f is None:
                return None
            data = f.read()
            f.close()
        except Exception:
            return None

        ## ---- wav ----
        if data[:4] == b"RIFF" and data[8:12] == b"WAVE":

            pos = 12
            rate = 0
            block = 0

            while pos + 8 <= len(data):

                cid = data[pos:pos + 4]
                size = struct.unpack("<I", data[pos + 4:pos + 8])[0]
                body = pos + 8

                if cid == b"fmt " and body + 14 <= len(data):
                    rate = struct.unpack("<I", data[body + 4:body + 8])[0]
                    block = struct.unpack("<H", data[body + 12:body + 14])[0]
                elif cid == b"data":
                    if rate > 0 and block > 0:
                        return size / float(rate * block)
                    return None

                pos = body + size + (size & 1)

            return None

        ## ---- ogg ----
        pos = data.rfind(b"OggS")
        if pos < 0 or pos + 14 > len(data):
            return None

        granule = struct.unpack("<q", data[pos + 6:pos + 14])[0]
        if granule <= 0:
            return None

        if data.find(b"OpusHead") >= 0:
            rate = 48000
        else:
            v = data.find(b"\x01vorbis")
            if v < 0 or v + 16 > len(data):
                return None
            rate = struct.unpack("<I", data[v + 12:v + 16])[0]
            if rate <= 0:
                return None

        return granule / float(rate)

    def hist_open_dissolve():
        """唤出淡入时长：优先用手动值，否则等于书本音效时长。"""

        if HIST_ENTER_DISSOLVE is not None:
            return HIST_ENTER_DISSOLVE

        if _hist_open_len:
            return _hist_open_len[0]

        length = audio_file_length(HIST_SFX_OPEN) or HIST_ENTER_DISSOLVE_FALLBACK
        _hist_open_len.append(length)
        return length

    def hist_enter_time_warp(complete):
        """
        淡入曲线（总时长不变，只改透明度上升的节奏）。

        默认的线性淡入，前 0.2 秒面板还只有两三成不透明，看上去像"声音先响、
        页面后出现"。这里把透明度往前压：音效刚起的头几十毫秒，页面就已经明显
        在浮现了，后面慢慢收尾到全不透明。
        """

        return 1.0 - pow(1.0 - complete, 5.0)

    ## ---- 音效 ------------------------------------------------------------

    ## 本次打开是否已经响过书本声（防止界面重建时重复播放）
    _hist_open_played = [False]

    ## 是不是走 OpenHistory 进来的（是的话声音交给转场的第一帧去播，
    ## 因为页面第一帧可能要排版好几百条历史，慢的时候要几百毫秒）
    _hist_enter_active = [False]

    ## 滚动音效通道轮转游标
    _hist_tick_cursor = [0]

    ## 上一次真正播响滚动音效的时刻（time.monotonic 秒），用于限频
    _hist_tick_last = [None]

    ## 缓存算出来的最小间隔
    _hist_tick_gap = []

    def hist_reset_open():
        """下一次显示历史页时要重新播放书本声。"""
        _hist_open_played[0] = False
        _hist_enter_active[0] = False
        hist_page_begin()

    def hist_play_open():
        """
        书本摩擦声，只响一次。

        调用点有三处，谁先到谁响：
          · OpenHistory（按 ↑ / 上滚轮 / 点"日志"的那一刻，最早）
          · HistEnterDissolve.render（第一帧画完，兜底）
          · hist_on_show（从设置/保存的侧栏进历史页时）
        """

        if _hist_open_played[0]:
            return False

        _hist_open_played[0] = True
        _hist_enter_active[0] = False
        renpy.sound.play(HIST_SFX_OPEN, channel="sound",
                         relative_volume=HIST_OPEN_VOLUME)
        return True

    def hist_on_show():
        """
        历史页被显示出来。

        从快捷菜单/设置里进历史页时没有专用转场，就在这里直接响；
        从 OpenHistory 进来时声音在按键那一刻已经响了，这里只是兜底。
        """

        if _hist_open_played[0]:
            return

        if _hist_enter_active[0]:
            hist_play_open()
            return

        ## 从菜单侧栏进来的：没有专用转场，也没人调 hist_reset_open()，
        ## 在这里把分页状态收回到"最新的几十条、停在底部"。
        hist_page_begin()

        hist_play_open()

    ## ---- 唤出转场 --------------------------------------------------------

    import renpy.display.transition as _hist_transition

    class HistEnterDissolve(_hist_transition.Dissolve):
        """
        历史页的淡入转场。

        声音现在在 OpenHistory 里、按键那一刻就播；这里保留一次兜底，
        免得哪条路径没经过 OpenHistory 时静音。
        """

        def render(self, width, height, st, at):

            rv = super(HistEnterDissolve, self).render(width, height, st, at)

            hist_play_open()

            return rv

    class HistEnterTransition(object):
        """
        config.enter_transition 用的转场工厂。

        引擎会以 `(old_widget=..., new_widget=...)` 调用它并期望拿回一个 displayable
        （和 `Dissolve(...)` 返回的东西是同一种），所以这里只是一个可调用的壳。
        """

        def __call__(self, old_widget, new_widget):
            return HistEnterDissolve(
                hist_open_dissolve(),
                old_widget=old_widget,
                new_widget=new_widget,
                time_warp=hist_enter_time_warp,
            )

    def hist_tick_gap():
        """滚动音效的最小间隔：比音效本身略长，保证一声播完才允许下一声。"""

        if HIST_TICK_MIN_GAP is not None:
            return HIST_TICK_MIN_GAP

        if _hist_tick_gap:
            return _hist_tick_gap[0]

        length = audio_file_length(HIST_SFX_TICK) or HIST_TICK_SFX_FALLBACK
        gap = max(length + 0.004, 0.052)
        _hist_tick_gap.append(gap)
        return gap

    def hist_play_tick():
        """滚一下的打字机声（限频 + 多通道轮转）。"""

        now = time.monotonic()
        last = _hist_tick_last[0]

        ## 滚太快：这一声直接跳过（不排队、不延后），保持"一拍一声"的稳定节奏
        if last is not None and now - last < hist_tick_gap():
            return False

        _hist_tick_last[0] = now

        i = _hist_tick_cursor[0]
        _hist_tick_cursor[0] = (i + 1) % len(HIST_TICK_CHANNELS)

        renpy.sound.play(
            HIST_SFX_TICK,
            channel=HIST_TICK_CHANNELS[i],
            relative_volume=HIST_TICK_VOLUME,
        )

        return True

    def hist_tick(value):
        """
        历史页滚动时的打字机声（由 viewport 的 yadjustment 回调触发）。

        滚到顶端还继续往上时，顺手把更早的历史追加进来（拖动滚动条也走这里）。
        """

        hist_play_tick()

        if value <= 0.5:
            hist_page_more()

    ## ---- 背景音乐闪避 ----------------------------------------------------
    ## 滚动音效是一声很短、很轻的打字机拨片，BGM 一起响就被盖住了。
    ## 所以历史页开着的时候把背景音乐往下压，退出历史页再恢复：
    ## 这里改的是通道音量（set_volume），不是混音器音量，所以玩家在设置里
    ## 调的音量比例保持不变，只是历史页期间额外乘一个系数。

    ## 历史页开着时要压下去的音轨（sfx 层的滚轴音效通道不在此列）
    HIST_DUCK_CHANNELS = ("music", "bgs", "psycho")

    ## 压到原来的多少（0.2 ≈ -14dB），想更狠就写 0.1
    HIST_DUCK_VOLUME = 0.2

    ## 压下去 / 恢复各用多少秒渐变，避免声音"啪"地跳一下
    HIST_DUCK_DELAY = 0.2
    HIST_UNDUCK_DELAY = 0.35

    ## 记录"现在是否处在压低状态"。历史页没开、也没压过的时候，回调什么都不做
    ## （引擎自己有一套"有人说话时压低音乐"的逻辑，别去和它打架）
    _hist_ducked = [False]

    ## 压下去之前的音量，退出历史页时还原成它（而不是硬写回 1.0）
    _hist_duck_saved = {}

    def _hist_channel_volume(channel):
        """读通道当前的（乘在混音器之上的）音量，读不到返回 None。"""

        try:
            return renpy.audio.audio.get_channel(channel).context.secondary_volume
        except Exception:
            return None

    def hist_duck_update():
        """
        每次交互开始时对齐一次：历史页 / 临时设置菜单开着就压背景，关着就恢复。

        用轮询而不是"进/出各调一次"，是因为历史页有好几个退出路径
        （右键/空格/ESC、贴底继续往下、从菜单侧栏点返回），
        只要页面消失，下一次交互就会自动把音量还回去。
        """

        shown = (renpy.get_screen("history") is not None
                 or renpy.get_screen("ui_game_menu") is not None)

        ## 页面没开、也不是我们压下去的：不碰音量
        if not shown and not _hist_ducked[0]:
            return

        for channel in HIST_DUCK_CHANNELS:

            current = _hist_channel_volume(channel)

            if shown:

                target = HIST_DUCK_VOLUME
                delay = HIST_DUCK_DELAY

                ## 已经压着了（同一个历史页会话里的后续交互）：不重复设置
                if current is not None and abs(current - target) < 0.002:
                    continue

                ## 只记第一次压之前的音量（之后 current 是我们自己压过的值）
                if channel not in _hist_duck_saved:
                    _hist_duck_saved[channel] = 1.0 if current is None else current

            else:

                target = _hist_duck_saved.pop(channel, 1.0)
                delay = HIST_UNDUCK_DELAY

                if current is not None and abs(current - target) < 0.002:
                    continue

            renpy.music.set_volume(target, delay, channel=channel)

        _hist_ducked[0] = shown

    if hist_duck_update not in config.interact_callbacks:
        config.interact_callbacks.append(hist_duck_update)

    ## ---- 增量渲染 --------------------------------------------------------

    ## 历史页一次只排这么多条（从最新的一句往前数）。首帧只排 HIST_LOAD_FIRST，
    ## 玩家往上翻到顶了再追加 HIST_LOAD_MORE 条。
    ## 为什么：viewport 里的 vbox 会把每条历史都建成 text 显示对象，条数越多
    ## 首帧排版越慢；而玩家进历史页总是先看最近的几句，所以没必要一上来就把
    ## 几百条全排出来（那会把唤出历史页的第一帧拖长）。
    HIST_LOAD_FIRST = 30
    HIST_LOAD_MORE = 30

    ## 当前渲染了多少条（从末尾往前数）
    _hist_loaded = [HIST_LOAD_FIRST]

    ## 刚追加了条目、但还没拿到新内容的像素高度：等 viewport 报出新 range 再补偿
    _hist_pending_comp = [False]
    _hist_range_before = [0.0]

    def hist_page_entries():
        """这一屏要渲染的历史条目：最新的 _hist_loaded 条。"""

        return _history_list[-_hist_loaded[0]:]

    def hist_page_begin():
        """新开一次历史页：回到"只排最新的几十条"并停在最底部。"""

        _hist_loaded[0] = HIST_LOAD_FIRST
        _hist_pending_comp[0] = False

        ## 先给一个远超内容高度的值，viewport 读 value 时会自己钳到 range 上，
        ## 于是第一帧就停在最底部（不依赖 yinitial，屏幕重建也不会被拉回顶部）。
        hist_yadj._value = 1e9

    def hist_page_more():
        """往上翻到头了：再放一段更早的历史进来。"""

        if _hist_pending_comp[0]:
            return False

        total = len(_history_list)

        if _hist_loaded[0] >= total:
            return False

        _hist_range_before[0] = hist_yadj.range
        _hist_pending_comp[0] = True
        _hist_loaded[0] = min(total, _hist_loaded[0] + HIST_LOAD_MORE)

        ## 重新走一遍屏幕，让 hist_page_entries() 的返回值生效
        renpy.restart_interaction()
        return True

    def hist_page_ranged(adj):
        """
        viewport 算出新的 range 时被调用（由 yadjustment 的 ranged 参数转发）。

        追加条目之后内容变高了 H 像素，滚动值也往上推 H 像素：原本贴着视口
        顶端的那一条仍然贴着顶端，所以加载更早的历史不会让画面跳一下。
        """

        if not _hist_pending_comp[0]:
            return

        _hist_pending_comp[0] = False

        added = max(adj.range - _hist_range_before[0], 0.0)
        adj.value = adj.value + added

    ## 全局唯一的滚动值对象。放在这里（而不是屏幕里的 default），是因为
    ## 加载更早的历史要重建屏幕，屏幕重建不该把滚动位置或滚动条重置掉。
    hist_yadj = renpy.display.behavior.Adjustment(
        1,
        0,
        changed=hist_tick,
        ranged=hist_page_ranged,
    )

    ## ---- 动作 ------------------------------------------------------------

    class OpenHistory(Action):
        """
        唤出历史记录页。

        页面本身由屏幕里的 ATL 从右侧滑出（见 10_ui_menu.rpy 的 ui_right_slide），
        这里只负责：按键那一刻就响书本声 + 把进出菜单的全局转场关掉，
        免得淡入淡出跟滑动动画叠在一起。
        """

        def __init__(self, screen="history"):
            self.screen = screen

        def __call__(self):

            hist_reset_open()
            _hist_enter_active[0] = True

            ## 按键/点击的瞬间就响，不等转场、不等第一帧画完
            hist_play_open()

            old_enter = config.enter_transition
            old_exit = config.exit_transition

            config.enter_transition = None
            config.exit_transition = None

            try:
                renpy.run(ShowMenu(self.screen))
            finally:
                config.enter_transition = old_enter
                config.exit_transition = old_exit

    class CloseHistory(Action):
        """关闭历史记录页：先一声"咔"，再瞬间回到游戏。"""

        def __call__(self):
            renpy.sound.play(HIST_SFX_CLOSE, channel="sound")
            hist_reset_open()

            ## Return() 在菜单里是靠返回 True 结束交互的，必须把返回值往上抛，
            ## 否则外面包一层 action 就会"只响音效、不退出"。
            return renpy.run(Return())

    class HistoryScroll(Action):
        """
        历史页滚动。

        `yadj`  当前历史页 viewport 的 yadjustment
        `delta` 负数向上、正数向下
        `page`  True 时按整页滚动（PgUp / PgDn），否则按一格 step

        贴到最下方（value == range）之后继续"向下"，就直接回到游戏；
        如果给了 on_close（临时菜单里的历史栏），就只收起那一栏。
        """

        def __init__(self, yadj=None, delta=-1, page=False, on_close=None):
            self.yadj = yadj
            self.delta = delta
            self.page = page
            self.on_close = on_close

        def __call__(self):

            yadj = self.yadj

            if yadj is None:
                return

            ## 已经在最下方还继续往下 → 退出（右键/空格不受此限制，随时可退）
            if self.delta > 0 and yadj.value >= yadj.range - 0.5:
                ## 同样要把返回值往上抛，菜单才会真的关掉
                if self.on_close is not None:
                    return renpy.run(self.on_close)
                return renpy.run(CloseHistory())

            ## 已经在最上方还继续往上 → 把更早的历史追加进来（真加载了才响一声）
            if self.delta < 0 and yadj.value <= 0.5 and hist_page_more():
                hist_play_tick()
                return

            ## 先响再滚：声音在事件进来的这一刻就排进音频队列，
            ## 不等 adjustment 的 changed 回调（那次调用会被限频挡掉，不会响两下）
            hist_play_tick()

            amount = yadj.page if self.page else yadj.step
            yadj.change(yadj.value + self.delta * amount)

