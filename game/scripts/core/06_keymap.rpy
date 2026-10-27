## 06_keymap.rpy - 玩家操作习惯：隐藏对话框 / 历史记录 / 菜单
##
## 这里集中管理"玩家侧"的键盘与鼠标绑定，之后重做 UI 只改这一个文件即可。
##
## ┌───────────────────┬────────────────────────────────────────────────┐
## │ 右键 / 空格       │ 隐藏对话框（再按一次、或点击画面任意处恢复）   │
## │ 上滚轮 / ↑        │ 唤出历史记录（进去之后即为正常滚动翻阅）       │
## │ 左键 / 回车       │ 推进对话                                       │
## │ ESC               │ 游戏菜单（右键不再呼出菜单）                   │
## │ PageUp / PageDown │ 回退 / 取消回退（保留引擎默认）                │
## └───────────────────┴────────────────────────────────────────────────┘
##
## 实现要点：
##   1. Ren'Py 在 init 结束后才把 config.keymap 编译成事件匹配缓存
##      （renpy.display.behavior.init_keymap），所以必须在 init 阶段修改；
##      游戏运行中用 python 改是无效的。
##   2. config.keymap 的条目是 _keymap_list，developer 模式下 remove 一个
##      不存在的键会抛异常；统一走 _bind() 做存在性检查，因此 Shift+R 热重载
##      反复执行 init 也不会出问题。
##   3. "hide_windows" 就是引擎自带的 H 键逻辑（label _hide_windows）：
##      隐藏窗口 → 等一次点击或再次按键 → 恢复。它不会推进对话。

init -100 python:

    def _bind(binding, keysym, add=True):
        """向 config.keymap 的某个动作安全地追加 / 移除一个键位。"""
        keys = config.keymap.setdefault(binding, [])

        if add:
            if keysym not in keys:
                keys.append(keysym)
        else:
            while keysym in keys:
                keys.remove(keysym)

    ## 1) 隐藏对话框：右键、空格。引擎自带的中键与 H 键保留。
    _bind("hide_windows", "mouseup_3")
    _bind("hide_windows", "K_SPACE")

    ## 2) 右键不再呼出游戏菜单（否则与"隐藏对话框"冲突），菜单交给 ESC。
    _bind("game_menu", "mouseup_3", add=False)

    ## 3) 空格不再推进对话；推进改为左键 / 回车。
    _bind("dismiss", "K_SPACE", add=False)

    ## 4) 上滚轮不再触发回退，改为一键唤出历史记录。
    _bind("rollback", "mousedown_4", add=False)

    ## 5) 新增 "history" 动作：上滚轮 + ↑。
    ##    供 say / inner1_say / inner2_say / duet_say 等所有对话界面复用，
    ##    界面里写 `key "history" action OpenHistory()` 即可。
    _bind("history", "mousedown_4")
    _bind("history", "K_UP")

    ## 6) 历史记录页内部的滚动键位。这里用 anyrepeat，长按会连续触发，
    ##    配合滚动音效就是打字机连续敲击的效果。
    _bind("hist_up", "mousedown_4")
    _bind("hist_up", "anyrepeat_K_UP")
    _bind("hist_down", "mousedown_5")
    _bind("hist_down", "anyrepeat_K_DOWN")
    _bind("hist_pageup", "anyrepeat_K_PAGEUP")
    _bind("hist_pageup", "anyrepeat_KP_PAGEUP")
    _bind("hist_pagedown", "anyrepeat_K_PAGEDOWN")
    _bind("hist_pagedown", "anyrepeat_KP_PAGEDOWN")
