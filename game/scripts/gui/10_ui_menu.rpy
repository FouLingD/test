## 10_ui_menu.rpy —— 主界面 / 游戏内临时菜单 / 确认弹窗
##
## 结构：画面左边一块灰色面板（游戏内多一个标题白框 + 竖排选项），右边一块白色内容区。
## 左键选选项时不换屏、不盖遮罩，只切右侧内容；被选中的选项保持"选中"外观。
##
## 三态（全部由样式给出，改颜色即可整体换肤）：
##   常态     = 灰底白字
##   悬停     = 常态加亮，字变黑
##   选中/点击 = 常态加深，字保持黑
##
## 声音：悬停一声轻"嗒"，点击一声"嗒"。Ren'Py 的按钮只有 activate_sound（点击），
## 没有 hover_sound，所以悬停音用 hovered 回调自己播。

init offset = 5

## ---- 配色 ----

define UI_LEFT_BG = "#d2d2d2"
define UI_RIGHT_BG = "#fdfdfd"
define UI_INK = "#141414"
define UI_LINE = "#141414"
define UI_SLOT_HOVER = "#cfcfcf"

## 左侧选项
define UI_NAV_IDLE_BG = "#8c8c8c"
define UI_NAV_HOVER_BG = "#efefef"
define UI_NAV_SELECTED_BG = "#737373"

define UI_NAV_IDLE_TEXT = "#ffffff"
define UI_NAV_HOVER_TEXT = "#0d0d0d"
define UI_NAV_SELECTED_TEXT = "#0d0d0d"

## 右侧分类标签
define UI_TAB_IDLE_BG = "#dcdcdc"
define UI_TAB_HOVER_BG = "#bdbdbd"
define UI_TAB_SELECTED_BG = "#141414"
define UI_TAB_IDLE_TEXT = "#141414"
define UI_TAB_SELECTED_TEXT = "#ffffff"

## ---- 音效 ----

define UI_SFX_HOVER = "audio/sfx/ui_hover.wav"
define UI_SFX_CLICK = "audio/sfx/ui_click.wav"
define UI_SFX_VOLUME = 1.0

## 界面唤出音效（一声像敲木鱼的"咚"，比按钮点击音更清脆、尾音更长）
define UI_SFX_MENU_IN = "audio/sfx/ui_menu_knock.wav"
define UI_SFX_MENU_IN_VOLUME = 0.85

## 界面退出音效（一声"刷"，音高由高到低）
define UI_SFX_MENU_OUT = "audio/sfx/ui_menu_out.wav"
define UI_SFX_MENU_VOLUME = 0.9

## 动画时长：遮罩淡入要和左侧面板"弹到最右、还没回弹"的那一刻同时结束。
## 面板用的是 easein_back（1 - easeout_back(1-t)，s=1.7015），过冲顶点在
## t = 1 - 2s/(3(s+1)) ≈ 0.580，所以 0.580 × UI_LEFT_POP_TIME ≈ 0.198s。
define UI_OVERLAY_TIME = 0.198
define UI_OVERLAY_OUT_TIME = 0.26
define UI_LEFT_POP_TIME = 0.34
define UI_RIGHT_SLIDE_TIME = 0.52

## 退出动画：一级更快地弹走；二级像纸页一样滑走
define UI_LEFT_OUT_TIME = 0.24
define UI_RIGHT_OUT_TIME = 0.38

## 对话框淡入/淡出时长（菜单进出、历史页进出时由我们用 ATL 接管，
## 不再依赖引擎的 window_show/hide_transition —— 那套只在窗口真的被隐藏时才触发）
define UI_SAY_IN_TIME = 0.26
define UI_SAY_OUT_TIME = 0.34

## 主标题入场（启动页用）：从下往上微微抬起 + 淡入
define UI_TITLE_IN_TIME = 0.85
define UI_TITLE_IN_DELAY = 0.16

## 文字输出速度的四档（字符/秒）；0 表示瞬间
define UI_CPS_LOW = 18
define UI_CPS_MID = 35
define UI_CPS_HIGH = 60

init python:

    ## 把当前 cps 归到最近的一档（存档里可能是滑块留下的任意值，比如 61.39）
    def ui_cps_tier(cps):
        if cps is None or cps <= 0:
            return 0
        return min((UI_CPS_LOW, UI_CPS_MID, UI_CPS_HIGH),
                   key=lambda v: abs(v - cps))

## 从"历史文本"交接去历史页时，对话框"线性亮 → 紧接着线性暗"的一次三角波：
## 先用 UI_HANDOFF_IN_TIME 匀速亮到 UI_HANDOFF_PEAK，再用 UI_HANDOFF_OUT_TIME 匀速暗到 0。
## 两段共用一条时间线，中间没有任何停顿；总耗时 = 两者之和。
define UI_HANDOFF_PEAK = 0.45
define UI_HANDOFF_IN_TIME = 0.10
define UI_HANDOFF_OUT_TIME = 0.14

## ---- 右侧内容尺寸 ----

define UI_PAD = 70          # 内容区左内边距
define UI_RULE_Y = 112      # 标题下横线位置
define UI_BODY_Y = 150      # 内容起始 y

## 设置页每一行（标签 / 滑条 / 读数）的列位置，用绝对坐标保证各行对齐
define UI_ROW_LABEL_W = 220
define UI_ROW_BAR_X = 244
define UI_ROW_VALUE_X = 1108
define UI_ROW_VALUE_W = 120

## 音量四行：滑条起点按最长标签（"背景音乐"等四字，约 92px）再留 50px；
## 右侧百分比紧跟在滑条末端后面 24px（与"自动前进等待时间"那行的读数间距一致）
define UI_VOL_BAR_X = 142
define UI_VOL_VALUE_X = 1006

define UI_CARD_W = 432      # 存档卡片尺寸
define UI_CARD_H = 396
define UI_SHOT_W = 406      # 卡片里的截图区
define UI_SHOT_H = 228

## 非激活状态（窗口切走）时降低 CPU：每帧在回调里等这么久，把帧率压到 ~15fps
define UI_LOW_CPU_WAIT = 60

## 默认：非激活时暂停音频（引擎默认行为），但不额外降 CPU
default persistent.ui_low_cpu_unfocused = False

## 菜单的屏幕级状态（当前右侧内容 / 系统设置分类 / 退场状态 / 待办动作）。
## 用 define 而不是 default，免得被 rollback 卷回去；每次菜单显示时由 ui_reset_state() 重置。
define ui_store = {"page": None, "ptab": "display", "closing": None, "pending": None}

## 当前鼠标停在"删除档案"上的槽位（同一时刻只可能有一个）
default _ui_card_hot_slot = None

