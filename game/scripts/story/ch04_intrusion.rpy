## ch04_intrusion.rpy - 事件 06+07+08：越界的闯入与窗外的阴天
## 对应剧本：草莓牛奶的慰问、羽丘高校的秘密、窗前的阴天与拉钩约定
## 包含完整原案 112 个文本块、共 260 句对白与旁白，100% 完整保留无任何删节。

# from __unknown__ import bgm_music_box
label ch04_intrusion:
    $ current_chapter = 4

    # 阴天病房，爱音的越界闯入
    scene bg hospital_room with fade
    play bgs bgs_hospital fadein 2.0 loop
    play music bgm_searching fadein 2.0 loop


    
    "真奇怪。"
    "一天前，我还一心盼着自己的内脏慢慢停止跳动。"
    "“你不想知道自己的情况吗？”那时一个护士这样对我说。"
    "我摇了摇头，不算肯定也不算肯定，我的身体情况我自然清楚不过。"
    "我心里清楚。或许那些仪表能很好地反映我的身体在发生什么，但是它们无法解释我的内心发生着什么。"
    "虽然我的誓言向来缺少公信力。但是，我还是准备好了在有勇气和健康的时候去死，最好的时间是一天前，其次就是现在。"
    "那时候，我讨厌任何递到嘴边的热气，讨厌护士换药时撕开胶布的声响，更讨厌窗外透进来的每一缕光线。"
    "可是今天中午，当护士把那一小碗南瓜粥端进来的时候，我居然握着勺子，慢慢把它喝完了。"
    "甚至连医生查房时递过来的温水，我也乖乖喝了半杯。"
    "因为我在心里悄悄算着时间。"
    "如果我不吃东西，护士就会一直在房间里念叨，下午的探视时间就会被各种各样的检查占满。"
    "那样的话……千早爱音推门进来的时候，我就没有力气和她说话了。"
    "如果她完全不期待和我说话，但愿如此，这只是我自作多情。"
    "不过，但凡她希望来见我一面，尽管这听起来不太可能，我辜负了她的心意，就太不应该了。"
    "她比我好上千倍万倍，如果我都能得到垂怜，那么她也一样。"
    "我的脑子里还是一遍又一遍地排演那些场景。"
    "在喝那半杯温水的时候，又或者只是靠在铁床边漫无目的地消磨时间，我都会忍不住开始想。"
    "要是她问我今天感觉怎么样，我是该回答“还好”，还是该告诉她“肋骨没有前两天那么疼了”？"
    "要是她又开始吹嘘伦敦的大本钟和红茶，我是该安静地听着，还是该问她司康饼到底是什么味道？"
    "这些琐碎得毫无意义的念头，在我的脑子里转来转去，竟然把那些关于冰冷雨水和天台铁丝网的噩梦挤开了一大半。"

    # 爱音带来草莓牛奶
    play sound sfx_door_slide
    play music bgm_anon_theme fadein 1.5 loop
    show anon hospital smile at center_standee with dissolve



    anon hospital smile "哈喽！{w=0.4}高松同学！"
    anon hospital smile "今天精神看起来不错嘛！"

    "她很自然把门反手关上了。"

    tomori hospital expressionless "……千早同学。"

    anon hospital smirk "都说了多少遍啦，叫我爱音！"
    anon hospital smile "看！我今天冒着被护士长抓包的危险，去自动贩卖机抢到的战利品！"

    tomori hospital expressionless "……草莓牛奶？"

    voice "audio/voice/vo_anon_04_01.ogg"
    anon hospital smile "两瓶！刚好是最后两瓶！"

    "还没等到我拒绝，她就给牛奶插上吸管，把玻璃瓶塞到了我手里。"

    tomori hospital smile "……谢谢爱音。"

    "听到“爱音”两个字，她的嘴角满意地翘起来，露出右边那颗尖尖的小虎牙。"
    "她吸了一大口牛奶，两只脚在椅子下面晃来晃去。"
    "爱音喝着牛奶，她看起来是个好人。"
    "起初我还以为她是想耍我，或者搞什么恶作剧，但现在看来并非如此。"
    "不要再与世界作对，我建议自己，去爱现实。"
    "爱音没有和我这么说，但是我渐渐要把自己说服了。"

    play sound sfx_glass_clink
    "草莓牛奶的玻璃瓶贴着我的手心，光滑温润。"
    "十六年来，每当大人们把东西递到我手里的时候，眼神里总是带着防备的叹息，好像我随时都会把杯子摔碎一样。"
    "可是千早爱音不一样。"
    "她把牛奶放在床头桌上，炫耀着自己如何在自动贩卖机前抢赢了别人。"
    "她没有问我手腕还疼不疼，也没有问我为什么站在天台上。"
    "她只是把一瓶甜甜的饮料塞进我手里，理直气壮地找我讨要人情。"

    anon hospital smile "对了高松同学，我昨天看你病历卡上写着16岁，你是在哪所学校念书啊？"

    tomori hospital expressionless "羽丘女子学园。"

    anon hospital smile "羽丘？！"
    anon hospital surprised "{size=+4}真的假的？！{/size}"
    anon hospital smile "我回国之后办转学手续，家里安排的也是羽丘诶！"

    tomori hospital expressionless "……真的吗？"

    anon hospital smile "当然是真的啦！"
    anon hospital smile "本来我还担心回国插班会跟不上大家，没想到居然在医院里先遇到了未来的同校同学！"
    anon hospital smile "那我们以后不就是同级的校友了吗！"

    "她趴在病床边的铁栏杆上，凑得很近。"
    "我能闻到她身上洗发水的气味。"

    anon hospital smile "喂，高松同学，羽丘的校风怎么样？"
    anon hospital smile "大家平时下课都会去哪里玩啊？"

    tomori hospital expressionless "我……不太清楚。"
    tomori hospital expressionless "下课的时候，我一般都在教室角落里坐着。"
    tomori hospital expressionless "或者去操场边上看落叶。"

    anon hospital smile "诶？看落叶？"
    anon hospital smile "你平时在学校都不和别人聊天的吗？"

    tomori hospital expressionless "……不太会聊天。"
    tomori hospital expressionless "大家聊的话题，我都听不懂。"

    anon hospital smile "那又怎样？你是挺怪的，但我就喜欢你这点——"
    anon hospital smile "反正等我去了羽丘，和我一起玩就够了嘛。"

    tomori hospital expressionless "……"

    "我有多久没像这样跟人聊天了？"
    "感觉像是过了好几个世纪。"
    "爱音啊……"
    "真的，我好久没试过这么轻松地跟人说话了。"
    "之前我都在干什么呢？这可怪罪不到其他人头上。"
    "爱音的视线在床头柜上扫了一圈，突然停在了那昨天没有看完的本子上。"


    #这段可以做的搞一点，很明显的抖包袱的地方（）

    play music bgm_tense_1 fadein 0.4 fadeout 0.4 loop

    anon hospital smile "咦？这是什么？"
    anon hospital smile "昨天我就想问了，日记本？还是作业？"

    tomori hospital expressionless "……是写歌词的本子。"


    "爱音整个人像是被点着了一样，眼睛瞬间亮起来。"



    anon hospital smile "歌词？！"
    anon hospital smile "音乐？！"
    anon hospital smile "高松同学你居然在写歌词？！"

    tomori hospital expressionless "……以前写的。"
    tomori hospital expressionless "现在……不写了。"


    play music bgm_tense_2 fadein 0.4 fadeout 0.4 loop



    "她完全没有理会我的后半句话，兴致勃勃地翻开封皮。"

    anon hospital smile "我看看我看看！"
    anon hospital smile "哇，字写得还挺工整的嘛……"

    "病房里一下子安静了下来。"
    "爱音低着头，手指按在活页本的纸张边缘。"
    "她盯着本子看了好几秒钟，慢慢把散落的粉色发丝撩到耳后。"

    play music bgm_tense_3 fadein 0.4 fadeout 0.4 loop


    "我祈祷她不会看见那些内容！"
    "不行！我急忙伸出手去，想要把它从爱音手里抢回来。"

    "爱音稍刚好避开了我伸过去的手。"

    anon hospital smile "喂，别乱动嘛，病人就给我好好躺着！"
    anon hospital smile "……等一下，这一行写的是什么？"




    tomori hospital expressionless "快给我！"

    "爱音停住了。"


    play music bgm_tense_rest fadein 1.0 fadeout 1.0 loop

    anon hospital smile "你的歌词很酷。"
    anon hospital smile "写得很有意思。"

    tomori hospital expressionless "……啊？"

    # 抖包袱段落结束，淡出紧张配乐，回到这一段之前的日常曲
    play music bgm_anon_theme fadein 2.0 fadeout 1.5 loop

    "她把本子抱在怀里，歪着脑袋，若有所思地盯着床头柜上的那束白百合花。"

    anon hospital smile "我刚不就这意思嘛！我说真的，不要质疑我的眼光！"
    anon hospital smile "写了又不给人看，那还有什么意义？"
    anon hospital smile "不过话说回来……"
    anon hospital confident "高松同学，前两天来病房看你的那几个人……该不会就是你之前的乐队队友吧？"

    tomori hospital expressionless "爱音……看见她们了？"

    anon hospital smile "当然看到了！那天下午我正好在走廊里晃悠呢！"

    tomori hospital expressionless "……嗯。"
    tomori hospital expressionless "是立希买给我的花。"
    tomori hospital expressionless "她们……确实是我以前的队友。"

    anon hospital smile "诶，原来是这样吗？"
    anon hospital smile "那后来怎么不玩了？"
    anon hospital smile "是吵架了吗？还是音乐理念不同什么的呢？"

    stop music

    tomori hospital expressionless "是我……"

    "我低着头，不敢看爱音的眼睛。"
    "离别没有来临，但未来确实会来。"
    "这一次我汲取了教训。我停止奢望。"
    "也许，我最终也会停止追赶你。"

    tomori hospital expressionless "因为我唱得太差了。"
    tomori hospital expressionless "在舞台上发不出声音……连一句完整的歌词都唱不出来。"
    tomori hospital expressionless "大家为了照顾我，付出了那么多努力。"
    tomori hospital expressionless "可是我却把演出全毁了……"
    tomori hospital expressionless "祥子把乐谱撕掉了，立希和大家吵架了……"
    tomori hospital expressionless "全都是因为我。"
    tomori hospital pensive "如果不是因为我太笨拙……大家就不会解散了。"
    tomori hospital tears "对不起……真的对不起……"

    "爱音突然重重地把玻璃瓶往桌上一放，发出当的一声脆响。"

    play music bgm_happy_bop fadein 1.5 loop



    anon hospital surprised "哈？！"
    anon hospital smile "你道什么歉啊？！"
    anon hospital smile "行啦，你也不需要道歉的！"
    anon hospital smile "那事跟你又没关系！"

    "我猛地抬起头，满脸茫然。"

    tomori hospital expressionless "……啊？"
    tomori hospital expressionless "也……没关系？"

    "她翻了个大大的白眼，气呼呼地抱起手臂。"

    anon hospital smile "废话！"
    anon hospital smile "乐队是好几个人一起玩的东西吧？"
    anon hospital smile "演出出了状况，大家一起想办法解决不就好了吗！"
    anon hospital smile "凭什么一个人撕了乐谱跑掉，所有责任就全变成你的错了啊？"
    anon hospital smile "他们会以此为借口，彻底把事情甩到一边！"
    anon hospital smile "那些动不动就把责任推给别人、搞得大家都不开心的家伙，光是听着就让人心烦！"

    tomori hospital expressionless "……心烦？"

    anon hospital smile "对啊！超烦的！"
    anon hospital smile "最讨厌这种动不动就甩脸子搞得全天下都欠她一样的做派了！"
    anon hospital smile "高松同学你也是，干嘛把什么黑锅都往自己身上揽啊！"
    anon hospital smile "你又不是垃圾桶！"

    "看着我发呆的表情，爱音有些不自然地咳了一声。"

    anon hospital smile "咳！"
    anon hospital smirk "好啦，过去的事情就让它过去嘛！"
    anon hospital smile "反正等我去了羽丘，我肯定是要组一支全校最闪耀的女子乐队的！"

    tomori hospital expressionless "……爱音要组乐队？"

    "她站起身来，得意洋洋地比划着弹吉他的姿势。"

    anon hospital smile "当然！"
    anon hospital smile "我在英国的时候就看中了一把超好看的粉色电吉他！"
    anon hospital confident "回国之后我一定要买下来！"
    anon hospital smile "到时候，我要站在舞台最中间！"
    anon hospital excited "高松同学，你既然会写词，那等我组了乐队，你就来给我当主唱！"

    tomori hospital expressionless "我……？"
    tomori hospital smile "我不行的……我真的唱不好……"

    "主唱。"
    "在舞台中央发出声音。"
    "像是发现了什么不得了的事情一样，爱音突然凑近过来，上下打量着我。"

    #音乐换成：test/game/audio/bgm/bgm_joyful.ogg

    anon hospital smile "喂，高松同学。"
    anon hospital smile "你今天气色真的比前两天好多了诶！"
    anon hospital smile "脸上都有血色了，刚才说话声音也比昨天大了一点点！"
    anon hospital excited "你看你，草莓牛奶都快喝完大半瓶了！"

    tomori hospital expressionless "……有吗？"

    anon hospital confident "有啊！绝对有！"

    "她双手叉腰，在床前转了个圈。"

    anon hospital smile "我说啊，你总是应该下床走走的。"

    tomori hospital expressionless "散、散步？"
    tomori hospital expressionless "可是……护士说还要静养……"
    tomori hospital expressionless "我站不太稳。"
    tomori hospital expressionless "脚底下……没有力气。"

    "爱音掀开我的被角，把塑料拖鞋踢到床沿下面。"

    anon hospital smile "怕什么！有我扶着你呢！"
    anon hospital smile "来，把脚放下来！"

    "脑子还是晕乎乎的，但起码能自己站起来了。"
    "我从床沿撑起来，借着她的支撑直起膝盖——"

    tomori hospital expressionless "……唔。"

    "算了。"
    "还是站不稳。"

    anon hospital smile "哇——哇……！"
    anon hospital smile "小心点！"
    anon hospital smile "慢点起……一、二、三，起！"

    "在我摔到地上前，她接住了我。"
    "她把我的左手臂搭在她自己的肩膀上，另一只手揽住我的腰。"

    "……我真不想承认，但她是正确的。"
    "有人扶着确实很有帮助。"
    "当我的双脚重新踩在坚硬的地板上时，整个世界的分量好像一下子全都压了回来。"
    "几天前，我站在天台边缘任由身体向深渊坠落；"
    "爱音的出现，是不是因为世界需要阻止我，好去成就什么更重要的事情呢？"
    "还是说，是因为我潜意识里渴望着什么东西——任何东西——来阻止我？"
    "而且，我其实并不在乎伦敦的红茶到底是什么滋味，但我拼命假装我在乎，我顺着她的话点头，想问她什么时候能带我去看大本钟。"
    "因为我也在做着同样的事情——我正拼尽全力，想要让她觉得我是一个可以交谈的朋友。"
    "这真是一件让人脸红的事情。"

    anon hospital smile "呼……高松同学，你看着瘦瘦小小的，怎么骨头还挺沉的嘛！"
    anon hospital smile "站稳了没有？"

    tomori hospital tears "……对不起……压疼你了吧？"

    "她没好气地敲了一下我的脑门。"

    anon hospital smile "你没别要总是道歉的。"

    tomori hospital smile "……好。"

    anon hospital smile "嘘……小声点！"
    anon hospital smile "护士站就在前面转角，要是被护士长看到我们私自出来溜达，肯定又要被抓去写检讨了！"

    tomori hospital expressionless "……检讨？"

    anon hospital smile "对啊！昨天我被她训了半个小时，还要我保证不在走廊里大声喧哗！"

    "看着她小心翼翼踮着脚尖走路的滑稽模样，我轻声开口。"

    tomori hospital expressionless "……爱音很像小偷。"

    "她差点脚下一滑，瞪着我。"

    anon hospital smile "哪有这样的小偷啊！"

    tomori hospital expressionless "阿德利企鹅。"

    anon hospital smile "我知道了，你说过的！喜欢偷石头。"

    tomori hospital expressionless "诶？原来爱音能记住的吗？"

    "爱音翻了个白眼。"

    stop music 

    # 两人并肩走在走廊
    scene bg hospital_corridor with dissolve
    play sound sfx_footsteps

    "我们这样走过了二十米长的走廊。"
    "终于挪到了走廊尽头的那扇大窗户前。"

    #配合失焦重新聚焦的感觉，用音乐bgm_night_lily。

    "好了。"
    "视野变清晰了一些。"
    "窗外是秋日午后淡金色的天空。"
    "阳光透过玻璃照在我的脸上，暖洋洋的。"
    "窗缝里漏进来的微风吹动着我的额发，带着室外干爽的气息。"
    "我双手扶着窗台，低头看着医院外面的街道。"

    tomori hospital expressionless "……嗯。"

    "从五楼往下看。"
    "我能看清人行道了，还有建筑物、天空和灯光。"
    "楼下的马路上，汽车慢慢移动着。"
    "穿着制服的初中生走过人行道，路边的银杏树叶子已经开始泛出金黄色。"
    "那是活着的世界。"
    "周围的一切都很友善。一切都很美。"
    "真好。"
    "这些都是值得一看、值得一想的美好事物。"

    "爱音顺着我的视线看下去，忽然指着远处的一栋红砖大楼。"

    anon hospital smile "喂，高松同学，你看那边！"
    anon hospital smile "那栋楼是不是羽丘的校舍啊？"

    tomori hospital expressionless "……不是。"
    tomori hospital expressionless "那是图书馆。"
    tomori hospital expressionless "羽丘在更往右边的坡道上面。"

    anon hospital smile "切，长得真像。"
    anon hospital smile "等我们出院了，一起去羽丘上学吧！"

    tomori hospital expressionless "……爱音，真的想和我一起组乐队吗？"

    anon hospital smile "当然是真的啦！"

    "她伸出小拇指，递到我面前。"

    anon hospital excited "来！拉钩！"

    "看着她白皙的小拇指，我迟疑了一下，慢慢伸出自己的小指，轻轻勾住了她的手指。"

    tomori hospital expressionless "……拉钩。"

    "她用力摇了摇我们勾在一起的手指。"
    "走廊另一头突然传来了护士长严厉的喊声。"

    play sound sfx_footsteps
    show nurse gentle at right_standee with dissolve
    nurse_head "{size=+2}喂！那边的两个病号！{/size}" with shake_h
    nurse_head "千早同学！高松同学！你们两个怎么跑到窗户那去了？！"
    nurse_head "不是说了高松同学不能剧烈运动吗？！快回病房！"

    "爱音吓得缩了缩脖子，飞快地拉住我的手。"
    "我被她拉着手，拖鞋在地上啪嗒啪嗒地响着。"

    anon hospital confident "我明天一定到您的宿舍！"
    anon hospital smile "哦，对不起，我已经是在提要求了……"

    hide nurse
    hide anon
    with dissolve

    "我点了点头。"
    "对，她是性急了点，确实几乎是在提要求……"
    "不过，我也不能告诉她，事情是这样的，明天她不能不到这里来。"
    "我的实际生活很少很少，像现在这样的时刻，我认为是罕见的，几乎是没有的。"
    "因此我不能不让这些时刻在我的幻梦中重现。"
    play sound sfx_strike
    "{b}我会整夜、整个星期都想您，成年成月地想您。这种思念不会因为时间流逝而减弱分毫！{/b}" with shake_h
    "所以，明天您一定要到这里来，我会感到无比的幸福。"
    "这个地方对我来说，实在太可爱了。"

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    scene black with slow_dissolve

    $ persistent.cleared_chapter_4 = True
    jump ch05_notebook
