## ch05_notebook.rpy - 事件 09+10+12：活动室里的残缺笔记本
## 对应剧本：活动室里的残破笔记本、未写完的歌词、就算看不到星星也想去的海边
## 包含完整原案 126 个文本块、共 282 句对白与旁白，100% 完整保留无任何删节。

label ch05_notebook:
    $ current_chapter = 5

    # 医院活动室，雨后黄昏
    scene bg music_room with fade
    play bgs bgs_hospital fadein 2.0 loop


    #音乐改成test/game/audio/bgm/bgm_autumn_leaves.mp3

    "我独自缩在最靠窗的折叠椅上，周围只有鱼缸里氧气泵吐出气泡的咕嘟声。"
    "十六年来，我习惯了把自己的呼吸压得极低极低，生怕惊扰了任何一个正常走过的人。"
    "可是在这个安静得甚至能听见尘埃落下的房间里，我竟然第一次没有感到恐慌。"
    "我很庆幸。我很幸运。"
    "因为我知道，那个总是踩着塑料拖鞋、大呼小叫的女孩，随时都会推开这扇门。"
    "我会看到她粉色的头发，我会看到她今天给我准备的礼物。"
    "哦对了，我应该拿些什么东西来着……"
    "我从病号服的口袋里掏出了那本活页本。"
    "之前，首先是一本精装日记本。"
    "这纸质真好，甚至还有个让我写名字的扉页。"
    "扉页之后的那一页被我用力撕掉了，留下参差不齐的毛边。"
    "我用铅笔在上面重重写下了那些句子。"
    "写下关于黑色的暴风雨，那场雨你可能永远也遭遇不上……"
    "这样想来，如果你永远都不能和我感同身受的话，那些文字还真的存在意义吗？"
    "或许你会讲，文学本身的存在就是意义了！就像我也会觉得爱音本身的存在就拥有十足的意义，不需要解释。"
    "我是不是跑题了？抱歉，我不是故意一直要把话题往她的方向拐的……"
    "主要问题是，我不知道自己为什么要写这些，我的痛苦显得如此微不足道，甚至有点娇气。"
    "我的文字如此无力，我的歌声依旧含糊不清。"
    "我自己写着开心嘛，也许我只是想给自己的残缺找一个可以安放的角落。"

    # 爱音推门找到活动室
    play sound sfx_door_slide
    play music "audio/bgm/bgm_banter_break.ogg" loop
    show anon hospital smile at center_standee with dissolve




    anon hospital smile "找到你啦，{w=0.4}高松同学！"

    "爱音手里攥着一盒插着吸管的橙汁，大步流星地走过来，在我对面的单人沙发上坐下。"
    "她把橙汁放在玻璃茶几上，探着身子看向我膝盖上的本子。"

    anon hospital smile "还在看这个本子啊？"
    anon hospital smile "借我再瞧瞧！"

    tomori hospital expressionless "……这是立希给我的。"
    tomori hospital expressionless "以前在乐队里的时候写歌用的。"

    anon hospital smile "立希？就是那个……"

    "我手在空中扑腾了几下！祈祷她能看懂吧。"

    anon hospital smile "看起来凶巴巴、生人勿近的那个？"

    tomori hospital smile "……立希其实人很好。"
    tomori hospital expressionless "以及那个本子写得很乱。要是看不懂也没关系的。"

    anon hospital smile "怎么会看不懂！"
    anon hospital excited "让我来看看未来的主唱大人到底写了什么传世名作！"
    anon hospital smile "咦？ 后面全都是空白的啊？"

    play music "audio/bgm/bgm_banter_boops.ogg" loop

    tomori hospital pensive "……嗯。 因为……写不出来了。"
    tomori hospital confused "那天从排练室跑出来以后，脑子里就空掉了。 无论怎么想，都觉得后面再也不会有任何新的东西了。"

    play music "audio/bgm/bgm_banter_chords.ogg" loop

    anon hospital smile "为什么会空掉啊？"
    anon hospital smile "之前的乐队解散了，再写新的不就好了吗？"

    stop music

    voice "audio/voice/vo_tomori_05_01.ogg"
    tomori hospital smile "写不出来的…… 我……我根本不是能好好传达心意的人。"
    tomori hospital smile "连普通的对话都做不好，只会把大家弄得痛苦……"
    tomori hospital confused "以前大家在一起演奏的时候，我以为自己终于抓住了什么。"
    tomori hospital expressionless "可是到最后，全都被我搞砸了。"

    play sound sfx_page_turn
    "爱音低头看着摊开的活页本。"
    "那些被划掉的横线、凌乱的标点、重重压在纸背上的笔锋。"

    anon hospital smile "拜托了，高松同学。"

    "爱音把本子抱在胸前，眼睛直直地看着我。"

    play music "audio/bgm/bgm_dreams.ogg" loop 

    anon hospital smile "我想和你两个人一起把最后一页写满。 我想和你两个人一起完成它。"



    tomori hospital expressionless "……哎？ 和我两个人……？"

    anon hospital smile "对啊！ 你看，这本本子后面还有这么多空白页，空着多浪费啊！"

    tomori hospital expressionless "但是……我只会写这些乱七八糟的碎片……"
    tomori hospital pensive "字也写得很乱……我也不会写吉他谱……"
    tomori hospital expressionless "唱歌的时候，声音也经常发抖……"

    anon hospital smile "那又有什么关系嘛！"

    anon hospital smile "喂，高松同学！"
    anon hospital smile "既然词都写得这么完整了，你平时肯定自己试着哼过旋律吧？"
    anon hospital smile "快！现在就唱一句给我听听！"

    tomori hospital expressionless "……欸？"
    tomori hospital expressionless "唱、唱出来……？"

    anon hospital smile "对啊！"
    anon hospital smile "反正活动室现在又没有别人，护士站离这里隔着大半个走廊呢！"
    anon hospital smile "就唱两句！如果不愿意的话，一句也可以的。"

    tomori hospital expressionless "不……不行的！"

    anon hospital smirk "好啦好啦，不唱就不唱嘛！"
    anon hospital smile "干嘛一副天都要塌下来的样子啊，我又没有逼你上刑场！"

    tomori hospital expressionless "……爱音……不生气吗？"

    anon hospital smile "我哪有那么小气！"
    anon hospital smile "给，把右边耳朵露出来！"

    "她不由分说地凑过来，把一边的白色耳塞轻轻塞进了我的右耳。"
    "耳塞上还带着她口袋里的余温。"
    "另一只耳塞被她自己戴在了左耳上。"
    "她按亮了手机屏幕，点开了一个绿色的音频软件。"

    # 播放白噪音音效
    play bgs bgs_white_noise fadein 1.5

    tomori hospital confused "……这是什么声音？"

    anon hospital smile "白噪音啦！"
    anon hospital smile "下雨天的声音，还有海浪拍在沙滩上的声音！"
    anon hospital excited "我在英国失眠的时候……咳，我是说，我在伦敦写作业的时候，最喜欢听这个了！"
    anon hospital smile "戴上耳机，外面的嘈杂声就全都不见了，很神奇吧？"

    tomori hospital expressionless "……真的，听不见了。"

    anon hospital smile "对吧！"
    anon hospital smile "喂，高松同学，要不要去个更好的地方？"

    tomori hospital smile "更好的地方……？"

    anon hospital smirk "秘密基地！ 跟我来就是了！"

    "综合医院六楼通往天台的消防铁门前。"
    "爱音手里攥着一根不知道从哪里捡来的细发卡，在门锁孔里来回拨弄着。"

    # 细发卡撬锁与重型铁门开启
    play sound sfx_lock_pick
    $ renpy.pause(0.6, hard=False)
    play sound sfx_metal_door_open
    stop bgs fadeout 0.8
    play bgs bgs_rooftop_wind fadein 1.5

    play music bgm_spelunking fadein 2.0 loop


    anon hospital smile "搞定！我就说这扇门的锁早就生锈松动了！"

    anon hospital smile "快上来呀，高松同学！这里的视野超级棒的！"

    tomori hospital confused "……天台。"

    "爱音踩着塑料拖鞋快步跑到了天台的铁丝防护网前，回过头朝我招手。"


    "闪闪发光。"
    "我现在大概明白爱音为什么执着于站在舞台最中间了，那不仅是虚荣，也是像我们这样的人唯一得以安身的地方。"
    "的确，有的人只有在远离人群的高处才觉得自如。"
    "在日常细节上，她都渴望登高望远：喜欢开阔的天台而不喜欢幽闭的单人病房，喜欢刺目的聚光灯而不喜欢角落里的阴影。"
    "讨厌逼仄的通道、沉闷的地下室以及深不见底的泥沼。"
    "她是吉他手，需要空间，若能站在四楼天台的铁丝网旁，远眺被落日染成金红色的街景，呼吸才会变得酣畅起来。"
    "尤其是当我们并肩站立在芸芸众生可望而不可即的高处，俯瞰着街道上蝼蚁般来去匆匆的人群，一种得救的安宁便在心头升起。"
    "所有的誓言与奇迹，似乎都只有在耀眼的高处才能被点燃。"
    "我们之所以拼命想要爬上最高峰，大声宣告着要组建轰动全校的乐队，不过是为了站得足够高，好让底下的人再也无法轻易审判我们的残缺。"
    "对有些人来说，星空不可知是命运将我们与当下缝合的方式。"
    "对另一些人来说，这是惩罚的标记，是我们在此的整个存在最好被理解为一个缺陷或错误的确凿证据。"
    "对我来说，两者皆不是。这只是我们存在的方式。"
    "这场坠落是幸或不幸，大概更隶属于心境的问题，而不是其他问题。"
    "这样想就一切都清晰明了。"
    "你得站在那里，别为这个事实过于烦恼。"

    anon hospital smile "别愣在门口吹冷风啦！快过来！"

    tomori hospital expressionless "……铁丝网很薄。"

    "爱音回到我身边，拉着我挪到了那堵绿色的菱形防护网前。"

    anon hospital confident "你看！这里有这么高、这么结实的铁丝网挡着呢，绝对掉不下去的！"

    tomori hospital smile "……好高。"

    "爱音双手抓住铁丝网的网格，把脸贴在上面，两只眼睛倒映着天边燃烧的晚霞。"

    anon hospital smile "高才好啊！站在最高的地方，就能把所有讨厌的东西都踩在脚下了！"

    tomori hospital expressionless "……踩在脚下？"

    "爱音转过头看着我，风把她的刘海吹得凌乱不堪。"

    anon hospital smile "对啊！等我们出院了，组一个全新的乐队吧！"
    anon hospital smile "我要去买一把最耀眼的粉红色电吉他！"

    "爱音整个人趴在铁丝网上，对着下方辽阔的城市大声描绘着她的宏图伟业。"
    "风把她的话语吹得七零八落，但她依然喊得极其卖力。"

    anon hospital smile "我们要站在最华丽的舞台上，聚光灯啪的一下打在我们身上！"

    tomori hospital expressionless "……台下会有人听吗？"

    anon hospital smile "台下全都是为我们欢呼的观……呃……唔……！"

    stop music  

    tomori hospital expressionless "爱音？"
    tomori hospital tears "你怎么了？胃又开始疼了吗？"

    anon hospital smile "没、没事……呼……就是突然抽筋了一下……"

    tomori hospital expressionless "我们快回去吧！"

    anon hospital smile "不要！别去叫医生！"

    tomori hospital expressionless "可是爱音的脸色很差……"

    anon hospital smile "……其实……"

    tomori hospital expressionless "……爱音？"

    #这里用，音乐从刚才那里继续播放。

    anon hospital tears "切！才没哭呢！是天台的风太大了！"
    anon hospital smile "喂，高松同学！冲着下面大喊吧！"

    "爱音把两只手拢在嘴边，做成喇叭的形状，她深吸了一大口气，把胸腔里的冷空气全部压进喉咙里。"
    "下一秒，一声极其响亮、带着一点破音的大喊划破了高空。"

    anon hospital tears "伦敦的鬼天气去死吧————！虚荣心去死吧————！千早爱音才不会认输呢————！"

    tomori hospital expressionless "……！"

    anon hospital smile "来！轮到你了，高松同学！"

    play music bgm_work loop



    "几个月前在排练室里，我背后那声撕裂乐谱的绝望呼喊，顺着倾盆的雨水一直飘向了远方，在广漠的记忆里日夜折磨着我直到今天。"
    "我心里清楚，那声求救还会在走廊和病房的每一个角落等着我，只要我依然活着。"
    "可是站在这高高的天台上，俯瞰着脚下沉睡在暮色中的屋顶与街道，我忽然明白自己不能再永远躲在自责的深渊里了。"
    "晚风中回荡的难道不是自己内心深处压抑太久的呼救吗？它催促着我做点什么。"
    "是啊，做点什么，还趁现在有大把的时间。"
    "没有任何坚硬的物质把我们同其他人分隔开来。"
    "他们，他们不知道我们的存在。"
    "而我们，我们却可以觉察到他们的某些东西，听到他们全部的声音，看出他们的一些踪影。"
    "于是我探出身子，朝着铁丝网下方的城市大声吼叫出来——"

    tomori hospital expressionless "我想……成为人类————！我想和爱音组乐队————！"

    tomori hospital expressionless "糟糕……两点半了，护士长该查房了。"

    anon hospital smile "怕什么嘛！"

    "我有些慌乱地想要转身朝消防门走去。"
    "爱音却一把拉住了我的手腕，用力把我拽了回来。"

    tomori hospital expressionless "被抓到的话……会被关禁闭的。"

    anon hospital smile "回去又要被关在那个只能拉开十五厘米细缝的小房间里，多没劲啊！"

    "爱音拉着我，背靠着天台的水泥矮墙坐了下来。"
    "她把我的双手塞进她宽大的开衫口袋里，两个人紧紧挨在一起取暖。"

    tomori hospital confused "……那我们现在怎么办？"

    anon hospital smile "既然都逃上来了，不如就在这里看星星吧！"

    "爱音抬起头，手指指向渐渐暗下来的深蓝色天穹。"
    "晚霞已经彻底褪去，天边升起了第一颗明亮而清冽的暮星。"

    anon hospital smile "对啊！你看，第一颗星星已经出来了！"

    tomori hospital expressionless "……很亮。"

    "天色完全暗了下来，天空变成了一片深邃的深蓝色。"
    "铁丝网外面，城市的灯火和天空的星光连成了一片，天地之间亮着望不到边际的微光。"
    "重力在脚底下仿佛失去了分量，让人产生了一种只要再往前走一步就会飘向夜空的错觉。"
    "世界失去了景深，也失去了上下之分。"
    "我可以想象所有的灯光在漫长的注视中悄然融化、溢出轮廓。"
    "远方群山与地平线的边缘被白色的光晕蚀穿，就像我能伸手触碰到……或许只需要半步！"
    "对啊！但是，如果我再往前半步的话……不行，我要尽早打消这个念头。"
    "不能重蹈覆辙倒是次要的事情，更主要的是，在自己喜欢的人面前死掉也是太糟糕、太糟糕的事情了。"
    "对啊！就这样想。虽然，我完全不介意想象到她悲伤的画面。"
    "东京未必不比伦敦忧郁吧！但是坏消息是，我又没法看到这一切。"
    "我之前已经犯过这样的错误一次了，人总不能总是踏入同一条河流……除非她本身就喜欢蹚水！"
    "那么，爱音会是喜欢水的类型吗？我是很喜欢的啦，或许以后可以和她一起去的。"
    "但是眼前总有更重要的事情处理。她完全对这片天空一无所知！是啊，虽然我们都在同一片天空下，但是她好像和这片天空不太熟悉。"
    "对天空一无所知的女孩！"
    "她难道不会抬头看看天空吗？我们的头上一直挂着太阳和月亮，这是小孩子都知道的事情。"
    "有没有一种可能她从昨天才开始学习了解这个世界。喂。我完全无法拒绝这样的假设！"
    "这样想来真的是太可爱了。真的太可爱了。我的爱音。"

    anon hospital smile "到了，高松同学！"
    anon hospital smirk "你看！这里是整座医院视野最好的秘密基地！"
    anon hospital smile "从这里看过去，天空的星星是不是特别清楚？"
    anon hospital smile "感觉只要伸出手就能摸到一样对吧！"

    tomori hospital expressionless "……嗯。"

    "高远夜空中的无数光点，仿佛静静落在了我们单薄的肩膀上。"
    "我迟疑着抬起手臂，学着爱音的样子，慢慢朝着夜空伸开五指。"
    "哪怕踮起脚尖拼命伸手，也是不可能够得到那些遥远星辰的。"
    "伸出的指尖触碰到的只有初秋干燥微凉的晚风。"
    "但千早爱音依然仰着脸，一遍又一遍执拗地在虚空中虚握着手掌，试图把那些散落的光芒抓进掌心里。"

    anon hospital smile "喂，高松同学，你想要哪一颗星星？"
    anon hospital smile "要是让你选，你想要哪一颗？"

    tomori hospital expressionless "我……"
    tomori hospital expressionless "我想要那一颗。"
    tomori hospital expressionless "天顶附近，泛着白光、最亮的那一颗。"

    anon hospital smile "那一颗啊！"
    anon hospital smile "那我就要那条白白的、长长的带子！"

    tomori hospital confused "……为什么？"

    anon hospital smile "你不觉得那条白色的光带很像刚刚出炉的长条奶油面包吗？"

    tomori hospital expressionless "……那是银河。"
    tomori hospital expressionless "我第一次听见有人把银河说成奶油面包。"

    anon hospital surprised "哈？！原来那个叫银河啊！"
    anon hospital smile "有意见吗！"

    tomori hospital expressionless "……没有意见。"
    tomori hospital expressionless "刚才那一颗最亮的……是天琴座的织女星。"

    anon hospital smile "哇，高松同学你知道得真多啊！"
    anon hospital smile "那在它下面、同样亮晶晶的那一颗呢？"

    tomori hospital expressionless "那是天鹰座的牛郎星。"
    tomori hospital expressionless "左边稍微靠后一点的那一颗，是天鹅座的天津四。"
    tomori hospital expressionless "把这三颗连起来，在夜空里就成了一个三角形。"
    tomori hospital expressionless "叫作夏季大三角。"

    anon hospital smile "啊！真的连成三角形了！"

    "爱音抱着膝盖在长椅边坐了下来，托着下巴看着头顶的星空。"
    "她明明连最基础的星座名字都叫不上来，却对这片夜空表现出了一种近乎孩童般的热切与向往。"
    "她仰着头的时候，眼睛里倒映着细碎的星光，整个人看起来毫无防备。"
    "这大概就是千早爱音的本质。"
    "她不关心那些深奥的宇宙规律，她只是单纯地向往一切明亮、耀眼、能够被人群注视的事物。"
    "为了得到这份注视，她愿意把整个天空都装扮进自己的梦想里。"

    stop music

    anon hospital smile "真好啊，这里。"
    anon hospital surprised "怎么就没早点发现这个天台呢。"
    anon hospital smile "要是能一直这样坐在高处仰望星空就好了。"

    tomori hospital expressionless "……爱音很喜欢星空吗？"

    play music "audio/bgm/08 Kirk Osamayo - Spelunking.mp3" loop


    "黄昏退去，西边的晚霞原本还很明亮，但正渐渐变得暗淡，底下的街灯发着柔和的光亮。我和爱音并肩靠在天台的铁栏杆旁，远处的坡道和图书馆尽收眼底。"
    "在城市高楼的缝隙之间，可以瞥见地平线上泛起的薄暮。"
    "街道上行人稀少，夜市尚未喧闹起来，我们脚下踩着天台地面上残留的白日余温。"
    "有的人正进晚餐，而有的人准备休息。"
    "作息如此不同的两类人，就这样被马虎地分进同一个时区。"
    "天空渐渐布满繁星，若从一道微光望向另一道微光，便可瞥见它们在深蓝色的苍穹中悄然映入眼帘的模样。"
    "我们正享受着病房喧扰之后的宁静，这微凉的夜色，以及渐显开阔的城市轮廓。"
    "我很满足。"
    "真的。"
    "我看见成群的白鸽。这些可爱的小动物终于下决心回落地面，它们以厚实洁白的羽毛遮掩着屋顶和水面，向着家家户户的玻璃窗翻飞扑打。"
    "到处都是啊！但愿它们带来好消息。"
    "果真如此，那么所有的人，不仅是出类拔萃者，都将得救！"
    "大家有福同享，有难同当。"

    anon hospital smile "喜欢啊！"

    "我想我没有必要补充“我也是”了。于是耐心等着爱音说完。"

    anon hospital smile "因为不管你在下面过得有多狼狈，被别人怎样冷落……"
    anon hospital confident "只要抬起头，这片天上的星星都一直都在那里闪闪发光，从来不会改变。"
    anon hospital smile "在英国的时候，每当我一个人在公寓里难过得睡不着，就会推开窗户看天上的光点。"
    anon hospital excited "虽然伦敦老是下雨……但偶尔放晴的夜晚，看到这些星星，就会觉得世界上还有别的东西在陪着我。"
    anon hospital smile "所以，在我练琴累了的时候，我会抬头看星星。"
    anon hospital smile "我不懂那些天文学之类的事情！不过如果它们都愿意当我的观众的话……"
    anon hospital smile "不也是……我的福气吗！"

    "她轻声说着这些话，声音里少见地没有了平时的浮夸与张扬。"
    "铁丝网外面的夜空安静地悬挂在头顶。"
    "上亿年前发出的微弱光芒穿透了漫长的时间与空间，落在我们两个人的身上。"
    "天空确实没有改变。"
    "无论人世间经历了多少次破碎、解散与逃离，这片星空依然毫无改变地存在着。"

    anon hospital smile "决定了！"
    anon hospital smile "等我们出院以后，不仅要组乐队，还要一起去真正能看到满天星海的偏远海边！"
    anon hospital smile "到时候找一个最高的悬崖，一边弹吉他一边把所有的星星看个够！"
    anon hospital smile "高松同学，你得陪我一起去哦！"

    tomori hospital expressionless "……嗯。"
    tomori hospital expressionless "我和爱音一起去。"
    tomori hospital tears "对不起。"

    anon hospital smile "怎么了？"

    tomori hospital expressionless "之前没有认识你。"
    tomori hospital expressionless "我很抱歉。"

    anon hospital smile "说什么蠢话呢。"

    tomori hospital expressionless "我知道。"
    tomori hospital expressionless "可我还是很抱歉。"

    anon hospital smile "这不是你的错。"

    tomori hospital expressionless "如果那天我没有允许你打开门呢？"

    anon hospital smile "干嘛这样问。"

    tomori hospital expressionless "抱歉。"


    anon hospital smile "我会一直吵。"
    anon hospital smile "到你来把我拉回病房。我的或者你的。"

    tomori hospital pensive "不会的。我连站起来都很困难。"
    tomori hospital expressionless "我会一直躺在床上。"
    tomori hospital expressionless "看着天花板。"
    tomori hospital smile "等肋骨长好，然后再找一个地方跳下去。"

    anon hospital smile "高松同学。"

    tomori hospital expressionless "嗯。"

    anon hospital confident "现在不会了。"

    tomori hospital pensive "现在不会了。"

    anon hospital smile "真的会去海边吗？"

    tomori hospital expressionless "真的会去。"

    anon hospital smile "海边会很冷。"

    tomori hospital expressionless "我知道。"

    anon hospital smile "要是到了海边，{w=0.4}什么星星都看不到呢？"

    play sound sfx_impact
    "{b}就算看不到……{w=0.5}\n我也和爱音在一起。{/b}" with shake_h

    "铁丝网发出轻微的撞击声。风从楼顶吹过去。"
    "我们坐得很近，肩膀贴着肩膀。"
    "即使上面的光点隔着几亿年，我们谁也没有动。"
    
    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    scene black with slow_dissolve

    $ persistent.cleared_chapter_5 = True
    jump ch06_verdict