init python:

    import time as _ui_time

    ## 音量滑条：0.01 ~ 1.00 的线性百分比。
    ## 不能用 Ren'Py 自带的 Preference("music volume")：它背后是 MixerValue，
    ## 滑条坐标走的是分贝映射（get_mixer/set_mixer），拖起来和"100%"读数对不上，
    ## 手感很怪。这里直接读写 _preferences 里的线性音量。
    class UIVolumeValue(BarValue):

        def __init__(self, mixer):
            self.mixer = mixer

        def _clamp(self, value):
            if value < 0.01:
                return 0.01
            if value > 1.0:
                return 1.0
            return value

        def get_adjustment(self):
            return renpy.display.behavior.Adjustment(
                range=1.0,
                value=self._clamp(_preferences.get_volume(self.mixer)),
                step=0.01,
                force_step=True,
                changed=self.set_mixer,
                )

        def set_mixer(self, value):
            _preferences.set_volume(self.mixer, self._clamp(value))
            renpy.restart_interaction()

        def get_style(self):
            return "slider", "vslider"

    ## 悬停音限频：鼠标快速划过一串按钮时不至于连成一片
    _ui_hover_last = [0.0]

    def ui_hover_sound():
        now = _ui_time.monotonic()
        if now - _ui_hover_last[0] < 0.045:
            return
        _ui_hover_last[0] = now
        renpy.sound.play(UI_SFX_HOVER, channel="sound",
                         relative_volume=UI_SFX_VOLUME)

    ## 游戏内"返回标题 / 退出游戏"先弹确认窗
    def ui_confirm(message, yes_action):
        renpy.show_screen("ui_confirm_dialog",
                          message=message,
                          yes_action=yes_action)
        renpy.restart_interaction()

    ## 界面唤醒音效：一声敲木鱼似的"咚"（ESC、快捷菜单的 保存/系统 都用它）
    def ui_menu_in_sound():
        renpy.sound.play(UI_SFX_MENU_IN, channel="sound",
                         relative_volume=UI_SFX_MENU_IN_VOLUME)

    def ui_menu_out_sound():
        renpy.sound.play(UI_SFX_MENU_OUT, channel="sound",
                         relative_volume=UI_SFX_MENU_VOLUME)

    ## 用快捷菜单（下方 保存/设置 按钮）打开时，点击音已经响了，就不再叠唤醒音。
    ## 按 ESC 打开则只响唤醒音。
    _ui_skip_in_sound = [False]

    def ui_suppress_in_sound():
        _ui_skip_in_sound[0] = True

    def ui_menu_shown():
        if _ui_skip_in_sound[0]:
            _ui_skip_in_sound[0] = False
            return
        ui_menu_in_sound()

    def ui_reset_state(page=None, ptab="display"):
        ui_store["page"] = page
        ui_store["ptab"] = ptab
        ui_store["closing"] = None
        ui_store["pending"] = None

    ## 打开某一页（二级界面）：只有按钮自己的点击音，这里不再叠别的音效
    def ui_open_page(state, page):
        if state.get("closing"):
            return
        state["page"] = page
        renpy.restart_interaction()

    ## ---- 打开菜单（顺便拍一张干净的存档缩略图）----
    ## 引擎在进菜单那一刻截图，那时对话框还在画面上，存出来的缩略图会带个文字框。
    ## 注意：这里绝对不能 hide / show 那个对话框屏——那会重建 Text，把"打字打到一半"
    ## 的状态丢掉，于是退出菜单后整句会一次性冒出来、再点一下又跳回断点。
    ## 所以只把对话框的**透明度压到 0**（屏还在、Text 还是同一个），重绘一帧后再截图。
    _ui_shot_job = [None]

    ## ---- 游戏内的对话框屏 ----
    ## 除了标准的 say，还有三个特殊演出用的变体（都是整屏背景），
    ## 菜单截图、历史页都要把它们整体收起来，不然会盖在 UI 上面。
    UI_SAY_SCREENS = ("say", "inner1_say", "inner2_say", "duet_say")

    def ui_find_say():
        for name in UI_SAY_SCREENS:
            sc = renpy.get_screen(name)
            if sc is not None:
                return (name, sc.scope.get("who"), sc.scope.get("what"))
        return None

    def ui_open_menu(start_page=None, start_ptab="display"):

        ## 菜单已经开着：这一下当成"返回"（收二级，或整个退出）
        if renpy.context()._menu:
            if renpy.get_screen("ui_game_menu") is not None:
                ui_close(ui_store, "page" if ui_store["page"] else "menu")
            return

        job = ui_find_say()

        ## 打字机拨片是循环播的，进了菜单要先掐掉，否则会一直响
        ui_blip_stop()

        ## 没有对话在显示（选项、演出中按 ESC 等）：没什么可藏的，直接开菜单
        if job is None or job[2] is None:
            renpy.run(ShowMenu("ui_game_menu", start_page=start_page, start_ptab=start_ptab))
            return

        _ui_shot_job[0] = (start_page, start_ptab)

        ## 对话框压到全透明（不重建屏幕），快捷菜单也收掉，好让缩略图干净
        ui_say_hide_now()
        if renpy.get_screen("quick_menu") is not None:
            renpy.hide_screen("quick_menu")

        renpy.show_screen("ui_shot_watch")
        renpy.restart_interaction()

    def ui_shot_take():

        job = _ui_shot_job[0]

        if job is None:
            renpy.hide_screen("ui_shot_watch")
            return

        _ui_shot_job[0] = None
        start_page, start_ptab = job

        try:
            renpy.take_screenshot((config.thumbnail_width, config.thumbnail_height), keep_existing=False)
        except Exception:
            pass

        renpy.hide_screen("ui_shot_watch")

        if renpy.get_screen("quick_menu") is None:
            renpy.show_screen("quick_menu")

        renpy.run(ShowMenu("ui_game_menu", start_page=start_page, start_ptab=start_ptab))

    ## 退出：mode="page" 只收二级（回到一级），mode="menu" 整个菜单退出去。
    ## 所有退出路径都走这里，动画和音效只有一个来源。
    def ui_close(state, mode="menu"):
        if state.get("closing"):
            return
        state["closing"] = mode
        ui_menu_out_sound()
        renpy.restart_interaction()

    def ui_close_page(state):
        ui_close(state, "page")

    ## 历史文本：先像普通返回一样退出菜单（动画 + 退出音），
    ## 菜单收完之后让对话框按"原来的淡入速度"亮到 UI_HANDOFF_PEAK，
    ## 再按"原来的淡出速度"暗下去，最后才展开历史页。
    _ui_hist_pending = [False]
    _ui_hist_stage = [0]
    _ui_hist_when = [0.0]

    def ui_history_request(state):
        if state.get("closing"):
            return
        _ui_hist_pending[0] = True
        _ui_hist_stage[0] = 0
        ui_close(state, "menu")

    def ui_hist_show():

        if not _ui_hist_pending[0]:
            return

        ## 还在菜单里就别动，等菜单真的收完（回到游戏里、对话框露出来）再说
        if renpy.context()._menu or renpy.get_screen("ui_game_menu") is not None:
            return

        now = _ui_time.monotonic()
        stage = _ui_hist_stage[0]

        ## 亮起来的那一段 / 暗下去的那一段，两段首尾相接、中间不停顿
        peak = UI_HANDOFF_PEAK
        t_in = UI_HANDOFF_IN_TIME
        t_out = UI_HANDOFF_OUT_TIME

        ## 1) 一条三角波：匀速亮到 peak 再匀速暗到 0（中间不停）
        if stage == 0:
            ui_say_handoff_begin(t_in, t_out, peak)
            _ui_hist_stage[0] = 1
            _ui_hist_when[0] = now + t_in + t_out
            return

        if now < _ui_hist_when[0]:
            return

        ## 2) 三角波走完（对话框已经完全暗下去）才展开历史页
        _ui_hist_stage[0] = 0
        _ui_hist_pending[0] = False

        if renpy.get_screen("history") is not None:
            return

        ## 必须走 ShowMenu（= 新的菜单上下文），否则历史页里的"右键/空格/ESC 返回"
        ## 拿到的 Return() 结束不了这层交互，页面会赖在对话框上面关不掉。
        ## OpenHistory 里已经包含：重置标记 + 书本声 + 关掉进出菜单的全局转场。
        renpy.run(OpenHistory())

    if "ui_hist_watch" not in config.overlay_screens:
        config.overlay_screens.append("ui_hist_watch")

    ## 退场动画结束后的收尾
    def ui_finish_close(state):

        mode = state.get("closing")
        state["closing"] = None
        state["pending"] = None

        if mode == "page":
            state["page"] = None
            renpy.restart_interaction()
            return

        ## 整个菜单退出：对话框趁遮罩/面板退场时淡回来
        ui_say_fade_in(UI_SAY_IN_TIME)
        ui_blip_resume()

        return renpy.run(Return())

    ## ---- 左侧选项表 ----

    def ui_nav_rows(mode):
        if mode == "game":
            return [
                ("返回游戏", "resume"),
                ("保存进度", "save"),
                ("读取进度", "load"),
                ("系统设置", "preferences"),
                ("历史文本", "history"),
                ("返回标题", "main_menu"),
                ("退出游戏", "quit"),
                ]
        return [
            ("开始游戏", "start"),
            ("继续游戏", "load"),
            ("系统设置", "preferences"),
            ("关于作品", "about"),
            ("退出游戏", "quit"),
            ]

    ## 菜单内部的"换页"状态：用一个可变 dict 存，按钮直接改它。
    ## 不用 SetScreenVariable —— 它在 use 出来的子屏幕里会乱掉（点不动）。
    def ui_set_state(state, key, value):
        state[key] = value
        renpy.restart_interaction()

    ## 鼠标停在"删除档案"上时，让整张卡保持深色（只让删除按钮变亮）
    def ui_card_hot(slot):
        if store._ui_card_hot_slot != slot:
            store._ui_card_hot_slot = slot
            renpy.restart_interaction()

    def ui_card_cool(slot):
        if store._ui_card_hot_slot == slot:
            store._ui_card_hot_slot = None
            renpy.restart_interaction()

    def ui_nav_action(mode, key, state):
        if key == "start":
            return Start()
        if key == "resume":
            ## 返回游戏：和 ESC 完全同一条出口（弹回 + 退出音），不走向右渐隐
            return Function(ui_close, state, "menu")
        if key == "quit":
            if mode == "game":
                return Function(ui_confirm,
                                "确定要退出游戏吗？\n当前未保存的进度将会丢失。",
                                Quit(confirm=False))
            return Quit(confirm=False)
        if key == "main_menu":
            return Function(ui_confirm,
                            "确定要返回标题主菜单吗？\n当前未保存的进度将会丢失。",
                            MainMenu(confirm=False))
        if key == "history":
            return Function(ui_history_request, state)
        if mode == "game":
            return Function(ui_open_page, state, key)
        return Function(ui_set_state, state, "page", key)

    ## ---- 右侧分类标签表 ----

    UI_PREF_TABS = [
        ("显示与画面", "display"),
        ("声音与音量", "audio"),
        ("文本与快进", "text"),
        ]

    ## 存档卡片：整张卡是一个按钮，返回 (主操作, 提示文字, 是否可用)
    def ui_slot_main(mode, slot, saved):
        if mode == "save":
            if saved:
                return (Function(ui_confirm,
                                 "覆盖这个档位？原有存档会被替换。",
                                 FileSave(slot, confirm=False)),
                        "覆盖存档", True)
            return FileSave(slot, confirm=False), "保存至该档位", True
        if saved:
            ## 主界面的读档：没有"当前进度会丢失"这回事，不需要确认
            if main_menu:
                return FileLoad(slot, confirm=False), "读取此档位", True
            return (Function(ui_confirm,
                             "读取这个档位？当前未保存的进度会丢失。",
                             FileLoad(slot, confirm=False)),
                    "读取此档位", True)
        return NullAction(), "暂无存档", False

    ## ---- 两个"非激活状态"开关 ----

    ## 非激活时降低 CPU：窗口失去焦点时给主循环每帧加一点等待，把帧率压下来
    ## （config.needs_redraw_callbacks 每帧都会被问一次，在这里睡眠最省事）
    def ui_low_cpu_tick():
        if not persistent.ui_low_cpu_unfocused:
            return False

        try:
            import pygame
            active = pygame.display.get_active()
        except Exception:
            return False

        if active:
            return False

        try:
            pygame.time.wait(UI_LOW_CPU_WAIT)
        except Exception:
            pass

        return False

    class ToggleLowCPU(Action):
        def __call__(self):
            persistent.ui_low_cpu_unfocused = not persistent.ui_low_cpu_unfocused
            renpy.restart_interaction()

        def get_selected(self):
            return bool(persistent.ui_low_cpu_unfocused)

    ## 非激活时静音：勾上 = 窗口切出去就把声音停掉（引擎的 audio_when_unfocused 反过来）
    class ToggleMuteUnfocused(Action):
        def __call__(self):
            preferences.audio_when_unfocused = not preferences.audio_when_unfocused
            renpy.restart_interaction()

        def get_selected(self):
            return not preferences.audio_when_unfocused

    ## 复选框当前状态（交给 action 自己判断，InvertSelected 之类也能用）
    def ui_action_selected(act):
        getter = getattr(act, "get_selected", None)
        if getter is None:
            return False
        try:
            return bool(getter())
        except Exception:
            return False

    ## 每帧都会被问一次（needs_redraw_callbacks），用来在非激活时降低帧率
    if ui_low_cpu_tick not in config.needs_redraw_callbacks:
        config.needs_redraw_callbacks.append(ui_low_cpu_tick)

    ## ---- 游戏层的对话框：进出菜单 / 历史页时由我们逐帧控制透明度 ----
    ## 引擎的 window_show_transition / window_hide_transition 只在"窗口真的被隐藏/显示"
    ## 的那一刻才触发；而进出菜单时窗口一直挂在屏幕上，所以那套转场根本不会跑 ——
    ## 这就是"对话框看起来是瞬间切换"的原因。这里用逐帧 alpha 动画接管。
    ## 状态：t0=None 表示没有动画在跑（此时停在 peak 这个不透明度上）。
    _say_fade = {"t0": None, "dur": 0.0, "mode": "idle",
                 "from": 1.0, "peak": 1.0, "last": 1.0, "hidden_at": 0.0}

    ## 注意：不能叫 ui_say_fade —— 那是下面 ATL transform 的名字，会互相覆盖。
    ## 统一模型：从"当前实际不透明度"匀速变到 peak，到了就停住（峰值即终点）。
    def ui_say_fade_begin(dur, peak, mode="to"):

        _say_fade["from"] = _say_fade["last"]
        _say_fade["peak"] = peak
        _say_fade["t0"] = _ui_time.monotonic()
        _say_fade["dur"] = max(dur, 0.01)
        _say_fade["mode"] = mode
        renpy.restart_interaction()

    def ui_say_fade_in(dur=UI_SAY_IN_TIME):
        ui_say_fade_begin(dur, 1.0)

    def ui_say_fade_out(dur=UI_SAY_OUT_TIME, peak=0.0):
        ui_say_fade_begin(dur, peak)

    ## 一次性三角波：先用 in_dur 匀速亮到 peak，紧接着用 out_dur 匀速暗到 0。
    ## 全程一条时间线，中间不留任何停顿（交接专用）。
    def ui_say_handoff_begin(in_dur, out_dur, peak):

        _say_fade["from"] = 0.0
        _say_fade["peak"] = peak
        _say_fade["t0"] = _ui_time.monotonic()
        _say_fade["in_dur"] = max(in_dur, 0.01)
        _say_fade["out_dur"] = max(out_dur, 0.01)
        _say_fade["mode"] = "handoff"
        renpy.restart_interaction()

    ## 立刻把对话框压到全透明（不动屏幕本身）。
    ## 专供"拍存档缩略图 / 打开菜单"用：这样 say 屏和里面的 Text 实例都还在，
    ## 打字打到一半的状态不会丢，退出菜单后还是从断点继续。
    def ui_say_hide_now():
        _say_fade["t0"] = None
        _say_fade["mode"] = "hidden"
        _say_fade["hidden_at"] = _ui_time.monotonic()
        _say_fade["last"] = 0.0
        _say_fade["peak"] = 0.0
        renpy.restart_interaction()

    def ui_say_alpha_fn(trans, st, at):

        ## 被 ui_say_hide_now() 压掉的状态：保持透明，直到下一次 fade_in。
        ## 加一层超时自愈：万一菜单没走正常退出（返回标题 / 读档 / 退出），
        ## 这个"隐藏"不能一直挂着，否则之后的新对话会全透明。
        if _say_fade["mode"] == "hidden":
            if _ui_time.monotonic() - _say_fade["hidden_at"] > 1.5:
                _say_fade["mode"] = "idle"
                _say_fade["t0"] = None
                _say_fade["peak"] = 1.0
                _say_fade["last"] = 1.0
            else:
                _say_fade["last"] = 0.0
                trans.alpha = 0.0
                return 0.02

        t0 = _say_fade["t0"]

        ## 交接用的一次性三角波：线段上升 → 紧接着线段下降 → 停在 0
        if _say_fade["mode"] == "handoff" and t0 is not None:

            t_in = _say_fade["in_dur"]
            t_out = _say_fade["out_dur"]
            peak = _say_fade["peak"]
            el = _ui_time.monotonic() - t0

            if el < t_in:
                a = peak * (el / t_in)
            elif el < t_in + t_out:
                a = peak * (1.0 - (el - t_in) / t_out)
            else:
                a = 0.0
                _say_fade["t0"] = None
                _say_fade["mode"] = "to"

            _say_fade["last"] = a
            trans.alpha = a

            return 0.01

        ## 没有动画在跑：停在 peak 上（常态 1.0，历史页淡出后是 0.0）
        if t0 is None:
            a = _say_fade["peak"]
            _say_fade["last"] = a
            trans.alpha = a
            return 0.02

        k = (_ui_time.monotonic() - t0) / _say_fade["dur"]

        if k >= 1.0:
            _say_fade["t0"] = None
            a = _say_fade["peak"]
            _say_fade["last"] = a
            trans.alpha = a
            return 0.02

        ## 直线匀速走完全程：起点 → peak（峰值就是终点，不再二次淡出）
        frm = _say_fade["from"]
        a = frm + (_say_fade["peak"] - frm) * k

        _say_fade["last"] = a
        trans.alpha = a

        return 0.01

    ## ---- 打字机拨片音（blip 通道）----
    ## 02_defines.rpy 里的回调是"开始打字 → 循环播一个短拨片，打完 → 停"。
    ## 打字打到一半打开菜单时，say 的交互被挂起，slow_done/end 不会来，
    ## 于是那个循环音会一直响下去（用户听到的"卡住一直循环"就是它）。
    ## 处理方式：进菜单/历史页时直接把这句的拨片**掐掉**（等于中断打字声），
    ## 回到游戏时如果这句还在打字，就重新把循环音接上（回调里的 slow_done/end 会再停它）。
    def ui_blip_stop():
        store._ui_blip_was_typing = bool(getattr(store, "_blip_typing", False))
        try:
            renpy.sound.stop(channel="blip")
        except Exception:
            pass

    def ui_blip_resume():
        if not getattr(store, "_ui_blip_was_typing", False):
            return
        if not getattr(store, "_blip_typing", False):
            ## 这句在菜单里已经打完/翻页了，不用再接
            return
        sound = getattr(store, "_blip_sound", None)
        if not sound:
            return
        try:
            renpy.sound.play(sound, channel="blip", loop=True)
        except Exception:
            pass

    ## 打开菜单：先把拨片掐掉
    def ui_blip_enter_menu():
        ui_blip_stop()

    ## 离开菜单/历史页：这句还在打字就接上
    def ui_blip_leave_menu():
        ui_blip_resume()

    ## 兜底：菜单收掉之后如果还有循环音在响、但当前不在打字，就停掉
    ## （比如从菜单里"返回标题"→ 开始游戏、或者读档之后）
    def ui_blip_guard():
        if renpy.context()._menu:
            return
        if getattr(store, "_blip_typing", False):
            return
        try:
            if renpy.music.get_playing("blip"):
                renpy.sound.stop(channel="blip")
        except Exception:
            pass

    if ui_blip_guard not in config.needs_redraw_callbacks:
        config.needs_redraw_callbacks.append(ui_blip_guard)

    ## 打开历史页：对话框淡出（慢一些，正好被遮罩吞掉）。不 hide 屏幕，
    ## 免得退出历史页时对话框"biu"地弹回来。
    def ui_hist_hide_game_ui():
        if renpy.get_screen("quick_menu") is not None:
            renpy.hide_screen("quick_menu")
        ui_blip_stop()
        ui_say_fade_out(UI_SAY_OUT_TIME)

    ## 关掉历史页：对话框淡入
    def ui_hist_show_game_ui():
        if renpy.get_screen("quick_menu") is None:
            renpy.show_screen("quick_menu")
        ui_say_fade_in(UI_SAY_IN_TIME)
        ui_blip_resume()


