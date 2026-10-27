## 03_defaults.rpy - 游戏动态状态与存档变量初始化 (default 铁律)
## 严格对标 01_renpy_basic_style_guide.md 规范：所有动态数值、分支标记均使用 default 声明

default current_chapter = 1
default player_route = "main"

# 情感与互动状态
default tomori_hope_value = 10
default anon_closeness = 0

# 关键事件线索标记
default ate_pumpkin_soup = False
default drank_strawberry_milk = False
default showed_notebook_to_anon = False
default accepted_anon_cheering = False
default received_discharge_slip = False

# 成就与周目持久化（persistent 声明）
default persistent.cleared_chapter_1 = False
default persistent.cleared_chapter_2 = False
default persistent.cleared_chapter_3 = False
default persistent.cleared_chapter_4 = False
default persistent.cleared_chapter_5 = False
default persistent.cleared_chapter_6 = False
default persistent.unlocked_pv = False
