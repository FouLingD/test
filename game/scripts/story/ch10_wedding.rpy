## ch10_wedding.rpy - 事件 24+25+26：橱窗外的婚纱与anone的倒计时
## 对应剧本：爱音独白与医生报告单真相、清晨的结婚之约、Livehouse RiNG与立希摊牌谎言、天桥上的谅解与告别

label ch10_wedding:
    $ current_chapter = 10

    # 1. 爱音的独白与诊室记忆断片
    scene bg apartment_bedroom with fade
    play music bgm_anon_vulnerable fadein 2.0 loop

    "【千早爱音的独白】"
    "我听到一片海洋的声音，就在我身旁，只隔着一道砂堤。"
    "那是在伦敦。阴冷的雨季，狭小的寄宿房间。这片海洋是什么东西，要把我怎样摆布，那时的我连一点观念都没有。"
    "我只意识到这海洋要从堤岸上翻过来，那时……啊，那时才好呢，我就可以完全快乐了。"

    # 记忆断片 1
    scene bg hospital_corridor with dissolve
    doctor "你是帮501床来拿评估单的吧？回去告诉她，她没有任何问题。"
    anon "……什么？您的意思是……她一点事都没有？明天就能出院？"
    doctor "是啊，死神早就退场啦！我已经通知她母亲了，她家里人听说没有后遗症，终于松了一大口气。"

    scene bg apartment_bedroom with dissolve
    "【千早爱音的独白】"
    "小灯，这就是为什么当我第一次遇见你的时候，我会那样发疯似的高兴。"
    "我还记得那时候要向你开口有多难，多残忍。想要抓住你的欲念太强烈，简直找不到话来表达。"
    "连我自己也很难原谅我自己。"
    "我也为撒谎感到害怕。可我不能自制，好比人老想到死，有点像。"
    "我哄骗了你，也哄骗了我自己——我告诉你，我们的生活只剩下最后这几天了，过了这几天一切就都结束了。"
    "这感觉就像是一场偷窃。我把你从她们身边偷出来，又从你手里偷走了这几天的生命，像个小偷一样独自守在昏暗的房间里清点赃物。"
    "我为此感到羞耻，感到心惊肉跳；可是小灯，请你原谅我——除了撒谎，除了做这个卑劣的小偷之外，我已经没有任何别的办法能留住你了，也没有任何别的办法能活下去了。"

    # 2. 清晨的婚纱之约
    "晨光透过百叶窗的缝隙落在床单上。"
    "小灯醒着。她把脸贴在我的胸口，手指无意识地数着我的发梢。"

    show anon loungewear gentle at center_standee with dissolve

    tomori windbreaker expressionless "学校里的那些女孩子那么饶舌，你以前的乐队、还有我以前的乐队，她们很快就会知道我们的事情。她们会痛苦的。可能她们已经知道了。正因为我使你们痛苦，我们也该结婚了。"

    anon loungewear gentle "是的。"

    tomori windbreaker smile "我想为你穿一次婚纱。"

    anon loungewear blush "好啊。从第一夜起……我就很怕这个事……怕我做不好你的新娘，也怕做不好你的新郎。"

    tomori windbreaker smile "然后我们就去漫游世界。"

    anon loungewear smile "是这样的。到那时候，我们已经坐上离开这里的船了。"

    anon loungewear gentle "我们到海边去吧。就在九十九里滨那边，我订了一个看得到海的房间。"

    tomori windbreaker smile "什么时候去？"

    anon loungewear smile "随你的意。今天晚上。今天夜里。或者今天白天也可以。"

    "她安心地闭上眼睛，午后的热气漫进房间，她的呼吸渐渐变得绵长而均匀，终于沉沉睡去。"
    "我看了看床头的闹钟，轻轻抽出手臂，替她掖好被角。"

    anon loungewear gentle "你不是说想为我穿一次婚纱吗？趁你睡午觉，我出门去买点婚礼道具——头纱、戒指，还有今晚去海边要带的东西。乖乖等我回来。"

    tomori windbreaker smile "……嗯。"

    hide anon with dissolve

    # 3. 池袋 Livehouse RiNG 与立希的对峙
    scene bg livehouse_ring with dissolve
    stop music fadeout 1.5
    play music bgm_tense_1 fadein 1.5 loop

    "我推开池袋 Livehouse RiNG 的大门，顺着台阶走下去。"
    "下午的地下演出厅空空荡荡，只有吧台那边亮着几盏射灯。"
    "椎名立希就站在吧台后面。自从灯从医院失踪后，她显然没有睡过一个好觉。"

    show taki casual serious at center_standee with dissolve

    taki casual serious "……千早爱音？！你是干什么来的，你？！"

    anon windbreaker serious "我以为您是知道的。事关高松灯。"

    taki casual serious "灯？！你把灯拐到哪里去了？！她才刚从医院抢救过来，你这个莫名其妙冒出来的家伙到底对她灌了什么迷魂汤？！"

    anon windbreaker serious "请原谅，我不太了解您，但是您引起我的好奇……为什么您强迫自己摆出这副凶狠的样子？假的，它是假的。只有您一个人相信您在发火，其实您只是害怕得快要死了。"

    taki casual serious "你这家伙……把自己当成什么人了？！灯现在到底在哪儿？！"

    anon windbreaker gentle "她在我那里。睡在我的床上。很安全。"
    anon windbreaker serious "我来这儿，是因为昨天夜里她哭着跟我说，她还是忘不了之前的乐队。我要您对我说真话……在之前的乐队里，你们是不是有时候在折磨她？"

    taki casual serious "胡说八道什么！谁会折磨她！我一直都在保护她！是祥子那家伙……是那场莫名其妙的解散把她逼成这样的！"

    anon windbreaker serious "您说她“没法活下去”，就像大人说一个孩子“没治了”一样。"

    taki casual concerned "……你们到底发展到哪一步了？"

    anon windbreaker gentle "我以为您已经猜到了。我成了她的情人。"

    play sound sfx_strike
    taki casual serious "{size=+3}{b}你疯了？！她才多大，而且她刚从鬼门关回来，脑子根本不清醒！你这种轻浮的家伙，根本不知道她有多脆弱！{/b}{/size}" with shake_h

    anon windbreaker serious "我知道。从第一天起我就知道。因为她老怀着一种儿童才有的恐惧心理。害怕一切，怕雷雨、黑暗、人群、大海……怕你们，也怕我，怕一切。"
    anon windbreaker gentle "可即便她像你们说的那样“没治了”，我也爱她一辈子。"

    "地下室的空调发出低沉的嗡鸣。立希看着我，在她紧绷的唇际和目光中，我看到了和我一模一样的绝望与恐惧。"

    taki casual concerned "……那你到底为什么要来告诉我这些？！她什么时候走？马上告诉我日期。"

    anon windbreaker serious "就在这几天。她只有最后几天了。"

    taki casual concerned "确切说，是哪一天？"

    anon windbreaker serious "最晚六天以后，除非出了意外。"

    taki casual tears "那么说，没有任何希望了……这算什么事啊……我的天哪……"

    anon windbreaker gentle "……我多么希望这是真的。可是并不是。"

    taki casual serious "……你说什么？"

    anon windbreaker serious "我说，根本没有什么后遗症。医院的复查报告单现在就揣在我的口袋里——上面写着她只是贫血和神经性低热，身体早就康复了。"
    anon windbreaker tears "我多么希望她真的只剩下最后六天，那样她就永远只属于我一个人了……可是并不是。"

    play sound sfx_table_slam
    taki casual serious "{size=+4}{b}千早爱音——！！你他妈在耍我吗？！既然不是真的，那你为什么欺骗她？！{/b}{/size}" with shake_h

    anon windbreaker tears "对不起……对不起，我没有其他办法！！"
    anon windbreaker tears "那天下午在诊室门口，医生笑眯眯地跟我说“死神退场啦，她明天就能出院啦”，然后呢？！"
    anon windbreaker tears "她妈妈已经在千叶乡下找好了全封闭式的矫正机构！就算不去那里，回到羽丘的教室，回到你们那间撕碎了乐谱的排练室，你觉得她能撑过三天吗？！"
    anon windbreaker tears "我自私透顶，我卑劣得像个小偷，我靠着这个谎言才偷来了她这几天的温存……可是立希，对不起，我真的没有其他办法了！"

    taki casual concerned "……你疯了，千早。你们两个全都是疯子。……那等这七天过去呢？"

    anon windbreaker gentle "今晚我就带她去九十九里滨的海边。等她把那首新歌唱给大海听，等最后的一秒钟走完……如果她还是想死，我就陪她一起跳进海里；如果她愿意活下去，我就带她逃到谁也找不到的地方去。"

    taki casual concerned "……带我去看看她吧。如果揭穿你，她现在就会崩溃吧。我不提报告单的事，也不提以前乐队的事。我发誓。哪怕只是站在门外看她一眼……让我去跟她道个别，千早。"

    # 4. 铁路天桥上的对话与谅解
    scene bg railway_overpass with dissolve
    stop music fadeout 1.5
    play bgs bgs_train_overpass fadein 2.0 loop
    play music bgm_dialogue_warm fadein 2.0 loop

    show anon windbreaker gentle at left_standee with dissolve
    show taki casual concerned at right_standee with dissolve

    "阳光在桥面上移动，把我们的影子拉得很淡。"

    taki casual concerned "千早。对不起。刚才在下面，我不该那样对你大吼大叫。我不该骂你轻浮，也不该说你想把灯毁掉。"
    taki casual concerned "还有以前的事情……我也该道歉。是我太没用了。看着灯一个人站在暴雨里，浑身湿透，哭着把本子递给别人，可是没有任何人接过来……"

    anon windbreaker gentle "你什么也不知道，立希。这不能怪你。刚才在店里，我对你摆出的那副高傲样子，全都是装出来的。其实我自私透顶。我在英国搞砸了一切，灰溜溜地逃回日本……我甚至在利用她的脆弱……"

    taki casual concerned "但她笑了。自从那支乐队解散之后，我再也没见她笑过。可是在你的公寓里，她睡得那么安稳，还想着要为你穿婚纱。千早，虽然我还是很难喜欢你……但至少你让她活过来了。哪怕只有这几天。"

    "她望着远处的铁路线。列车正缓缓进站。"

    taki casual concerned "如果她说的是真的，如果她真的只有接下来几天了，那之后呢？我们会怎么样？我们会忘掉吗？"

    anon windbreaker gentle "不会忘掉。永远不会。"

    taki casual concerned "我们会回到各自的学校。我们会重新加入别的乐队，跟别的人一起弹琴、唱歌。然后有一天，我们会爱上别的人。"

    anon windbreaker gentle "是的。生活会逼着我们往前走。"

    taki casual concerned "即便过去几十年，这世上也再不会有第二个高松灯了。"

    anon windbreaker smile "是的。再也不会有了。"

    taki casual concerned "还好这一切不是真的。走吧。电车要开了。带我去看她。"

    stop music fadeout 2.5
    stop bgs fadeout 2.5
    scene black with slow_dissolve

    $ persistent.cleared_chapter_10 = True
    jump ch11_proposal