## 存档缩略图：等比缩放到卡片里
transform ui_shot_fit:
    xysize (UI_SHOT_W, UI_SHOT_H)
    fit "contain"


## 主菜单主标题入场：从下往上微微抬起 + 淡入（dur=0 时就是直接到位）
transform ui_title_in(dur=0.75, delay=0.0):
    alpha 0.0
    yoffset 26
    pause delay
    ease dur alpha 1.0 yoffset 0


## 对话框的透明度动画：由 _say_fade 状态驱动（见上面的 ui_say_alpha_fn）
transform ui_say_fade:
    function ui_say_alpha_fn


################################################################################
## 动效（注意 Ren'Py 的 ease 命名是反的：easein_* 是"先快后慢"）
################################################################################

## 黑色遮罩淡入：和历史记录页一样的一层压暗（很快，几乎瞬间压下去）
transform ui_overlay_in:
    alpha 0.0
    linear UI_OVERLAY_TIME alpha 1.0

## 退场时遮罩一起淡掉
transform ui_overlay_out:
    alpha 1.0
    linear UI_OVERLAY_OUT_TIME alpha 0.0

## 左侧灰面板：快速弹出，末尾轻微过冲再回落（easein_back 在结尾会超过 1）
transform ui_left_pop:
    xoffset -380
    easein_back UI_LEFT_POP_TIME xoffset 0

