

label ch01_awakening:
    $ current_chapter = 1
    window hide
    # 初始黑屏，暴雨声、心跳声与阴郁回忆音乐
    scene black with fade

    play psycho sfx_heartbeat volume 8 fadein 10 loop
    play music bgm_opening loop

    pause 4.5
    n_fs "其实，{w=1}自然界当中有感情的生物不止有人类一种。"
    show elephant at Transform(zoom=0.6,align=(0.5, 0.05)) with Dissolve(0.5)
    n_fs "大象会在死去的同伴白骨前伫立，{w=0.5}这是它们理解离去的方式。"
    hide elephant with Dissolve(0.8)
    pause 0.8
    n_fs "在太平洋某处，{w=0.5}曾经有一位失去幼崽的虎鲸母亲。{w=1}{nw}"
    show whale at Transform(zoom=0.7,align=(0, -0.05)) with Dissolve(0.5)
    n_fs "用额头顶着早已失去生机的孩子，{w=0.5}在汹涌冰冷的洋流里日夜不停地游曳上千公里。"
    n_fs "听说，{w=0.5}她一次又一次用脊背将不断下沉的冰冷躯体重新托出海面，{w=1}\n跨越了整整十七个昼夜。"
    hide whale with Dissolve(1)
    pause 1
    n_fs "以此类推，{w=0.5}在广袤的天地之间，{w=0.5}还有许许多多的生命和我们一样，{w=1}{nw}"
    n_fs "会为了无法挽回的失去而固执地抵抗遗忘。{w=999}\n……这真是很浪漫的事情啊。"
    n_fs "这样说来，{w=0.5}在这个庞大而井井有条的地方，{w=0.5}我们似乎也没有那么孤独。"
    n_fs "所以，{w=0.5}当你沉溺在痛苦、{w=0.5}执念{w=0.5}与深情当中，{w=1}不妨摸摸自己的心脏吧！"
    play bgs bgs_rain volume 0.3 fadein 2.0 loop 
    n_fs "想象一下，{w=1}那里流淌的血液是所有真实活过的灵魂共同经历过的。"
    n_fs "当你摸到自己脉搏的瞬间，{w=0.5}尽管……{w=0.2}尽管你可能穿着校服，{w=0.3}还是什么其他的——{w=0.5}{nw}"
    play sound sfx_impact
    pause 0.3
    n_fs "{b}你会听见海的声音！{/b}{w=1.5}\n那些仅仅存在于视野之外的灵魂，此刻正在你的身体中回响……"
    with shake_h
    n_fs "这或许是某种很取巧的，可以看海的方法吧！"
    n_fs "当然，{w=0.5}我其实并不赞同什么，生命是无价的之类的观点。"
    n_fs "大家都在给它贴金，{w=0.5}给生活贴金，{w=0.5}给爱贴金，{w=1}把它们写成诗，拍成电影。"
    n_fs "我讨厌那些被包装的盛大而无坚不摧的奇迹。{w=1}\n至少，那些烂片的票房算不到我的帐上。"
    n_fs "这个世界不由那些宏大的词句构成！"
    n_fs "那么……{w=0.5}它到底是怎么运转下去的呢？"
    n_fs "这个问题真是难倒了一大片哲学家啊。"
    n_fs "曾经我在读到一本图鉴的时候，上面说过，{font=fonts/ChillHuoSong_F_Bold.otf}“世界依靠社会规范、共同信念与相互依赖维持”{/font}。"
    n_fs "……这好像在没有解决上一个问题的同时，{w=0.5}又提出了好多悬而未决的新的概念。"
    n_fs "什么可以被称作是规范？{w=0.5}什么是共同信念？"
    n_fs "我还是没看懂，{w=0.5}但是至少我们可以推己及人——"
    n_fs "我会在无数个夜晚将自己折磨地翻来覆去，{w=0.5}排练着应该如何面对自己的过分敏感和迟钝。"
    n_fs "我可不想被这样刁难，{w=0.5}但总有人是想的，这会成为她们的共同信念吗？"
    n_fs "如果是真的，{w=0.5}是不是说明我又被别人抛下了？"
    n_fs "不过我也并不在乎。"
    n_fs "因为，{w=0.5}你其实是一颗特别奇怪的星星。"
    n_fs "归国转学生。{w=0.5}在年级里只占极少数，{w=0.5}在少数人里也是个异类。"
    n_fs "吉他弹得很一般，{w=0.5}平平无奇。"
    n_fs "可就算这样，{w=0.5}你还是比任何人都更努力地、{w=0.5}拼尽全力地想要发光。{w=1}\n……我觉得这点，真的超可爱。"
    n_fs "越想这些，{w=0.5}就越觉得不可思议。"
    n_fs "刚好在天台遇见，{w=0.5}刚好伸出了手，{w=0.5}刚好撞在一起组了乐队。"
    n_fs "或许会有人说这只是巧合，{w=0.5}但即使如此的话，这种巧合不也太经常出现了吗！"
    play sound sfx_strike
    n_fs "{b}假如偶然足够多，填满了所有的时间与空间，{w=0.5}那这种巧合怎么不能被视为是必然事件呢！{/b}" with shake_h
    n_fs "我可不信什么命中注定。{w=0.5}我没自大到！{w=0.5}以为你是为了拯救我才降临的，也不觉得你的努力只是为了博眼球。"
    n_fs "不过……{w=0.5}换个角度想呢？{w=1}女孩向往人群，{w=0.5}是因为按常理来说，我们以为认同来自外界。"
    n_fs "但如果这个女孩的心，{w=0.5}本身就是一整座空无一人的舞台呢？"
    n_fs "在她身后没有人为她鼓掌，{w=0.5}她只能一个人在上面拼尽全力，{w=0.5}撑起自己全部的体面。{w=1}\n她需要用自己的方式来解释这一切……"
    n_fs "然后在独自表演的过程中，{w=0.5}慢慢萌生出了想要被真正看见的心愿——{w=1}{nw}"
    n_fs "想被爱，想被认真注视。"
    n_fs "所以，{w=0.5}她才会不管不顾地把我也硬拽上这座舞台。"
    n_fs "唱得走调也没关系，{w=0.5}吉他弹得乱七八糟也没关系。"
    n_fs "因为她的世界，{w=0.5}从一开始就只有她自己啊！"
    play sound sfx_impact
    n_fs "{b}只要我们站在这里，{w=0.5}她就已经替我否定了所有的否定……{/b}{w=999}\n这难道不超有意思吗！" with shake_h
    n_fs "我几乎都要开心到掉眼泪了，{w=0.5}真的。"
    stop music fadeout 4
    stop psycho fadeout 4    
    stop bgs fadeout 4
    n_fs "…………"
    n_fs "……"

    pause 2
    
    stop music
    stop psycho
    stop bgs

    # 现实苏醒：白光骤闪，心跳仪与医护急救
    #（增加一个类似睁眼的效果，）

    scene expression Solid("#ffffff") with flash_white
    play sound sfx_iv_drip

    pause 1.5
    
    window auto
    nurse_a "{size=+4}医生！{w=999}3号床瞳孔出现对光反应了！{/size}{w=0.5}{nw}"
    window hide

    play sound sfx_ringing
    scene bg hospital_room at Transform(blur=10)
    show docto at Transform(blur=10) , left_standee
    with Dissolve(3.0)
    stop sound fadeout(4)

    window auto
    doctor "手电拿给我。"
    doctor "高松同学，{w=0.4}能听见我的声音吗？"
    scene bg hospital_room
    show docto at left_standee
    with Dissolve(1.0)
    
    play bgs bgs_hospital fadein 3 loop
    show doctor calm at left_standee with dissolve
    show nurse gentle at right_standee with dissolve

    tomori hospital expressionless "……"

    doctor "如果能听见，{w=0.4}试着眨一下眼睛。"

    tomori hospital expressionless "……"
    "我没有眨眼。"
    "很疼。"

    tomori hospital tears "{size=-2}{cps=15}咳……{w=0.4}咳咳！{/cps}{/size}"

    nurse_a "{size=+2}侧过头！{w=0.3}别呛着！{/size}"
    nurse_a "拿脱脂棉来。"

    "棉花擦过下巴。"

    nurse_b "我去叫门外的家属？"
    nurse_b "他们在走廊里守了一整夜了。"

    doctor "去吧，{w=0.3}一次只能进一个。"

    play sound sfx_door_slide
    "门被推开了一条缝。"

    nurse_b "高松先生？{w=0.3}高松太太？"
    nurse_b "病人醒了，{w=0.4}但情绪不太稳定。"

    mother "谢天谢地……{w=0.5}医生，真的太谢谢你们了！"

    father "给你们添麻烦了……"

    nurse_b "{size=+2}小声点，{w=0.3}这里是重症监护区。{/size}"

    play music bgm_gloomy

    "看起来他们真的打算在一个刚自杀完的病人床前扎堆开辩论会就是了。"
    "推车轮子的噪音、橡胶鞋底蹭地胶板的吱吱声、{w=0.4}还有走廊里没完没了的呼叫铃……"
    "虽然我跳楼之前确实没料到事情会演变成这么严肃又尴尬的局面，{w=0.5}但好歹让我安安静静待一会儿吧！"
    "退一万步讲，{w=0.4}我刚才只是在普通地睡个午觉，{w=0.4}你们这样不打招呼就猛地把人摇醒、{w=0.4}又是拿手电筒照瞳孔又是抽管子的，{w=0.5}未免也太不讲礼貌了吧？"
    "我还活着。{w=0.5}我当然会这样想。"
    "一切都会重新开始，{w=0.4}我会在这里呆上一段时间，直到医生认为我完全康复。"
    "我会再次出院，{w=0.4}再次看到东京都的大街小巷、它的广场、车站、在路上上学放学的学生。"
    "我会继续过着一种充满耻辱的生活。{w=0.5}那种对我而言，从来就不可捉摸的人类的生活。"

    tomori hospital expressionless "{size=-2}{cps=15}……唔……{/cps}{/size}"

    doctor "高松同学，{w=0.4}右手不要用力，针头会鼓包的。"

    "我看着这一切。"
    "医生在一旁煞有介事地下医嘱，{w=0.4}护士在交头接耳地窃窃私语，{w=0.4}父母在门口像犯了滔天大罪一样对着空气连环鞠躬道歉。"

    # 走廊护士交头接耳闲谈
    hide doctor
    hide nurse
    with dissolve
    play music bgm_gloomy fadein 2.0 loop
    nurse_a "现在的高中生到底在想什么啊……"

    nurse_b "没。{w=0.3}不知道。"

    nurse_a "真怪啊。"
    nurse_a "现在的小孩压力有这么大吗？"

    nurse_b "也许是呢。"

    nurse_a "你听说是因为什么吗？"

    nurse_b "没。"

    nurse_a "我听警车那边的人说，{w=0.4}好像是跟学校里搞乐队的同学闹翻了。"

    intern_doctor "乐队吗？"
    intern_doctor "那你觉得她现在躺在这里，{w=0.4}过两天会不会有同队的小姑娘抱成一团哭着跑来探视？"

    nurse_b "怎么可能。"

    nurse_c "现在她们不都这样。{w=0.4}表面上好好的，背地里谁知道想的会是什么呢。"

    nurse_a "而且因为刚好砸在自行车棚的塑料顶棚上缓冲了嘛。"
    nurse_a "听说连雨棚都被砸穿了一个大窟窿，{w=0.4}物业今天早晨还在找学校索赔呢。"

    nurse_b "{size=+2}小声点！{/size}"
    nurse_b "万一让家属听到又要投诉我们了。"

    play sound sfx_footsteps
    "走廊外的谈话声伴随着手推车轮子的吱呀声慢慢飘远。"

    "好无聊。"
    "他们的议论让我很不爽，{w=0.4}我也不知道为什么。"

    "倒也不是说他们在胡说八道。"
    "我本来和他们描述的情况大差不差。"
    "在学校里交不到朋友，{w=0.4}在乐队里发不出声音。"
    "我也没太把那些护士的闲话放在心上。"

    "而且，{w=0.4}如果真的一切正如他们所说，也不是十足的坏事。"

    "这意味着祥子她们现在同样觉得我恶心透顶了吧。"

    "但不管别人怎么说……"
    "也不管我心底有多么不堪，{w=0.4}乐队确实因为我而彻底粉碎了。"

    voice "audio/voice/vo_tomori_01_02.ogg"
    "她们要是从此再也不理我，{w=0.4}我一点也不会感到奇怪。"
    "毕竟……{w=0.5}我就是这样只会给别人添麻烦的人啊。"

    "……"

    "可是，{w=0.4}刚才那个年轻医生说的那些话……"
    "会有人抱着花哭着跑来医院看我吗？"

    nurse_b "哎，{w=0.3}刚才前台是不是有个戴贝雷帽的女生在张望？{w=0.4}是来找她的吗？"

    nurse_a "没看到，{w=0.3}大概率只是隔壁床的女生在散步就是了。"

    "我从来没敢往这方面想过。"
    "那种跌跌撞撞冲进病房、{w=0.4}握着我的手大哭大闹的画面……"
    "哇。"
    "这么一说，{w=0.4}那简直……"
    "为了不成器的笨拙主唱、在大雨中反抗全世界的摇滚少女们……"
    play sound sfx_strike
    "{b}禁忌的羁绊，{w=0.4}被暴雨冲刷的誓约！{/b}" with shake_h
    "{b}简直像漫画里的情节一样！{/b}"
    "如果有真的这种情节发生的话，{w=0.4}那么我现在在这里躺着这么长时间也不算浪费。"
    "她们会说没关系，{w=0.4}只不过我让她们很失望。"
    "她们会很快意识到，{w=0.4}没人愿意再把乐队组下去了。"
    "没有人会愿意读我的日记，看完我写的歌词。"
    "人们翻阅一通，然后将其塞到我的病历最后，{w=0.4}好像其主旨不过是，我是一个需加管控的多语症患者。"

    "但是另一方面，{w=0.4}我真的很……"
    "难过。"

    "我这么想很蠢也很贪婪。"
    "现实才不会有漫画里的奇迹。"
    "如果祥子、立希和爽世真的彻底不要我了……"
    "我就好像，{w=0.5}真的再也没有什么可以指望的了。"

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    scene black with slow_dissolve

    $ persistent.cleared_chapter_1 = True
    jump ch02_silence
