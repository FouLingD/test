
label ch02_silence:
    $ current_chapter = 2

    # 五楼单人病房，医院环境音与沉郁音乐
    scene bg hospital_room with fade
    play bgs bgs_hospital fadein 2.0 loop
    play music bgm_relaxed fadein 2.5 loop

    "从重症监护室转到单人病房，是在入院后的第三天。"
    "房间在五楼走廊最靠里的角落。"
    "门牌上插着一张白色的塑料卡片。"
    "我躺在铁架床上，心中对此却没有丝毫现实感。"
    "冷漠地旁观着这一切。"
    "好似这是别人的事情，好似在看着没有声音的电视画面。"

    show nurse gentle at center_standee with dissolve
    nurse "高松同学，早餐放桌上了哦。"
    nurse "今天有热牛奶、白米粥和煮南瓜。"

    tomori hospital expressionless "……"

    nurse "昨天的南瓜汤，一口都没动呢。"

    tomori hospital expressionless "{cps=20}……不饿。{/cps}"

    nurse "不饿也得吃一点。"

    "这是不是前两天议论过我那个医生，我已经没印象了。"
    "就像你刚睡醒，一定也会对刚发生的事情记忆不深刻吧？"
    "周围的人都在劝我活下去，医生向我解释各种药物的作用，护士用极其温柔的声音哄我进食。"
    "但是，他们根本就不明白。"
    "我并不是在同某个具体的人作对，我也不是在冲什么人发脾气，借此来缓和本来就不存在的女女情谊。"
    "如果要发脾气，感到委屈了，我多可以有其他方式来排解。"
    "灯管亮得晃眼，把我弄得昏昏沉沉的。"
    "我只想在这张病床上耗尽最后一丝力气。"
    "有时候我长时间感到空虚。我没有身份。"
    "一开始会让人感到害怕。后来会变成一种幸福。仿佛我说话的时候我已经不在了。"

    nurse "医生说你今天的血糖指标又降了，胃一直空着会出问题的。"
    nurse "哪怕喝两口牛奶呢？"

    tomori hospital pensive "{cps=20}……放着吧。{/cps}"

    nurse "为什么？"

    tomori hospital confused "没什么。"

    nurse "你妈妈早上在走廊里碰见我，一直问你肯不肯吃东西。"
    nurse "她说只要你肯吃一小勺，她就安心了。"

    tomori hospital expressionless "……"

    nurse "医生说了，下午要是再不吃，就只能给你下鼻饲管了。"

    tomori hospital tears "会很疼吗？"

    nurse "会有点难受。"

    nurse "所以，尽量自己吃两口吧。"
    hide nurse with dissolve

    # 走廊公共休息区
    scene bg hospital_corridor with dissolve
    play sound sfx_footsteps

    "这样看来，我或许需要感谢她的提醒。"
    "待她走后，我又把那碗早饭往窗边推了推。"
    "走廊里传来推车的轮子声。"
    "我从床上坐起来，踩着塑料拖鞋，慢慢走到门外。"
    "走廊尽头有一处小小的休息区。"
    "摆着几张蓝色的塑料排椅，还有一台挂在墙上的电视机。"
    "电视里正在重播上午的晨间剧。"
    "女演员的声音响亮，台词说得很快。"
    "有两个人坐在排椅上看电视。"
    "他们谁也没有说话。"
    "只是面无表情地盯着那个闪烁的屏幕。"
    "上面播放着早就失去观众的老套笑话。"

    grandpa "小姑娘，今天降温了啊。"

    tomori hospital expressionless "……嗯。"

    grandpa "这里的暖气总是不太热。"
    grandpa "习惯了就好。"

    tomori hospital smile "……好。"

    "对话就这么简短地结束了。"
    "我和他们一起坐在排椅上，看那个无聊的电视剧。"
    "剧情是女主角在面包店里打翻了面粉袋，所有人都在手忙脚乱地大笑。"
    "笑声在空旷冰凉的走廊里回荡着。"
    "没有其他事情可做，也没有其他地方可去。"
    "大家都在安静地耗费着时间。"
    "人的生病与住院，原来是这么平淡无奇的事情。"

    # 下午三点探视时间铃声
    play sound sfx_bell
    scene bg hospital_room with dissolve

    "下午三点整。"
    "探视时间的铃声响了。"
    "单调的电子蜂鸣，一声接着一声。"
    "我慢慢走回自己的病房，重新在铁架床上躺下。"
    "或许真的会有人前来探访我吧！"
    "比如，下午放学的铃声刚刚打响，走廊里全是一路小跑踩过木地板的脚步声。"
    "少女们把书包甩在肩头，连制服裙摆上的褶皱都来不及整理好。"
    "两个人，三个人，或者更多人。"
    "慌慌张张地推开鞋柜，换上外出的鞋子。"
    "穿过开满八重樱的坡道，穿过电车道口的红色警示杆，穿过放学路上喧闹的人潮。"
    "怀里紧紧抱着从街角花店买来的花束，塑料包装纸在风里哗啦啦地响。"
    "气喘吁吁地冲进医院大厅，撞开电梯门，一路数着门牌号找过来。"
    "“灯！我们来看你了！”"
    "大声地喊着我的名字，额头上全是一路跑来的细汗。"
    "有人可能会忍不住当场哭出来，有人可能会气急败坏地数落我，有人可能会笨手笨脚地把花瓶打翻。"
    "那种跌跌撞撞、热气腾腾的画面……"
    "哇。"
    "会有的吧？"
    "不会有的吧。"
    "光是脑子里冒出这种念头，我都觉得自己的脸颊在微微发烫。"
    "我怎么能配得上这样礼遇的招待？我以为我是谁呢？"
    "我是一个有病的人……我是一个心怀歹毒的人。"
    "我想我的肝脏有病。我想我应该落下了什么后遗症。"
    "但是我对自己的病一窍不通，甚至不清楚我到底患有什么病。"
    "我不去看病，也从来没有看过病，虽然我很尊重医学和医生，但这不能让我成为一个健康的人。"
    "如果她们来了，退一步讲，任何人来，或许只是为了更加健康！"
    "所以，无论她们是不是会来，她们都是出自善意，没有人是坏人。"
    "我为她们的善良感到格外幸福。"
    "我对这个世界的善意感到格外幸福。"
    play sound sfx_impact
    "{b}疼痛，那就让它疼好了，{w=0.4}让它疼得更厉害些吧！{/b}" with shake_h
    "我很早以前就这样生活了，大概二十年了。或许时间短点，总之这是我出生之后就在进行的事情。"

    # Crychic 队友探视：立希、爽世、睦登场
    play sound sfx_door_slide
    play music bgm_daily fadein 2.0 loop
    show soyo annoyed at left_standee with dissolve
    show taki serious at right_standee with dissolve

    taki "……灯。"

    "啊！他们来了。"

    soyo annoyed "打扰了……"

    tomori hospital smile "没事。{w=0.4}正好我也没干什么。"

    taki "……这房间还挺大。"
    taki "五楼只有这一间是单人的吧？"

    tomori hospital pensive "……不知道。"

    soyo annoyed "我们在楼下问了护士台，{w=0.3}护士说在最里面这间。"
    soyo annoyed "电梯今天好像在检修，{w=0.3}我们走楼梯上来的。"
    soyo annoyed "有点热呢，{w=0.3}外面的风停了。"

    tomori hospital expressionless "雨已经停了吗？"

    taki "今天早上就停了，{w=0.4}你该不会刚醒没多久吧？"

    "换做平常，我早就会说，我已经醒了很长时间了。或者，我才不会睡那么长时间。"
    "但是即使是解释的话，也不可能会冰释前嫌对吗？所以，还不如节省点力气，在床上多蜷缩一会。"

    soyo annoyed "灯不想说话，{w=0.4}让她安静一会吧。"

    "爽世在一旁帮腔。她注意到了只能打开一个窄缝的窗户。"

    soyo annoyed "啊，这窗户怎么只开这么一点？{w=0.4}房间里有点闷呢。"

    taki "医院为了安全吧。"
    taki "高层病房都这样。"

    soyo annoyed "这样啊……"
    soyo annoyed "那个，灯酱，这里有可以插花的花瓶吗？"

    tomori hospital expressionless "……没有花瓶。"

    taki "用矿泉水瓶剪开就行了吧。"
    taki "我去洗手间找找看有没有剪刀。"

    soyo annoyed "不用麻烦啦，我先把包装纸拆开一点，{w=0.3}就这么靠在柜子边上也挺好的。"
    soyo annoyed "花店的阿姨说百合花开得最久了。"
    soyo annoyed "本来立希想买向日葵的。"
    soyo annoyed "但是这个季节的向日葵不太新鲜，{w=0.3}叶子都发黑了。"

    taki "向日葵颜色亮一点。"

    soyo annoyed "病房里放太刺眼的颜色不太好吧？"
    soyo annoyed "白色的比较柔和，让人心情平静。"
    soyo annoyed "对吧，灯酱？"

    tomori hospital expressionless "……嗯。"

    taki "顺路在车站前面的便利店买的。"
    taki "两个装的草莓布丁。"
    taki "我记得你以前排练完了喜欢吃这个。"

    tomori hospital smile "谢谢。"

    taki "今天吃了没？"

    tomori hospital expressionless "吃过了。"

    "她发现了床头柜上纹丝未动的南瓜粥托盘。"

    taki concerned "真吃了？"

    tomori hospital expressionless "喝了水。"

    "她有些担心地瞪了我一眼。"

    tomori hospital pensive "你不知道，现在就算是喝水也要不少废我力气呢！"

    taki "等会儿饿了再吃。"

    soyo annoyed "学校那边的事，{w=0.3}灯完全不用担心哦。"

    "爽世依旧是令人感到安心。"

    soyo annoyed "今天早上我和立希去羽丘交了请假申请单。"
    soyo annoyed "班主任老师人很好，说手续都已经办妥了。"
    soyo annoyed "月之森那边这周也是自习周，所以我时间很多，随时都可以过来。"

    tomori hospital pensive "不用麻烦爽世特地跑过来的。"

    soyo annoyed "说什么傻话呢，怎么会是麻烦？"
    soyo annoyed "我们大家……{w=0.5}都很挂念你啊。"



    taki "……对了。"
    taki "月之森那边的乐器室，借用期延后了。"
    taki "老板说可以保留到下个月。"

    soyo annoyed "对呀，所以灯酱只要安心养病就好了。"
    soyo annoyed "等身体养好了，出院了，我们再去合练。"
    soyo annoyed "那首新曲子的贝斯部分，我已经把谱子背熟了呢。"



    tomori hospital expressionless "……新曲子？"

    soyo disdain "就是之前祥子写的那首啊。"
    soyo disdain "祥子今天虽然没来……但她也是因为家里有事脱不开身。"
    soyo annoyed "她心里一定也一直在为你加油的。"

    "我这才注意到祥子没有来。"

    stop music

    taki serious "……爽世，别说了。"

    soyo annoyed "……怎么了？我只是想让灯酱放宽心……"

    taki serious "祥子根本不会来了，你心里很清楚吧。"
    taki serious "别再提什么新曲子了。"

    soyo annoyed "立希……你非要在这种时候说这些吗？"
    soyo annoyed "这里是病房，灯酱才刚醒过来！"

    taki serious "……灯。"
    taki serious "我就问一句话。"
    taki serious "那天在天台上……到底是为什么？"

    tomori hospital expressionless "……"

    soyo disdain "{size=+2}椎名立希！{/size}" with shake_h
    soyo annoyed "医生说了绝对不能刺激病人。"

    stop sound

    show taki serious at left_standee with dissolve
    show soyo annoyed at right_standee with dissolve

    taki serious "……给。"

    tomori hospital surprised "……！"
    tomori hospital confused "这、这个是……"

    soyo annoyed "立希？！你把那个本子拿来干什么？！"

    taki serious "闭嘴，爽世！这是灯自己的东西！"
    taki serious "……不管你还唱不唱歌，也不管乐队以后怎么样。"
    taki serious "你写下来的东西，不准随随便便丢在那种地方让人踩。"
    taki serious "听见没有，灯？"

    tomori hospital smile "……嗯。"
    tomori hospital smile "谢谢你，立希。"

    play music bgm_painful_memory fadein 2.0 loop




    "房间里又安静下来了。"
    "急促的声音传进我的耳朵里，却全都被蒙上了一层棉花。"
    "像是在水底听岸上的人说话。我可以使用这个比喻吗？虽然我很少游泳……"
    "她们的难过是真的，眼泪是真的，手心里的汗水也是真的。至少，我不能证明她们此刻流露出来的感情是虚假的。"
    "没有必要总是这样揣测人吧，这个世界上有三个人正为了我而痛苦着。这听起来其实挺暖和的。"
    "虽然最近总是很少出太阳，可是怪就怪在，没有人能记录太阳本身的出勤率吧？"
    "进一步想，如果完全没有人管着我的话，我或许也不知道会跑到那里去躲上一天了。"
    "而且，虽然人们会抱怨”今天没有出太阳“，可是实际上，它就在那里，不增不减地散播着热量……"
    play sound sfx_strike
    "{b}当我们把地球仪转一圈就会发现，{w=0.4}其实只是我们自己躲到黑暗里面了！{w=0.4}这明明都是我们的选择。{/b}" with shake_h
    "{b}而我们就这样抱怨着太阳……{w=0.4}用责怪的语气表示着在意，这是一件多么幸福的事情啊！{/b}"

    mutsumi "……灯。"

    tomori hospital expressionless "……睦？"

    mutsumi "……对不起。"

    voice "audio/voice/vo_tomori_02_01.ogg"
    tomori hospital pensive "睦不用道歉的。"
    tomori hospital expressionless "跳下去是我自己的决定。"

    "护士推开门走进来，看了看屋里的气氛。"

    play sound sfx_bell
    hide mutsumi
    show nurse gentle at center_standee
    with dissolve
    nurse "探视时间到了哦。"
    nurse "病人需要休息了，同学们请先离开吧。"

    "爽世如释重负般松了口气，整理好表情，转过头看着我，挤出一个温柔的微笑。立希也从床边撤了半步，伸手要干什么但是卡在半空。"

    hide nurse with dissolve

    soyo annoyed "好的，护士小姐。"
    soyo annoyed "灯酱，那我们先回去了。"
    soyo annoyed "明天……或者后天，等你有精神了，我们再来看你。"
    soyo annoyed "布丁记得吃哦。"

    taki "……走了。"

    mutsumi "……再见。"

    tomori hospital expressionless "……再见。"

    # 探视结束，恢复冷清
    play sound sfx_door_close
    hide soyo
    hide taki
    with dissolve

    "向日葵、百合花、漫长的雨季。"
    "大家都在很努力地找着无关痛痒的话题。"
    "就像是在车站等车时偶遇的同班同学，不得不硬凑出几句话来填补空白。"
    "今天怎么样呢？昨天休息如何？   、"
    "然而，我并没有感到被安慰。就像任何人都不会对公交车站的公式对话产生感动。"
    "他们送来鲜花，送来水果，说着那些没什么意思的安慰话语。"
    "但我能从他们的眼睛里看到隐藏在关怀背后的恐惧与优越感。"
    "这样说或许有点阴暗，但我总感觉，请允许我这样说。"
    "比起怜悯，她们在庆幸倒霉的不是自己。"
    "她们庆幸跳下去的不是自己。"
    "“真可怜啊！”"
    "“为什么不早点和我们说呢？”"
    "同时又在为自己表现出的善良而暗自得意。"
    "好在医院离车站不会很远，她们不用在我身上浪费太多时间。"

    stop music

    # 护士站谈论503病房千早爱音
    scene bg hospital_corridor with dissolve
    show doctor calm at left_standee with dissolve
    show nurse gentle at right_standee with dissolve

    nurse "医生，隔壁503床的千早同学刚才又在护士站问东问西了。"
    nurse "她一直在打听自动贩卖机什么时候会补货草莓牛奶。"

    doctor "千早爱音？那个刚从外国转院回来的女高一生？"

    nurse "对，就是她。"

    "啊，是那个女生。我之前还听说过她几次，但是具体印象什么的，倒是一点没有。"
    "我想，或许我之前见过她？"

    nurse "明明是在医院，却表现得像是在度假一样。"
    nurse "刚才还缠着实习医生问顶楼的天台能不能上去晒太阳呢。"

    doctor "为什么呢？"

    nurse "说是病房里的光线太暗了，拍出来的自拍不好看。"

    play music bgm_anon_playful loop


    "这算是什么借口呢？"
    "啊，算了，管他呢。"
    "人总归是有各种各样奇怪的理由去做莫名其妙的事吧。"
    "就像我为了不再弄脏大家而跳下天台一样，对别人来说肯定也是完全无法理解的怪事。"
    "这么一想，为了自拍好看想去天台晒太阳，反而显得挺健康的？"
    "我开始嫉妒这种健康了，她的发色是粉色，我的草莓布丁也是粉色。"
    "我可不会对还没见过的人的头发产生食欲！"
    "呃……我需要说清这一点。"
    "如此，我爱上一个颜色——就眼前的状况来说，粉色——好似中了魔咒。"
    "诚然，但那又如何？"
    "也许你会说，这是一种自愿的错觉。"
    "你会说，每个粉色的物体都可能是一丛准备开放的蔷薇，一段只有间谍能够破译的密码，一个地图上的X。"
    "只是这幅地图太芜蔓，这片大陆太过离散。"
    play sound sfx_impact
    "{b}我会努力给你解释。{w=0.4}假如有一个巨大的草莓布丁在满医院寻找角度拍照，{w=0.4}换成谁都会觉得有意思吧！{/b}" with shake_h
    "草莓布丁……"
    "我承认，也许是我太孤单。"
    "可是这不能成为我的借口，即使这孤单会带来一阵一阵炽热的痛。"
    "如果足够热，足够漫长，这痛便会开始模拟或者激发。"
    "——随你喜欢哪个词——对奇迹的领悟。"
    "不过，我们且先将某个范例倒推一遍。"
    "那个夏天，退队的键盘手祥子在经历了一段漫长的沉默时光之后，回信队友爽世："
    "“过去数月十分骇人。"
    "幸运的是。”"
    "她在信中对爽世说，"
    "“我现在差不多死心了。”"

    doctor "那孩子啊，看着挺开朗的。"

    patrol_nurse "也是呢。不过有她在，五楼走廊总算没那么死气沉沉了。"
    patrol_nurse "刚才她还跟保洁阿姨聊了半天羽毛球比赛的事。"

    hide nurse with dissolve
    show doctor calm at center_standee with dissolve
    doctor "高松同学，你也该多向同龄人学学。"
    doctor "隔壁的千早同学年纪和你差不多大。"
    doctor "等过两天你能下床活动了，可以去走廊或者活动室坐坐，多和大家聊聊天。"

    tomori hospital expressionless "……嗯。"

    hide doctor with dissolve
    scene bg hospital_room with dissolve
    "医生带着护士离开了。"
    "门轻轻合上。"
    "千早爱音。"
    "我在心里默默念着这个名字。"
    "千。{w=0.4}早。{w=0.4}爱。{w=0.4}音。"
    "像是一串挂在走廊窗户边上的彩色风铃。"
    "粉色的头发，闪闪发亮的水晶，草莓牛奶，天台的自拍。"
    "在这个充满消毒水和病号服的五楼，怎么会有人像是在度假一样生活呢？"
    "真厉害呀。我不由得要对这个还没有见过面的人产生尊敬了……"
    "哦，应该也用不上这么重的词！应该是，好感。"
    "输液管里的葡萄糖一滴一滴落下来。"
    "我闭上眼睛，沉沉地睡了过去。"

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    scene black with slow_dissolve

    $ persistent.cleared_chapter_2 = True
    jump ch03_encounter