## 右侧内容：从右边滑出，先快、再快速减速、最后停住（纸页滑出的手感）
transform ui_right_slide:
    xoffset 1540
    easein_cubic UI_RIGHT_SLIDE_TIME xoffset 0

## 退出：右侧内容滑回右边（纸页被抽走），一级面板更快地弹回左边
transform ui_right_slide_out:
    xoffset 0
    easein_cubic UI_RIGHT_OUT_TIME xoffset 1540

transform ui_left_pop_out:
    xoffset 0
    easein_cubic UI_LEFT_OUT_TIME xoffset -380


################################################################################
## 样式
################################################################################

style ui_left_panel is frame:
    xsize 380
    yfill True
    padding (0, 0, 0, 0)
    background Solid(UI_LEFT_BG)

style ui_right_panel is frame:
    xpos 380
    xsize 1540
    yfill True
    padding (0, 0, 0, 0)
    background Solid(UI_RIGHT_BG)

## 历史页用：位置和右侧面板一样，但底色透明（只留半透明遮罩 + 卡片）
style ui_hist_panel is frame:
    xpos 380
    xsize 1540
    yfill True
    padding (0, 0, 0, 0)
    background Solid("#00000000")

## 黑描边的浅色框：外层画边框，内层画填充
style ui_box is fixed:
    background Solid(UI_LINE)
    padding (1, 1, 1, 1)

style ui_box_fill is fixed:
    background Solid("#ffffff")
    padding (14, 12, 14, 12)

## 左侧选项
style ui_nav_button is button:
    xsize 268
    ysize 62
    idle_background Solid(UI_NAV_IDLE_BG)
    hover_background Solid(UI_NAV_HOVER_BG)
    selected_background Solid(UI_NAV_SELECTED_BG)
    activate_sound UI_SFX_CLICK

