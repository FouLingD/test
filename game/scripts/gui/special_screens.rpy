## special_screens.rpy - Figma Special Screens Implementation
## Strictly adheres to native 1920x1080 Figma design specifications:
## - 启动页 (Frame 2003:31)
## - 内心戏 1 (Frame 2006:195)
## - 内心戏 2 (Frame 2006:202)
## - 对唱 (Frame 2005:155)

################################################################################
## 1. 启动页 (Splashscreen) - Figma 2003:31
################################################################################

screen splash_screen_display():
    add "gui/splash_bg.png"

    # Centered focus box at (647, 290, 626, 413)
    frame:
        xpos 647
        ypos 290
        xsize 626
        ysize 413
        background None
        padding (40, 40, 40, 40)

        vbox:
            xalign 0.5
            yalign 0.5
            spacing 24

            text "二手时间":
                font "fonts/ChillHuoSong_F_ExBold.otf"
                size 54
                color "#000000"
                xalign 0.5
                at ui_title_in(0.85, 0.0)

            text "AFTER THE ROOFTOP":
                font "fonts/ChillHuoSong_F_Regular.otf"
                size 22
                color "#666666"
                xalign 0.5
                at ui_title_in(0.85, 0.16)

            null height 16

            text "— LOADING —":
                font "fonts/ChillHuoSong_F_Regular.otf"
                size 20
                color "#999999"
                xalign 0.5
                at ui_title_in(0.85, 0.34)

label splashscreen:
    show screen splash_screen_display
    with dissolve
    $ renpy.pause(1.2, hard=True)
    hide screen splash_screen_display
    with dissolve
    return


################################################################################
## 2. 内心戏 1 (Inner 1) - Figma 2006:195 (大情绪宽框独白)
################################################################################

screen inner1_say(who, what):
    ## 操作习惯：上滚轮 / ↑ 唤出历史记录
    key "history" action OpenHistory()

    add "gui/inner_1_bg.png":
        at ui_say_fade

    # Upper large focus box at (323, 117, 1274, 586)
    window:
        id "window"
        at ui_say_fade
        xpos 323
        ypos 117
        xsize 1274
        ysize 586
        background None
        padding (60, 60, 60, 60)

        vbox:
            xalign 0.5
            yalign 0.5
            xfill True

            text what id "what":
                font gui.text_font
                size 34
                color "#000000"
                line_spacing 16
                xalign 0.5
                text_align 0.5

    # Bottom quick menu
    use quick_menu

define inner1 = Character(
    None,
    screen="inner1_say",
    what_color="#000000",
    what_slow_cps=28
)


################################################################################
## 3. 内心戏 2 (Inner 2) - Figma 2006:202 (居中聚焦核心独白)
################################################################################

screen inner2_say(who, what):
    ## 操作习惯：上滚轮 / ↑ 唤出历史记录
    key "history" action OpenHistory()

    add "gui/inner_2_bg.png":
        at ui_say_fade

    # Centered focus box at (647, 290, 626, 413)
    window:
        id "window"
        at ui_say_fade
        xpos 647
        ypos 290
        xsize 626
        ysize 413
        background None
        padding (45, 45, 45, 45)

        vbox:
            xalign 0.5
            yalign 0.5
            xfill True

            text what id "what":
                font gui.text_font
                size 30
                color "#000000"
                line_spacing 14
                xalign 0.5
                text_align 0.5

    # Bottom quick menu
    use quick_menu

define inner2 = Character(
    None,
    screen="inner2_say",
    what_color="#000000",
    what_slow_cps=25
)


################################################################################
## 4. 对唱 (Duet) - Figma 2005:155 (双人立绘对峙与歌词碰撞)
################################################################################

default duet_left_image = "images/characters/side/side_tomori_hospital_smile.png"
default duet_right_image = "images/characters/side/side_anon_hospital_smile.png"
default duet_stage_lyric = "— 春日影与回音 —"

screen duet_say(who, what):
    ## 操作习惯：上滚轮 / ↑ 唤出历史记录
    key "history" action OpenHistory()

    add "gui/duet_bg.png":
        at ui_say_fade

    # Upper Left Avatar Box (162, 203, 300, 300)
    if duet_left_image:
        add duet_left_image:
            at ui_say_fade
            xpos 162
            ypos 203
            xsize 300
            ysize 300
            fit "contain"

    # Upper Right Avatar Box (1461, 203, 300, 300)
    if duet_right_image:
        add duet_right_image:
            at ui_say_fade
            xpos 1461
            ypos 203
            xsize 300
            ysize 300
            fit "contain"

    # Center Stage Dark Box at (323, 117, 1274, 500)
    if duet_stage_lyric:
        frame:
            xpos 323
            ypos 117
            xsize 1274
            ysize 500
            background None
            padding (40, 40, 40, 40)

            text duet_stage_lyric:
                font "fonts/ChillHuoSong_F_Bold.otf"
                size 36
                color "#ffffff"
                xalign 0.5
                yalign 0.5
                text_align 0.5

    # Bottom Dialogue Box at (142, 703, 1636, 280)
    window:
        id "window"
        at ui_say_fade
        xpos 142
        ypos 703
        xsize 1636
        ysize 280
        background None
        padding (50, 40, 50, 40)

        vbox:
            yalign 0.5
            xfill True

            if who is not None:
                text who id "who":
                    font gui.name_text_font
                    size 36
                    color "#000000"
                    xalign 0.0

            text what id "what":
                font gui.text_font
                size 32
                color "#000000"
                line_spacing 10
                xalign 0.0

    # Bottom quick menu
    use quick_menu

define duet = Character(
    None,
    screen="duet_say",
    what_color="#000000",
    what_slow_cps=35
)
