## script.rpy - 游戏主流程入口与章节路由
## 严格对标 01_renpy_basic_style_guide.md 规范：jump 进行跨章节解耦路由
# 1. 定义全屏文字显示界面
screen say_fullscreen(who, what):
    frame:
        background None
        xfill True
        yfill True
        
        vbox:
            xalign 0.5      # 整个文字块在屏幕水平居中
            yalign 0.5      # 整个文字块在屏幕垂直居中
            xmaximum 1200   # 限制最大宽度，防止一行太长贴到屏幕边缘
            
            text what:
                id "what"
                style "say_dialogue"
                color "#ffffff" 
                text_align 0.5  # 每一行文字自身居中
                xalign 0.5
                
# 定义一个专属的全屏旁白角色
define n_fs = Character(None, screen="say_fullscreen")

label start:
    # 停止主菜单可能残留的音乐
    stop music fadeout 1.0

    # 初始化运行时变量
    $ current_chapter = 1

    # 章节选择或者直接进入第一章
    if persistent.cleared_chapter_1:
        # 这一页（黑底上的两个选项）不显示下方快捷按钮
        $ quick_menu = False
        menu:
            "【开始新故事】":
                jump ch01_awakening
            "【章节选择】":
                jump chapter_select_menu
    else:
        jump ch01_awakening

label chapter_select_menu:
    $ quick_menu = True
    scene bg hospital with fade
    menu:
        "选择要前往的章节："
        "第 1 幕：天台的雨水与被抢救的苏醒":
            jump ch01_awakening
        "第 2 幕：单人病房的墙壁与绝食沉默" if persistent.cleared_chapter_1:
            jump ch02_silence
        "第 3 幕：走廊的哭声与逃兵的驻足" if persistent.cleared_chapter_2:
            jump ch03_encounter
        "第 4 幕：越界的闯入与窗外的阴天" if persistent.cleared_chapter_3:
            jump ch04_intrusion
        "第 5 幕：活动室里的残缺笔记本" if persistent.cleared_chapter_4:
            jump ch05_notebook
        "第 6 幕：临近的体检日与七天死刑宣告" if persistent.cleared_chapter_5:
            jump ch06_verdict
        "返回":
            jump start

label game_credits:
    scene black with fade
    play music bgm_dialogue_warm fadein 2.0 loop

    centered "{size=48}《二手时间 - After the Rooftop》{/size}\n\n{size=28}全剧终{/size}"
    centered "{size=28}原案：BanG Dream! It's MyGO!!!!!\n角色：高松灯 · 千早爱音 · 长崎素世 · 丰川祥子 · 椎名立希 · 若叶睦{/size}"
    centered "{size=28}感谢您的阅读。{/size}"

    stop music fadeout 2.0
    return
