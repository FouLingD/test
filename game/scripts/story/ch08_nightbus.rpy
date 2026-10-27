## ch08_nightbus.rpy - 事件 18+19+20+21：街角大头贴与夜行巴士的微温
## 对应剧本：池袋大商场开门、草莓三明治与金平糖、街机厅抓企鹅玩偶、家庭餐厅偶遇立希、斑马线奔跑

label ch08_nightbus:
    $ current_chapter = 8

    # 1. 池袋商场上午十点开门
    scene bg mall_exterior with fade
    play music bgm_playful fadein 2.0 loop

    show anon windbreaker excited at center_standee with dissolve

    anon windbreaker excited "喂，小灯！快醒醒！到了！池袋站到了！"

    tomori windbreaker confused "……唔。到了？"

    "我揉了揉沉重的眼皮，额头从爱音温暖的肩窝上抬起来。"
    "晨雾已经散开了，高耸的池袋商场大楼在薄白的天光下矗立在眼前。"
    "上午十点整。"
    play sound sfx_auto_door
    "商场厚重的强化玻璃大门才刚刚向两侧推开。"
    "还没有什么人。整座庞大的建筑呈现出一种清冷的空旷。"
    "【高松灯的心绪】有时候我长时间感到空虚。"
    "我没有身份。在这座高速运转的城市矩阵里，在这座明亮的商场里，我就像一具会走路的木乃伊。仿佛我说话的时候，我已经不在了。"
    "我已经临近那个致命的日子，不到一百五十个小时。周围的人纯粹是在消磨时间，因为他们的时间多得用不完；而我，连消磨的资格都没有了。"
    "你为什么不自杀？你为什么还没有自杀？"
    "不，不是这么回事。有时候在病房里我也想过，在那座天桥上，在水泥路面最硬的地方。只要翻过栏杆，一切就都结束了。"
    "那为什么没有跳下去？"
    "因为我舍不得那些光线。在早班车车窗上的光线，在空旷商场玻璃穹顶上的光线。我总觉得，如果我死在病房里，那些光线就会失去见证人。"
    "而且，我还在等待。"
    "等一个能陪我走到最后的人。一个不会在我转身时离开的人。"
    "千早爱音拉着我的风衣袖口，走在空无一人的走廊正中央。"
    "现在，爱音来了。我们要活下去，把剩下的时间全部烧成灰烬。"

    # 2. 负一层面包店与金平糖
    scene bg bakery_cafe with dissolve

    show anon windbreaker excited at center_standee with dissolve

    anon windbreaker excited "哇！负一层开门了！面包房！"
    anon windbreaker excited "快来快来！草莓奶油三明治！两层厚奶油！小灯！吃这个！"

    tomori windbreaker expressionless "……太厚了。咽不下去。"

    anon windbreaker smile "哪会咽不下去啊！那这个呢？热牛奶！"
    anon windbreaker excited "还有这个！小铁盒！不对，玻璃瓶！"

    show item konpeito jar at right with dissolve
    tomori windbreaker expressionless "……星星。"

    anon windbreaker excited "是金平糖啦！蓝色的！粉色的！硬糖！"
    anon windbreaker smile "买！老板，结账！"

    hide item konpeito jar with dissolve

    "我们在扶梯边的长椅上坐下。长椅很凉。奶瓶很烫。"
    "瓶身直接贴在手心上，暖意顺着手腕爬上来。"
    "爱音一口咬下去，白色的奶油直接沾在了鼻尖上。"

    tomori windbreaker smile "……鼻子。"

    anon windbreaker surprised "哈？鼻子怎么了？"

    tomori windbreaker smile "鼻尖上……有白色的奶油。像小丑。"

    anon windbreaker smile "才不是小丑呢！小灯也来一口！"

    tomori windbreaker expressionless "不吃……"

    anon windbreaker smile "吃一口嘛！就一口！啊——！"

    tomori windbreaker expressionless "唔……太甜了。"

    "爱音笑得整个人倒在椅背上。"
    play sound sfx_candy_jar
    "我拧开玻璃罐，倒出一颗蓝色的金平糖，塞进嘴里。"
    $ renpy.pause(0.4, hard=False)
    play sound sfx_candy_crunch
    "咔嚓。咬碎了。"
    "我把糖罐放进风衣内袋，贴着肋骨。叮当，叮当。走动时有轻微的声响。"

    tomori windbreaker smile "……很甜。"

    anon windbreaker smile "甜就对了！走！"

    # 3. 三楼街机厅抓娃娃机
    scene bg arcade with dissolve
    stop music fadeout 1.5
    play music bgm_banter fadein 1.5 loop
    play bgs bgs_arcade fadein 2.0 loop

    "爱音没有多说什么，直接一把拽住我的手腕，拉着我快步冲上了三楼。"

    tomori windbreaker confused "爱音……走太快了……"

    anon windbreaker excited "抓紧！到了！"

    "三楼。大型室内游乐街机厅。"
    "一出扶梯，五彩斑斓的霓虹灯光和电子音乐劈头盖脸砸过来。跳舞机、推币机、赛车机。金属摇杆碰撞，硬币哗啦作响。"

    tomori windbreaker expressionless "……我确实从来没有玩过这些。十六年来，一次都没有。这些声音太吵了，光线太刺眼了。我以为这里只有正常人才能进来。"

    anon windbreaker smirk "少啰嗦！换硬币！"

    "爱音往兑币机里塞了一千日元。塑料盒里装满了沉甸甸的百元硬币。"

    show anon windbreaker excited at center_standee with dissolve

    anon windbreaker excited "看！橱窗里！"

    show item penguin plush at right with dissolve

    tomori windbreaker expressionless "……企鹅。"

    "一只圆滚滚的黑白小企鹅玩偶歪倒在出物口的边缘，圆溜溜的塑料黑眼睛正对着我们。"
    play sound sfx_coin_insert
    "爱音把一枚枚硬币投进投币孔里，机器发出一阵欢快的电子音乐。"
    "机械爪在玻璃箱里笨拙地移动，落下去又抓空。"

    anon windbreaker worried "啊！又滑掉了！怎么这么松啊！"

    tomori windbreaker smile "……噗。"

    anon windbreaker smirk "小灯你笑我！不服气，再来！"

    "爱音屡次失手，气得直跺脚。"
    "随后，爱音一把拉住我，把我推到了操作台正前方。"

    anon windbreaker confident "你来！本小姐给你护航！"

    tomori windbreaker confused "我……我不行的。"

    anon windbreaker smile "握住摇杆！"

    "爱音从背后握住我的手，带着我的手指一起握紧了黑色的塑料摇杆。"
    "我会变成什么。我害怕。快来。快来我身边。"

    anon windbreaker excited "就是现在！拍下去！"

    play sound sfx_strike
    "我用手掌用力拍下了红色的圆形按键。" with shake_h

    "三根机械爪笔直落下去，紧紧抓住了企鹅圆滚滚的肚子。"
    "齿轮转动，小企鹅被一把捞起，晃晃悠悠地悬在半空中。"
    play sound sfx_plush_drop
    "啪嗒。企鹅稳稳当当掉进了下方的出物口里。"

    play sound sfx_bell
    anon windbreaker excited "{size=+3}{b}哇啊啊啊！抓到了！抓到了！{/b}{/size}" with shake_h

    tomori windbreaker smile "……抓到了。爱音，我们抓到了。"

    anon windbreaker smile "那是当然！快抱好！这是我们的战利品！"

    hide item penguin plush with dissolve

    # 4. 四楼家庭餐厅偶遇立希
    stop bgs fadeout 1.5
    scene bg famires with dissolve
    stop music fadeout 1.5
    play bgs bgs_restaurant fadein 2.0 loop
    play music bgm_gloomy fadein 2.0 loop

    anon windbreaker smile "呼！四楼！家庭餐厅！吃热乎的去！"

    "我们在四楼的家庭餐厅坐下。爱音点了加了熏三文鱼的意面，还有一大盘炸薯条。"

    anon windbreaker smile "给！刚出锅的薯条！"

    tomori windbreaker expressionless "不要……我从来没吃过油炸的东西。"

    anon windbreaker smile "十六年没吃过薯条？！真的假的啊！那全归我啦！"

    "就在这个时候，一片阴影落在了我们的餐桌上。我抬起头。"

    show anon windbreaker smile at left_standee with dissolve
    show taki casual serious at right_standee with dissolve

    "是立希。"
    "她手里端着一只灰色的塑料托盘。托盘上放着一碗白色的杏仁豆腐，还有一罐印着黑白大熊猫图案的巧克力饮料。"

    taki casual serious "……灯？"

    "周围的嘈杂像是骤然悬停了片刻。"
    "刀叉碰撞的声音、小孩子的哭闹声、服务员传菜的呼喊声，全都退到了很远的地方，却又依然喧闹地存在着。"

    tomori windbreaker confused "……立希。"

    "我有些慌张地指了指对面的千早爱音，手指捏紧了膝盖上的纸餐巾。"

    tomori windbreaker expressionless "那个……这是千早爱音同学。爱音……这是立希……"

    taki casual serious "我知道。同班的？不对，在琴行还是哪里……"

    "立希的视线在爱音脸上冷淡地扫过，视线落在卡座上那只圆滚滚的企鹅玩偶上，眉头习惯性地蹙起，但很快又移回到了我的脸上。"
    "她端着托盘站在桌边，没有走，也没有坐下。"

    anon windbreaker smile "原来你们认识呀？要一起坐吗？"

    "立希没有回答爱音。她只是看着我。"

    taki casual concerned "那之后……你还好吗？"

    tomori windbreaker expressionless "对不起。"

    taki casual serious "为什么是你道歉？那天在练习室，说了重话的人是我。擅自发火的人也是我。"

    tomori windbreaker expressionless "不是的。是我没有唱好。是我总是让大家……"

    taki casual serious "你没有。灯从来都没有错。错的是……算了。"

    anon windbreaker surprised "等等，你们在说什么呀？什么练习室？什么道歉？"

    "没有人向爱音解释。"

    taki casual concerned "我那时候……我只是想让你继续唱下去。不管别人怎么说。"

    tomori windbreaker smile "我知道。对不起，立希。但是谢谢你。"

    taki casual concerned "所以说了不用道歉啊。……你看起来比之前精神一点了。"

    tomori windbreaker smile "嗯。刚才……我们抓到了这只企鹅。"

    taki casual serious "哈？企鹅？"

    anon windbreaker smile "是三楼的那个娃娃机啦！灯超级厉害的哦，最后拍下按键的时候——"

    "她们开始说话了。准确地说，是爱音在说，立希皱着眉头偶尔冷淡地回敬一两句。"
    "立希离我远着呢。就像我小时候掉进水池里，眼前漆黑一片，不管怎么挣扎，什么也抓不住。"
    "练习室也好，祥子也好，现在我想起来，反倒难过。"
    "我们俩都是无辜之人。只是我现在已经时日无多了。"

    "立希最后还是没有坐下。她端着她的杏仁豆腐和熊猫饮料走了，走之前对我说了一句话。"

    taki casual concerned "在学校遇到的话，打个招呼也没关系。"

    tomori windbreaker smile "……嗯。"

    hide taki with dissolve
    hide anon with dissolve

    # 5. 街角绿灯与奔跑
    stop bgs fadeout 1.5
    scene bg street with dissolve
    play music bgm_soaring fadein 2.0 loop

    "【高松灯的感悟】我又感到幸福。这真是不可思议。"
    "明明时间还在从地板的缝隙里往上漫，明明那个致命的日子还在前面的某处等着我。"
    "我还是那个不会呼吸的怪物，还是那个连一句完整的道歉都说不明白的人。"
    "但我刚才抓到了一只企鹅。我喝到了热牛奶。我把爱音介绍给了立希。哪怕明天就要迎来休止符。"
    "我热爱生活，哪怕它已经到了这个份上。很好，我找到合适的词了。热牛奶。红色的按钮。塑料桌布。"
    "这毫无意义，但最终，我们相信了。"

    show anon windbreaker excited at center_standee with dissolve

    play sound bgs_crosswalk
    anon windbreaker excited "小灯，快跟上！绿灯只有二十秒啦！"

    tomori windbreaker smile "……来了。"

    "她转过身，抓住我的手。快来，好走得更快。快。就这样。快。"
    play sound sfx_running_corridor
    "我们一起跑过了白色的斑马线。"

    stop music fadeout 2.5
    stop sound fadeout 1.5
    scene black with slow_dissolve

    $ persistent.cleared_chapter_8 = True
    jump ch09_haruhikage
