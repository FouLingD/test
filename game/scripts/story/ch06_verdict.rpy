## ch06_verdict.rpy - 事件 13+14：临近的体检日与七天死刑宣告
## 对应剧本：出院审判、七天约定、清晨五点的逃跑计划、活下去的执念
## 包含完整原案 61 个文本块、共 164 句对白与旁白，100% 完整保留无任何删节。



####### 这一章你写吧，我懒得检查了 
label ch06_verdict:
    $ current_chapter = 6

    # 体检日病房，粉色凭条与七天宣判
    scene bg hospital_room with fade
    play bgs bgs_hospital fadein 2.0 loop
    play music bgm_gloomy fadein 2.0 loop

    play music bgm_routine fadein 2.0 fadeout 2.0 loop

    "第二天。"
    "我做完超声波复查回到病房，床头柜上放着一张粉色取报告凭条："
    "{font=fonts/ChillHuoSong_F_Bold.otf}【高松灯，今日16:30，主治医师诊室】{/font}。"
    "正当我盯着纸片发慌时，门被一把推开了。"
    "康复就意味着出院，出院就意味着必须重新走回大街上，回到父母叹气的视线里，回到羽丘空荡荡的储物柜前。"
    "所有人都觉得康复是一件好事。"
    "可我并不，我觉得那像是一场审判。"
    "只要你还能走路，你就得去扮演合格的女儿、合格的学生、合格的同龄人。"
    "你再也没有借口躺在床上发呆了。"
    "我想说些傻话，连着几小时唱歌，或者只是几小时在星空底下什么也不做。"
    "我是多么需要快乐！可惜没有人懂得这样的道理。"
    "活着就是这样一件事，不管你多想停下来，细胞还是会自顾自地分裂。"
    "它一点也不在乎你有多不想再当一个人。"

    # 爱音夺过粉色凭条
    play sound sfx_door_slide
    play music bgm_anon_theme fadein 1.5 loop
    show anon hospital smile at center_standee with dissolve

    anon hospital smile "哈喽！{w=0.4}高松同学，你干嘛又缩在床角盯着那张小粉纸发呆啊？"

    tomori hospital expressionless "下午……要拿最终评估单……"

    "爱音大大咧咧地坐在我床边，伸手戳了戳我紧紧皱着的额头。"
    "她两只眼睛亮晶晶的，兴奋地在半空中比划起各种手势。"

    anon hospital smile "你想想看，只要后天顺利拿到出院通知，我们能做的事情多得数不清呢！"

    tomori hospital expressionless "……出院以后？"
    tomori hospital expressionless "听起来……像做梦一样。"

    anon hospital excited "才不是做梦呢！只要出院就全都能实现！"
    anon hospital smile "所以这张报告单我替你去拿！"

    "爱音不由分说地从我手心里抽走那张粉色凭条。"

    voice "audio/voice/vo_anon_06_01.ogg"
    anon hospital excited "四点半准时等我凯旋归来！"

    voice "audio/voice/vo_tomori_06_01.ogg"
    tomori hospital expressionless "……嗯，我等你。"

    hide anon with dissolve

    "关于疼痛，我们经常将它当作唯一的真实。"
    "或者至少是最真实的。"
    "它来临之时，先于它的一切，它周围的一切，甚至在它面前的一切，都成为瞬间和错觉。"
    "走廊广播里说，今天是某个纪念日。反复讲了无数次，听得我索性用被子蒙住耳朵。"
    "一切被改变。一切被改变。"
    "那么，变的是什么？"
    "跌落揭示了什么？"
    "它为谁而来？"
    "书上写道："
    "“让我悲伤的是，悲伤不能教会我任何东西。”"
    "“我们仅被给予心脏所能承受的分量”"
    "“摔不死你的让你更坚强”"
    "“痛楚为我们提供最需要学会的功课”，"
    "诸如此类的话语让我愤怒。确实，医生难以设置一堂要求人们成为骨折者的修炼课。"
    "我忙于追问，在这个被撞坏的身体里，什么是可以忍受的日子，我如何与它一同撑下去。"
    "作为自己的见证者，我可以证明这其中没有道理，没有功课。"
    "但我能说出这样一句话：看着爱音，与她一同坐着，听她说话，与她一同掉眼泪，碰触她，与她交谈，我看到了某种纯净的核心。"
    "我无法告诉你它究竟是什么样的，但我能说我曾看见。"
    "同样，看见它让我产生依恋。"
    "尽管我无法描述我开始依赖的究竟是什么。"
    "当我为这个活页本收集那些词句时——收进书包、铁盒、日记、脑海——我想要写出一本巨大的歌词，关于西瓜虫、关于那个我跌落下去的夏季、沉在水底的石头的简明清单。"
    "然而，我做不到。"
    "当我现在摆弄这些旧纸页之时，最让我吃惊的是它们的贫乏，一种与我的执念成反比的贫乏。"
    "我以为我收集的碎石足以堆成一座高山。"
    "而今看来，我只是捡到乐队早已开场又散场之后散落在地面的几片细碎亮片；"
    "舞台背景早已被拆空。"
    "也许本该如此。关于这些句子的简短，我十分抱歉；可是，我还能写出什么？"
    "纵使你像挤柠檬一样地压我，也不能再多挤出什么了。"
    "那个受伤的同伴现在能够跑出病房，让我即时知晓外面的变化——这类变化总是很多。"
    "“我们的人生能够改变，会改变。”"
    "她大声宣称——确实正在改变，并且以吵闹的方式。然而，在这些话语的背后，我依然清楚自己承受的肉体，为弄丢的一切所感到的空洞，那是一个无底洞。"
    "“如果不写下这些摔碎的困难，我怕我会美化这不堪忍受的现实。”"
    "所以，在这里，我用铅笔直白地写下，我继续忍受这份痛。"
    "我把这些字句写在发黄的纸张上，以便记住所有声响，而不只是某些声响，消散在风里。"

    # 傍晚四点四十五分复查归来
    stop music fadeout 1.5
    scene bg hospital_corridor with dissolve
    play sound sfx_footsteps
    scene bg hospital_room with dissolve
    play sound sfx_door_slide
    play music bgm_dialogue_warm fadein 2.0 loop

    "下午四点四十五分。"
    "挂钟走过了约定的时间。门被用力推开了。"
    "千早爱音站在门框前，额前的碎发全被汗水打湿。"
    "她手里抓着撕开的牛皮纸袋，眼泪正顺着下巴往下掉。"
    show anon hospital tears at center_standee with dissolve

    tomori hospital expressionless "爱音……报告拿到了吗？"

    anon hospital smile "……"

    "她反手把门锁死，抱着变形的纸袋走到床前。"

    tomori hospital expressionless "是我……还不能出院吗？"

    anon hospital smile "不是出院的事情。"

    tomori hospital smile "那是骨头没有长好？"

    anon hospital smile "医生说，掉下来的时候，主动脉和心壁受到了损伤。现在的平稳只是药物撑出来的。"

    tomori hospital expressionless "……损伤？"

    anon hospital smile "最多只能再维持一百六十八个小时。"

    tomori hospital expressionless "……"

    anon hospital smile "高松灯……你只剩下最后七天了。"


    play music bgm_gloomy fadein 2.0 fadeout 1.5 loop

    "是时候做点什么了。"
    "不能一边待着什么也不做。或许可以写点什么。"
    "沉默，之后。 怎么做才能再多活一会儿，再活久一点。"
    "就这样。"
    "现在我不再是我了。而是某个我不再认识的人。"
    "沉默，之后。 你现在可以敞开心扉了。"
    "或许是我。为了让生活更甜美？"
    "谁也不知道。应该努力活着。"
    "不能投入死神的怀抱。"
    "就这样。"
    "这就是我要说的全部。"

    tomori hospital expressionless "一百六十八个小时……七天。"

    "我想躲开这一切。"
    "快来把我放在某个地方。"
    "病房里只有墙上挂钟的声音。"
    "七天。在学校里是一周的时间。"
    "黑胶唱片放两百遍，七天就结束了。"

    anon hospital smile "对不起……灯，对不起……我本来不该当面告诉你的。"
    anon hospital smile "可是我做不到看着你被蒙在鼓里……在这张床上等到最后一秒。"

    "爱音把脸埋在手心里。"
    "我看着她。"
    "胸口原本沉重的地方，忽然变得很空。"

    tomori hospital expressionless "原来……只有七天了。"

    "十六年里，我一直在向所有人道歉。"
    "向叹气的父母道歉，向觉得我怪异的老师道歉，向在雨里解散的乐队道歉。"
    "我每天醒来，都在为了自己不能成为一个正常人类而难过。"
    "但如果只剩下一百六十八个小时。"
    "这个世界就再也没有理由要求我去变好了。"
    "再也没有人会逼我回到教室，也没有人会对我露出失望的神情。"
    "我拿到了一张可以提前离场的票。"

    tomori hospital tears "爱音……不用说对不起的。"
    tomori hospital smile "谢谢你把这个消息带给我。"

    anon hospital smile "……为什么要谢我啊。"

    tomori hospital smile "因为……已经没有力气再去变好了。"

    anon hospital smile "……什么？"

    tomori hospital pensive "不用再回学校了。"
    tomori hospital pensive "也不用再试着……去当一个合格的人了。"
    tomori hospital expressionless "躺在这里就可以。"

    anon hospital smile "……高松灯。"

    tomori hospital smile "我一直……做不好那些事。"
    tomori hospital pensive "现在终于不用做了。"

    anon hospital smile "笨蛋！大笨蛋！谁要你认错谁要你合格了啊！"

    "爱音胡乱用毛衣袖口抹掉脸上的眼泪。"
    "我想躲开这一切。"
    "快来把我放在某个地方。"
    "下午，晚些时候。"
    "我一点也不想再坚持了。"
    "我认为谁也不能说出这种恐惧。还不能。"
    "我想叫住你，对你说，把你的嘴凑过来。"
    "快来，好走得更快。"

    anon hospital smile "只有七天了！"

    tomori hospital expressionless "……嗯，我知道。"

    "快。 就这样。"
    "我不会再做任何事来限制或扩展你的生活。"

    anon hospital tears "你难道真的要在这里乖乖数着墙缝等死吗？！"

    tomori hospital expressionless "我不想留在这里。"
    tomori hospital expressionless "我想在七天结束之前……做一件事。"
    tomori hospital expressionless "……唯一的一件事。"

    "十六年里，我一直在向所有人道歉。"
    "向叹气的父母道歉，向觉得我怪异的老师道歉，向在雨里解散的乐队道歉。"
    "我每天醒来，都在为了自己不能成为一个正常人类而难过。"
    "但如果只剩下一百六十八个小时。"
    "这个世界就再也没有理由要求我去变好了。"
    "再也没有人会逼我回到教室，也没有人会对我露出失望的神情。"

    tomori hospital expressionless "我想把没有写完的那首歌……完整地唱给爱音听。"

    anon hospital smile "……歌？那本写满歌词的日记本？"

    tomori hospital expressionless "嗯。"

    anon hospital smile "……只唱给我听吗？"

    tomori hospital expressionless "只唱给爱音一个人听。"

    anon hospital smile "好！"

    tomori hospital smile "……一言为定。"

    # 清晨五点的出逃之誓
    play music bgm_soaring fadein 2.0 loop

    anon hospital excited "明天清晨五点，护士交接班的时候，我们就从这里逃跑！"

    tomori hospital confused "……逃跑？"

    "不能像你一样，这是让我遗憾的地方。"
    "不过，既然爱音都说没关系了，那在这个世界上，就是真的再也没有任何关系了。"
    "我们还有那么漫长的几天，我们还有太多太多可以并肩去做的事情。"
    "我们要扯掉刺痛的手腕塑料环，迎着破晓的晨光坐上第一班脱离既定轨道的早班电车。"
    "我们要逃向狂风呼啸的遥远海岸线，把日记本里写满的歌词一字一句唱给翻滚的浪花。"
    "我们还要去涉谷挑选最漂亮的粉色吉他拨片。去吃甜得发腻的草莓大芭菲。"
    "神明在最后收回了对我的全部审判，并把千早爱音送到了我空无一人的病床前。"
    "在这个行将消逝的残破世界里，爱音会在最后的日子里一分一秒都坚定地陪在我的身边。"
    "哪怕只是握紧我冰凉的手指，只是和我分享毛衣口袋里的微温。"
    "我在这荒芜的人世间，再也找不到比这更加浩大、更加纯粹的至高幸福了。"
    "谢谢你。真的无尽感谢。"

    anon hospital tears "把手环扯掉，把难看的病号服扔了，坐上最早一班电车，去哪里都可以！"

    tomori hospital expressionless "去……能看到海的地方。"

    anon hospital smile "好！"

    tomori hospital smile "{cps=22}……一辈子都不放手。{/cps}"

    play sound sfx_strike
    anon hospital confident "{size=+4}{b}绝对不放手！{/b}{/size}" with shake_h

    # 尾声：高松灯的两个请求与清晨出逃之约
    play music bgm_music_box fadein 2.5 loop

    tomori hospital expressionless "以及，爱音，我对你有两个请求。"

    anon hospital gentle "你说。别说两个，一百个我也答应你。"

    tomori hospital expressionless "第一，帮我找一点能提神的药，或者苦一点的黑咖啡，怎么都可以……只要能让我一直醒着，只要能让我利用好我生命中最后的每一分钟就行。"
    tomori hospital expressionless "我现在好困，可我不想再去睡觉了，我还有太多太多的事情要做。"

    anon hospital gentle "我明白。我不会让你睡过去的，我会一直在你耳边说话。"
    anon hospital gentle "那……第二个请求呢？"

    tomori hospital expressionless "就像你刚才说的那样——带我离开这里，我要死在外面。"
    tomori hospital smile "我需要再去一次那座人行天桥，再去一次阳光城的水族馆。以前我总是低着头匆匆走过那里，可却从来没有产生过要贴在玻璃上、从近处仔细看看那些水母和鱼群的好奇心。"

    anon hospital smile "好，我们明天一早就去！"

    tomori hospital expressionless "我还想不穿厚外套、不打伞走在深夜的冷风里，去体验一下特别寒冷的滋味。从前因为害怕感冒、害怕在练习室里发不出声音，我总是把自己裹得严严实实的。"
    tomori hospital smile "爱音，总而言之，我需要仰起脸去淋淋雨，需要向那些曾经对我伸出手的女孩们报以微笑，需要去你邀请我去的所有涉谷咖啡馆，去挑最漂亮的粉色吉他拨片。"

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    scene black with slow_dissolve

    $ persistent.cleared_chapter_6 = True
    jump ch07_escape
