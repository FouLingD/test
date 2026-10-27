## 01_config.rpy - 引擎底层设置与多通道音频注册
## 严格对标 Ren'Py 8 架构与 03_visual_novel_audio_specification.md 规范

init -1 python:
    # 1. 注册专属音频通道
    # 拨片/打字机专属通道（单发或短促循环，受 SFX 音量滑条控制）
    renpy.music.register_channel("blip", mixer="sfx", loop=False)

    # 持续环境声通道（BGS），独立混音循环
    renpy.music.register_channel("bgs", mixer="sfx", loop=True)

    # 心理/低频音效通道（心跳、耳鸣、回响）
    renpy.music.register_channel("psycho", mixer="sfx", loop=True)

    # 单发环境演出音效通道
    renpy.music.register_channel("ambient_sfx", mixer="sfx", loop=False)

    # UI 界面音效通道（历史页滚动打字声等）。
    # 与 blip 分开：翻历史时不会打断对话框正在循环的打字机拨片。
    # 用了 3 个通道轮转（见 07_history_fx.rpy 的 HIST_TICK_CHANNELS）：
    # 一次快速连滚里相邻两声落在不同通道上，就不会后一声把前一声掐掉。
    renpy.music.register_channel("ui_tick_0", mixer="sfx", loop=False)
    renpy.music.register_channel("ui_tick_1", mixer="sfx", loop=False)
    renpy.music.register_channel("ui_tick_2", mixer="sfx", loop=False)

    # 2. 语音自动闪避（Voice Ducking）实现
    # 通过通道音量控制为人声让出声场频段 (-6dB ~ -8dB 避让)
    def duck_music():
        renpy.music.set_volume(0.40, delay=0.2, channel="music")

    def restore_music():
        renpy.music.set_volume(1.0, delay=0.4, channel="music")


    # 3. 默认打字速度（字符/秒，打字机拨片演出所需）
    if preferences.text_cps == 0:
        preferences.text_cps = 35

    # 4. 回退与存档安全性保护
    config.rollback_enabled = True
    config.hard_rollback_limit = 200
    config.has_autosave = True
    config.autosave_frequency = 25

    # 5. 原生加粗字体映射
    config.font_replacement_map["fonts/ChillHuoSong_F_Regular.otf", True, False] = ("fonts/ChillHuoSong_F_Bold.otf", False, False)