style ui_nav_button_text is text:
    font gui.name_text_font
    size 27
    xalign 0.5
    yalign 0.5
    idle_color UI_NAV_IDLE_TEXT
    hover_color UI_NAV_HOVER_TEXT
    selected_idle_color UI_NAV_SELECTED_TEXT
    selected_hover_color UI_NAV_SELECTED_TEXT

## 右侧分类标签
style ui_tab_button is button:
    ysize 44
    xpadding 26
    idle_background Solid(UI_TAB_IDLE_BG)
    hover_background Solid(UI_TAB_HOVER_BG)
    selected_background Solid(UI_TAB_SELECTED_BG)
    activate_sound UI_SFX_CLICK

style ui_tab_button_text is text:
    font gui.name_text_font
    size 24
    yalign 0.5
    idle_color UI_TAB_IDLE_TEXT
    hover_color UI_INK
    selected_idle_color UI_TAB_SELECTED_TEXT
    selected_hover_color UI_TAB_SELECTED_TEXT

## 右侧文字
style ui_pane_title is text:
    font gui.name_text_font
    size 40
    color UI_INK

style ui_group_label is text:
    font gui.name_text_font
    size 26
    color UI_INK

style ui_body_text is text:
    font gui.text_font
    size 24
    color "#1f1f1f"

style ui_hint_text is text:
    font gui.text_font
    size 20
    color "#6a6a6a"

## 关于页的英文 credit 行：左边角色名右对齐窄栏，右边人名
style ui_credit_role is text:
    font gui.text_font
    size 20
    color "#6a6a6a"
    xsize 340
    textalign 1.0

## 小按钮（分类里的单选行 / 恢复默认 / 存档操作）
style ui_small_button is button:
    ysize 42
    xpadding 18
    idle_background Solid("#dcdcdc")
    hover_background Solid("#bcbcbc")
    selected_background Solid(UI_INK)
    insensitive_background Solid("#e8e8e8")
    activate_sound UI_SFX_CLICK

style ui_small_button_text is text:
    font gui.name_text_font
    size 22
    yalign 0.5
    idle_color UI_INK
    hover_color "#000000"
    selected_idle_color "#ffffff"
    selected_hover_color "#ffffff"
    insensitive_color "#8a8a8a"

## 复选框行
style ui_check_button is button:
    ysize 40
    xpadding 0
    background None
    activate_sound UI_SFX_CLICK

## 滑块（8 年前的 left_bar/right_bar 已改名 fore_bar/aft_bar，只有后者真正参与绘制）
## 滑条本身 10px 高（Solid 自带 ysize=10，靠 thumb_align 在 22px 的 bar 里居中），
## 手柄是 22x22 的白色方块（带 2px 黑边），比滑条更宽更高。
style ui_slider is bar:
    xsize 840
    ysize 22
    bar_resizing True
    thumb_align 0.5
    fore_bar Solid(UI_INK, ysize=10)
    aft_bar Solid("#d0d0d0", ysize=10)
    ## 手柄是比滑条更宽的白色方块（22 高 vs 10 高铁轨，上下各露 6px）。
    ## 图片按自然尺寸绘制；Solid/Composite 会被 thumb_dim 压成一条线，所以用 PNG。
    thumb "gui/ui_slider_thumb.png"
    thumb_offset 0

## 存档卡片：外框 1px，内部整块是可点按钮
style ui_slot_frame is frame:
    background Solid(UI_LINE)
    padding (1, 1, 1, 1)

style ui_slot_button is button:
    idle_background Solid("#f2f2f2")
    hover_background Solid(UI_SLOT_HOVER)
    activate_sound UI_SFX_CLICK

## 鼠标停在"删除档案"上时：整张卡保持悬停的深色（不能退回浅色），
## 只有删除按钮自己变亮。靠 ui_card_hot / ui_card_cool 记录当前被悬停的槽位。
style ui_slot_button_hot is button:
    idle_background Solid(UI_SLOT_HOVER)
    hover_background Solid(UI_SLOT_HOVER)
    activate_sound UI_SFX_CLICK

## 卡片里的截图区
style ui_slot_shot is fixed:
    background Solid("#232b3a")

style ui_slot_label is text:
    font gui.name_text_font
    size 18
    color "#ffffff"

style ui_slot_time is text:
    font gui.text_font
    size 19
    color "#333333"

style ui_slot_name is text:
    font gui.text_font
    size 22
    color UI_INK
    layout "nobreak"

## 卡片右下角的"删除档案"：平时灰字透明底，悬停时局部变白、字变红
style ui_delete_button is button:
    xpadding 14
    ypadding 6
    idle_background Solid("#00000000")
    hover_background Solid("#ffffff")
    activate_sound UI_SFX_CLICK

style ui_delete_button_text is text:
    font gui.text_font
    size 21
    idle_color "#8a8a8a"
    hover_color "#c62828"

## 确认弹窗
style ui_confirm_card is fixed:
    xsize 880
    background Solid(UI_LINE)
    padding (1, 1, 1, 1)

style ui_confirm_head is fixed:
    background Solid(UI_INK)
    padding (22, 12, 22, 12)

style ui_confirm_head_text is text:
    font gui.name_text_font
    size 21
    color "#ffffff"

## 弹窗正文第一行（问句）：大一号、深色
style ui_confirm_title is text:
    font gui.name_text_font
    size 30
    color UI_INK
    textalign 0.5
    line_spacing 8

## 弹窗正文第二行（说明）：小一号、浅灰
style ui_confirm_message is text:
    font gui.text_font
    size 20
    color "#8a8a8a"
    textalign 0.5
    line_spacing 6

style ui_confirm_yes is button:
    xsize 250
    ysize 62
    idle_background Solid(UI_INK)
    hover_background Solid("#3a3a3a")
    activate_sound UI_SFX_CLICK

style ui_confirm_yes_text is text:
    font gui.name_text_font
    size 25
    xalign 0.5
    yalign 0.5
    idle_color "#ffffff"
    hover_color "#ffffff"

style ui_confirm_no is button:
    xsize 250
    ysize 62
    idle_background Solid("#dcdcdc")
    hover_background Solid("#c2c2c2")
    activate_sound UI_SFX_CLICK

style ui_confirm_no_text is text:
    font gui.name_text_font
    size 25
    xalign 0.5
    yalign 0.5
    idle_color UI_INK
    hover_color "#000000"


## 历史文本页
style ui_hist_border is frame:
    background Solid("#cfcfcf")
    padding (1, 1, 1, 1)

style ui_hist_card is frame:
    background Solid("#ffffff")
    padding (24, 16, 24, 16)

style ui_hist_chip_border is frame:
    background Solid(UI_INK)
    padding (1, 1, 1, 1)

style ui_hist_chip_fill is frame:
    background Solid("#ffffff")
    padding (16, 2, 16, 2)

style ui_hist_name is text:
    font gui.name_text_font
    size 19
    color UI_INK

style ui_hist_meta is text:
    font gui.text_font
    size 15
    color "#9a9a9a"

style ui_hist_text is text:
    font gui.text_font
    size 21
    color "#262626"
    line_spacing 5


################################################################################
## 菜单主体
################################################################################

screen ui_menu(mode, start_page=None, start_ptab="display"):

    ## 屏幕级状态：当前右侧内容 / 系统设置的当前分类 / 退场状态
    ## 存在 store 里的一个 dict 里（由按钮直接改），这样 use 出来的屏幕也能正常切换，
    ## 也不会像 SetScreenVariable 那样在子屏幕里悄悄失效（点不动）。
    ## 每次显示菜单时由 ui_reset_state() 重置，见下面两个入口屏幕的 on "show"。
    $ ui_state = ui_store

    $ page = ui_state["page"]
    $ ptab = ui_state["ptab"]

    if mode == "game":

        $ _closing = ui_state.get("closing")

        ## 唤醒时看左侧面板弹到位的那一刻遮罩刚好完全；退场时一起淡掉
        if _closing == "menu":
            add Solid("#000000a8") at ui_overlay_out
        else:
            add Solid("#000000a8") at ui_overlay_in

        ## 两级返回：二级开着就先收二级，只剩一级时再关菜单。
        ## ESC / 右键 / 空格 三个键行为一致；退场动画期间按键被吃掉，免得连按把动画打断。
        if _closing:
            key "game_menu" action NullAction()
            key "mouseup_3" action NullAction()
            key "K_SPACE" action NullAction()

        elif page:
            key "game_menu" action Function(ui_close, ui_state, "page")
            key "mouseup_3" action Function(ui_close, ui_state, "page")
            key "K_SPACE" action Function(ui_close, ui_state, "page")

        else:
            key "game_menu" action Function(ui_close, ui_state, "menu")
            key "mouseup_3" action Function(ui_close, ui_state, "menu")
            key "K_SPACE" action Function(ui_close, ui_state, "menu")

        ## 退场动画跑完再真正收尾（收二级 / 关菜单）
        if _closing:
            $ _close_delay = UI_LEFT_OUT_TIME if _closing == "menu" else UI_RIGHT_OUT_TIME
            timer _close_delay action Function(ui_finish_close, ui_state)

        ## 左侧灰面板：快速弹出 + 末尾轻微回弹；退出时快速弹回左边
        frame:
            style "ui_left_panel"
            at (ui_left_pop_out if _closing == "menu" else ui_left_pop)
            use ui_left_content(mode, page, ui_state)

        ## 右侧内容：点了某项之后才从右边滑出来，把游戏画面完全盖住
        if page:
            frame:
                style "ui_right_panel"
                at (ui_right_slide_out if _closing in ("page", "menu") else ui_right_slide)

                if page == "preferences":
                    use ui_pane_preferences(ui_state)

                elif page == "save":
                    use ui_pane_archive("save")

                elif page == "load":
                    use ui_pane_archive("load")

                elif page == "about":
                    use ui_pane_about()

    else:

        ## 主界面：ESC / 右键 / 空格 取消当前选中，回到"只有标题栏"的默认状态
        if page:
            key "game_menu" action Function(ui_reset_state)
            key "mouseup_3" action Function(ui_reset_state)
            key "K_SPACE" action Function(ui_reset_state)

        else:
            key "game_menu" action NullAction()
            key "mouseup_3" action NullAction()
            key "K_SPACE" action NullAction()

        ## 主界面：静态，左右两块直接摆着（不需要动画）
        frame:
            style "ui_left_panel"
            use ui_left_content(mode, page, ui_state)

        frame:
            style "ui_right_panel"

            if page is None:
                use ui_pane_home

            elif page == "about":
                use ui_pane_about

            elif page == "save" or page == "load":
                use ui_pane_archive(page)

            else:
                use ui_pane_preferences(ui_state)


## 左侧灰面板的内容（主界面 / 临时菜单共用）
screen ui_left_content(mode, page, ui_state):

    ## 游戏内临时菜单：左上角白框放游戏标题（主界面不放，保持左右结构一致）
    if mode == "game":
        frame:
            style "ui_box"
            xpos 56
            ypos 56
            xsize 268
            ysize 96

            frame:
                style "ui_box_fill"
                background Solid("#ffffff")
                xfill True
                yfill True
                padding (10, 10, 10, 10)

                vbox:
                    xalign 0.5
                    yalign 0.5
                    spacing 4

                    text "二手时间":
                        font gui.name_text_font
                        size 30
                        color UI_INK
                        xalign 0.5

                    text "AFTER THE ROOFTOP":
                        font "fonts/ChillHuoSong_F_Regular.otf"
                        size 15
                        color "#6a6a6a"
                        xalign 0.5

    vbox:
        xpos 56
        ypos (212 if mode == "game" else 300)
        spacing 16

        for nav_label, nav_key in ui_nav_rows(mode):

            textbutton nav_label:
                style "ui_nav_button"
                action ui_nav_action(mode, nav_key, ui_state)
                selected (page == nav_key)
                hovered Function(ui_hover_sound)


## 系统设置（主界面右侧 / 临时菜单右侧共用）
screen ui_pane_preferences(ui_state):

    $ ptab = ui_state["ptab"]

    text "系统设置":
        style "ui_pane_title"
        xpos UI_PAD
        ypos 40

    add Solid(UI_LINE) xpos UI_PAD ypos UI_RULE_Y xsize 1400 ysize 3

    hbox:
        xpos UI_PAD
        ypos 132
        spacing 12

        for tab_label, tab_key in UI_PREF_TABS:

            textbutton tab_label:
                style "ui_tab_button"
                action Function(ui_set_state, ui_state, "ptab", tab_key)
                selected (ptab == tab_key)
                hovered Function(ui_hover_sound)

    if ptab == "display":
        use ui_pref_display

    elif ptab == "audio":
        use ui_pref_audio

    else:
        use ui_pref_text

    ## 恢复默认设置：不属于任何分类，任何分类下都固定在同一位置
    textbutton "恢复默认设置":
        style "ui_small_button"
        xpos UI_PAD
        ypos 840
        action Preference("reset")
        hovered Function(ui_hover_sound)


################################################################################
## 右侧内容
################################################################################

## 主界面首页：标题框 + 副标题框
screen ui_pane_home():

    frame:
        style "ui_box"
        xpos 70
        ypos 40
        xsize 1000
        ysize 214

        frame:
            style "ui_box_fill"
            background Solid("#ececec")
            xfill True
            yfill True

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 14

                text "二手时间":
                    font "fonts/ChillHuoSong_F_ExBold.otf"
                    size 96
                    color UI_INK
                    xalign 0.5

                text "AFTER THE ROOFTOP":
                    font "fonts/ChillHuoSong_F_Regular.otf"
                    size 26
                    color "#5c5c5c"
                    xalign 0.5

    frame:
        style "ui_box"
        xpos 70
        ypos 276
        xsize 1000
        ysize 86

        frame:
            style "ui_box_fill"
            background Solid("#ffffff")
            xfill True
            yfill True

            text "yuanshen is not a good game.":
                font gui.text_font
                size 34
                color UI_INK
                xalign 0.5
                yalign 0.5


## 关于作品
screen ui_pane_about():

    text "关于作品":
        style "ui_pane_title"
        xpos UI_PAD
        ypos 40

    add Solid(UI_LINE) xpos UI_PAD ypos UI_RULE_Y xsize 1400 ysize 3

    vbox:
        xpos UI_PAD
        ypos UI_BODY_Y
        spacing 16

        text "[config.name!t]":
            font gui.name_text_font
            size 34
            color UI_INK

        text "[config.version!t]":
            style "ui_hint_text"

        null height 10

        ## 以下是模板原有的英文 credit，保留原样
        use ui_credit_row(_("Updated Character Art"), _("Deji"))
        use ui_credit_row(_("Original Character Art"), _("Derik"))
        use ui_credit_row(_("Updated Background Art"), _("Mugenjohncel"))
        use ui_credit_row(_("Original Background Art"), _("DaFool"))
        use ui_credit_row(_("Music By"), _("Alessio"))
        use ui_credit_row(_("Update Written By"), _("Lore"))
        use ui_credit_row(_("Originally Written By"), _("mikey (ATP Projects)"))

        null height 12

        text _("Made with {a=https://www.renpy.org/}Ren'Py{/a} [renpy.version_only]"):
            style "ui_body_text"

        text _("[renpy.license!t]"):
            style "ui_hint_text"
            xsize 1300


screen ui_credit_row(role, who):

    hbox:
        spacing 15

        text role:
            style "ui_credit_role"

        text who:
            style "ui_body_text"


## 存档 / 读档
screen ui_pane_archive(mode):

    ## 右侧顶部页签：快速 / 自动 / 页 01-03
    hbox:
        xpos UI_PAD
        ypos 40
        spacing 12

        use ui_page_tab(("快速保存" if mode == "save" else "快速读取"), "quick", mode)
        use ui_page_tab(("自动保存" if mode == "save" else "自动读取"), "auto", mode)
        use ui_page_tab(("保存页 01" if mode == "save" else "读取页 01"), "1", mode)
        use ui_page_tab(("保存页 02" if mode == "save" else "读取页 02"), "2", mode)
        use ui_page_tab(("保存页 03" if mode == "save" else "读取页 03"), "3", mode)

    add Solid(UI_LINE) xpos UI_PAD ypos UI_RULE_Y xsize 1400 ysize 3

    grid 3 2:
        xpos UI_PAD
        ypos UI_BODY_Y
        spacing 26

        for slot in range(1, 7):
            use ui_slot_card(mode, slot)


screen ui_page_tab(label, page, mode):

    textbutton label:
        style "ui_tab_button"
        action FilePage(page)
        selected (str(persistent._file_page) == str(page))
        hovered Function(ui_hover_sound)


screen ui_slot_card(mode, slot):

    $ saved = FileLoadable(slot)
    $ slot_name = "SLOT %02d" % slot
    $ main_action, main_label, main_on = ui_slot_main(mode, slot, saved)
    $ save_title = FileSaveName(slot, empty="空档位")
    $ save_title = save_title if len(save_title) <= 15 else save_title[:15] + "…"

    frame:
        style "ui_slot_frame"
        xysize (UI_CARD_W + 2, UI_CARD_H + 2)

        fixed:
            xysize (UI_CARD_W, UI_CARD_H)

            ## 整张卡片就是一个按钮：悬停整体加深，点任意位置都算主操作
            button:
                style ("ui_slot_button_hot" if _ui_card_hot_slot == slot else "ui_slot_button")
                xysize (UI_CARD_W, UI_CARD_H)
                action main_action
                hovered Function(ui_hover_sound)

            ## ---- 内容层（不吃点击，事件穿透到上面的按钮）----

            fixed:
                style "ui_slot_shot"
                xpos 13
                ypos 13
                xysize (UI_SHOT_W, UI_SHOT_H)

                if saved:
                    add FileScreenshot(slot) at ui_shot_fit
                else:
                    text "暂无存档":
                        font gui.text_font
                        size 24
                        color "#8f8f8f"
                        xalign 0.5
                        yalign 0.5

            hbox:
                xpos 13
                ypos 252
                spacing 12

                frame:
                    background Solid(UI_INK)
                    padding (8, 2, 8, 2)

                    text slot_name:
                        style "ui_slot_label"

                text FileTime(slot, format="%Y/%m/%d %H:%M", empty="——"):
                    style "ui_slot_time"
                    yalign 0.5

            text save_title:
                style "ui_slot_name"
                xpos 13
                ypos 288
                xsize (UI_CARD_W - 26)

            ## 主操作提示（真正可点的范围是整张卡）
            frame:
                background Solid(UI_INK if main_on else "#c9c9c9")
                padding (14, 5, 14, 5)
                xpos 13
                ypos 330

                text main_label:
                    font gui.name_text_font
                    size 22
                    color ("#ffffff" if main_on else "#f2f2f2")

            ## 删除档案：只有鼠标落在它上面时才吃掉点击
            if saved:
                textbutton "删除档案":
                    style "ui_delete_button"
                    xalign 1.0
                    yalign 1.0
                    xoffset -12
                    yoffset -16
                    action Function(ui_confirm,
                                    "删除这个档位？删除后无法恢复。",
                                    FileDelete(slot))
                    hovered [Function(ui_hover_sound), Function(ui_card_hot, slot)]
                    unhovered Function(ui_card_cool, slot)


## 系统设置：显示与画面
screen ui_pref_display():

    vbox:
        xpos UI_PAD
        ypos 220
        spacing 22

        text "【画面模式】":
            style "ui_group_label"

        vbox:
            spacing 12

            use ui_choice_row("全屏显示",
                              Preference("display", "fullscreen"),
                              preferences.fullscreen)

            use ui_choice_row("窗口模式",
                              Preference("display", "window"),
                              not preferences.fullscreen)

        null height 14

        text "【过场与特效】":
            style "ui_group_label"

        ## 勾上 = 关掉所有转场（默认不勾 = 转场开着，和引擎默认一致）
        use ui_check_row("关闭转场效果",
                         InvertSelected(Preference("transitions", "toggle")))

        use ui_check_row("非激活状态时降低 CPU 使用率",
                         ToggleLowCPU())


## 系统设置：声音与音量
screen ui_pref_audio():

    vbox:
        xpos UI_PAD
        ypos 220
        spacing 26

        text "【音量输出控制】":
            style "ui_group_label"

        use ui_volume_row("主音量", "main")
        use ui_volume_row("背景音乐", "music")
        use ui_volume_row("环境音效", "sfx")
        use ui_volume_row("角色语音", "voice")

        null height 10

        text "【非激活状态】":
            style "ui_group_label"

        use ui_check_row("非激活状态游戏静音",
                         ToggleMuteUnfocused())


## 系统设置：文本与快进
screen ui_pref_text():

    vbox:
        xpos UI_PAD
        ypos 220
        spacing 26

        text "【文本显示与快进】":
            style "ui_group_label"

        use ui_text_speed_row()

        ## 自动前进：滑块按"整秒"吸附（step 1），读数只显示整数秒
        use ui_speed_row("自动前进等待时间",
                         FieldValue(_preferences, "afm_time", range=30, step=1, force_step=True),
                         "%d 秒" % int(round(preferences.afm_time)))

        null height 8

        use ui_check_row("跳过未读对话文本",
                         Preference("skip", "toggle"))

        use ui_check_row("遇到选择支后继续快进",
                         Preference("after choices", "toggle"))


## ---- 行元件 ----

screen ui_choice_row(label, act, sel):

    textbutton label:
        style "ui_small_button"
        action act
        selected sel
        hovered Function(ui_hover_sound)


screen ui_volume_row(label, mixer):

    $ pct = int(round(preferences.get_volume(mixer) * 100))

    fixed:
        xsize 1440
        ysize 40

        text label:
            style "ui_body_text"
            xpos 0
            xsize UI_ROW_LABEL_W
            yalign 0.5

        bar:
            style "ui_slider"
            xpos UI_VOL_BAR_X
            yalign 0.5
            value UIVolumeValue(mixer)

        text "[pct]%":
            style "ui_body_text"
            xpos UI_VOL_VALUE_X
            xsize UI_ROW_VALUE_W
            textalign 1.0
            yalign 0.5


## 文字输出速度：低 / 中 / 高 / 瞬间 四档（不再用滑块和 字/秒）
screen ui_text_speed_row():

    $ cur_tier = ui_cps_tier(preferences.text_cps)

    fixed:
        xsize 1440
        ysize 40

        text "文字输出速度":
            style "ui_body_text"
            xpos 0
            xsize UI_ROW_LABEL_W
            yalign 0.5

        hbox:
            xpos UI_ROW_BAR_X
            spacing 10
            yalign 0.5

            use ui_speed_choice("低", UI_CPS_LOW, cur_tier == UI_CPS_LOW)
            use ui_speed_choice("中", UI_CPS_MID, cur_tier == UI_CPS_MID)
            use ui_speed_choice("高", UI_CPS_HIGH, cur_tier == UI_CPS_HIGH)
            use ui_speed_choice("瞬间", 0, cur_tier == 0)


screen ui_speed_choice(label, cps, sel):

    textbutton label:
        style "ui_small_button"
        action SetField(_preferences, "text_cps", cps)
        selected sel
        hovered Function(ui_hover_sound)


screen ui_speed_row(label, value, readout):

    fixed:
        xsize 1440
        ysize 40

        text label:
            style "ui_body_text"
            xpos 0
            xsize UI_ROW_LABEL_W
            yalign 0.5

        bar:
            style "ui_slider"
            xpos UI_ROW_BAR_X
            yalign 0.5
            value value

        text readout:
            style "ui_body_text"
            xpos UI_ROW_VALUE_X
            xsize UI_ROW_VALUE_W
            yalign 0.5


screen ui_check_row(label, act):

    $ sel = ui_action_selected(act)

    button:
        style "ui_check_button"
        action act
        selected sel
        hovered Function(ui_hover_sound)

        hbox:
            spacing 12
            yalign 0.5

            frame:
                xysize (18, 18)
                background Solid(UI_INK)
                padding (1, 1, 1, 1)
                yalign 0.5

                add Solid(("#141414" if sel else "#ffffff")) xysize (16, 16)

            text label:
                font gui.text_font
                size 24
                color UI_INK
                yalign 0.5


################################################################################
## 确认弹窗
################################################################################

screen ui_confirm_dialog(message, yes_action, no_action=None):

    modal True
    zorder 300

    key "game_menu" action ([Hide("ui_confirm_dialog"), no_action] if no_action else Hide("ui_confirm_dialog"))
    key "mouseup_3" action ([Hide("ui_confirm_dialog"), no_action] if no_action else Hide("ui_confirm_dialog"))

    ## 正文拆两行：第一行是问句（大、深色），第二行是说明（小、浅灰）
    $ _ui_msg = message.split("\n", 1)
    $ _ui_head = _ui_msg[0]
    $ _ui_note = _ui_msg[1] if len(_ui_msg) > 1 else ""

    add Solid("#000000a8")

    ## 固定尺寸卡片，绝对定位，避免嵌套容器把边框挤歪
    fixed:
        xysize (880, 286)
        xalign 0.5
        yalign 0.5

        ## 1px 黑外框 + 白底
        add Solid(UI_LINE) xysize (880, 286)
        add Solid("#ffffff") xysize (878, 284) xpos 1 ypos 1

        ## 黑标题条
        add Solid(UI_INK) xysize (878, 50) xpos 1 ypos 1

        text "确认操作":
            style "ui_confirm_head_text"
            xpos 22
            ypos 13

        ## 正文整体居中在标题条与按钮之间的区域里
        fixed:
            xpos 1
            ypos 51
            xysize (878, 143)

            vbox:
                xalign 0.5
                yalign 0.5
                spacing 12

                text _ui_head:
                    style "ui_confirm_title"
                    xalign 0.5

                if _ui_note:
                    text _ui_note:
                        style "ui_confirm_message"
                        xalign 0.5

        hbox:
            xalign 0.5
            ypos 202
            spacing 44

            textbutton "确认":
                style "ui_confirm_yes"
                action [yes_action, Hide("ui_confirm_dialog")]
                hovered Function(ui_hover_sound)

            textbutton "取消":
                style "ui_confirm_no"
                action ([Hide("ui_confirm_dialog"), no_action] if no_action else Hide("ui_confirm_dialog"))
                hovered Function(ui_hover_sound)


################################################################################
## 历史文本
################################################################################

## 历史列表主体（临时菜单右侧、以及游戏内直接唤出的历史页共用）
screen ui_history_body():

    ## 只有最近若干条会被排版（HIST_LOAD_FIRST 条），往上翻到顶再追加。
    ## 一次排完 250 条的话首帧要 0.6 秒，按 ↑ 之后要等这么久页面才看得见。
    $ _ui_entries = hist_page_entries()
    $ _ui_base = len(_history_list) - len(_ui_entries)

    text "历史文本":
        style "ui_pane_title"
        color "#f4f4f4"
        xpos UI_PAD
        ypos 40

    text "回顾已经读过的对话":
        style "ui_hint_text"
        color "#b9b9b9"
        xpos UI_PAD
        ypos 90

    add Solid("#9a9a9a") xpos UI_PAD ypos UI_RULE_Y xsize 1400 ysize 2

    viewport:
        yadjustment hist_yadj
        draggable True
        scrollbars "vertical"
        side_yfill True
        xpos UI_PAD
        ypos (UI_BODY_Y + 8)
        xsize 1400
        ysize 796

        ## 滚动条用中性灰，别用模板自带的褐色主题条
        vscrollbar_xsize 10
        vscrollbar_base_bar Solid("#e0e0e0")
        vscrollbar_thumb Solid("#8f8f8f")

        vbox:
            spacing 12
            xsize 1330

            for _i in range(len(_ui_entries)):

                $ _h = _ui_entries[_i]

                frame:
                    style "ui_hist_border"
                    xsize 1330

                    frame:
                        style "ui_hist_card"
                        xsize 1328

                        vbox:
                            spacing 10
                            xfill True

                            hbox:
                                spacing 20
                                yalign 0.5

                                frame:
                                    style "ui_hist_chip_border"
                                    yalign 0.5

                                    frame:
                                        style "ui_hist_chip_fill"
                                        text (_h.who or "旁白"):
                                            style "ui_hist_name"

                                text ("第 %03d 条" % (_ui_base + _i + 1)):
                                    style "ui_hist_meta"
                                    yalign 0.5

                            text renpy.filter_text_tags(_h.what, allow=gui.history_allow_tags):
                                substitute False
                                style "ui_hist_text"
                                xsize 1280

            if not _ui_entries:
                text "还没有任何对话记录。":
                    style "ui_hint_text"
                    color "#c8c8c8"

    text "↑↓ / 滚轮 / PgUp·PgDn 翻阅　·　贴底继续往下 或 右键、空格、ESC 返回":
        style "ui_hint_text"
        color "#c8c8c8"
        xpos UI_PAD
        ypos 990


## 游戏内直接唤出的历史页：黑色遮罩 + 右面板从右侧滑出
screen ui_history_panel():

    ## 历史页只用一层半透明遮罩，右边不再压一块白板（卡片自己带底）
    add Solid("#000000a8") at ui_overlay_in

    frame:
        style "ui_hist_panel"
        at ui_right_slide
        use ui_history_body()


################################################################################
## 入口
################################################################################

## 打开菜单前先拍缩略图用：等这一帧重绘完（对话框已藏）再截图、还原、开菜单
screen ui_shot_watch():

    zorder -200
    timer 0.02 action Function(ui_shot_take)


## "历史文本"点完之后：菜单一收走就立刻接着唤出历史页（不停顿）。
## 用 repeat 轮询，菜单还没真的收完就下一帧再来，收完那一帧马上走。
screen ui_hist_watch():

    zorder -200

    if _ui_hist_pending[0]:
        timer 0.02 repeat True action Function(ui_hist_show)


## 主界面
screen main_menu():

    tag menu

    on "show" action Function(ui_reset_state)

    use ui_menu("main")


## 游戏内临时菜单（ESC、快捷菜单的"保存""设置"都走这里）
## 默认不选中任何一页：先只弹左侧灰面板，点了选项才滑出右侧内容。
screen ui_game_menu(start_page=None, start_ptab="display"):

    tag menu

    ## ESC 打开时响唤醒音；快捷菜单按钮打开时点击音已经响过，跳过这一声
    on "show" action [Function(ui_reset_state, start_page, start_ptab), Function(ui_menu_shown)]

    use ui_menu("game", start_page, start_ptab)

## ESC 打开的默认界面
define _game_menu_screen = "ui_game_menu"

## 点窗口右上角的叉：用我们自己的确认窗（和游戏内退出/返回标题同一套），
## 引擎自带的那个大概是模板残留的样式，不要用。
define config.quit_action = Function(ui_confirm,
                                    "确定要退出游戏吗？\n当前未保存的进度将会丢失。",
                                    Quit(confirm=False))

## ESC / 右键 / 手柄菜单键：走 ui_open_menu（先拍干净缩略图，再开菜单）
define config.game_menu_action = Function(ui_open_menu)
