## ch07_escape.rpy - 事件 15+16+17：清晨的出逃与脱轨的早班电车
## 对应剧本：五点出逃、风衣与条纹病号服、长途大巴解离、耳机与围巾、池袋电车换乘

label ch07_escape:
    $ current_chapter = 7

    # 1. 清晨五点病房醒来
    scene bg hospital_room with fade
    play bgs bgs_hospital fadein 2.0 loop


    "我整夜没有合眼。"
    "耳朵里反复回响着昨天下午千早爱音说出的那句话。"
    "‘医生说……你只剩最后七天了。’"
    "主治医生让我老老实实待在病房里，去选择一个能够安静闭上双眼的地方。"
    "但是，当我在清晨看到千早爱音蜷缩在陪护椅上熟睡的时候，我彻底明白了什么是我离开这个世界时想要看到的画面——"
    "千早爱音的那张脸。"
    "所以我决定不再消极等死了。"

    voice "audio/voice/vo_tomori_06_01.ogg"
    tomori hospital expressionless "……千早同学。"

    "陪护椅上的粉发少女睫毛动了动，慢慢睁开眼睛。"
    "她揉着眼睛，有些吃力地把脑袋从椅背上抬起来，神情发懵。"

    show anon hospital surprised at center_standee with dissolve

    anon hospital surprised "呜……嗯？{w=0.4}灯……？"
    anon hospital smile "怎么突然又叫回千早同学了，昨天不是叫爱音叫得挺顺口的嘛……"
    anon hospital surprised "现在才五点不到！这么早就走嘛？"

    "当你在深夜疲惫入睡的时候，我的胸口又隐隐作痛了一次，我真切地以为最后的死期已经到了。"
    "我借着晨光注视着你的面容，试图猜测出你隐瞒的所有委屈与孤单，并且准备平静地走向终点。"

    tomori hospital expressionless "现在就走吧。"

    anon hospital surprised "这就出发了？"

    "但是时间还在走动，我的心脏依然在胸膛里倔强地跳动着，也许是因为我心底还有未完成的愿望。"
    "千早爱音低下了头。你不要因为我的任性而感到为难。"
    "我不会对千早同学提出任何过分的要求，仅仅是要你允许我喜欢你，允许我再为你唱完整整一首歌，如果我的喉咙还能发出声音的话。"
    "作为交换，我只要求你答应我一件事：如果你听到医生说我就要死了，请你带我走出这所综合医院的高墙，去看看外面的树木和天空，去呼吸清晨新鲜的空气。"
    "千早爱音许久没有讲话。我以为她又回到了自己的犹豫中，不想如此早地面对外界。"
    "我望着医院围墙外边的晨光。"

    anon hospital gentle "如果你想离开这里，我就带你出去。"
    anon hospital smile "只是给我几分钟时间，让我去拿外套和钱包，然后我们两个人立刻就走。"

    tomori hospital expressionless "千早同学，我们在一起的时间不多了，这你是明白的。"

    "千早爱音没有回答。"
    "她迅速从椅背上抓起防风夹克，将充电线、钱包和围巾塞进大衣口袋里，快步走到了病床前。"
    play sound sfx_clothes_rustle
    "她把宽大的深色夹克罩在我单薄的条纹病号服外面，拉链唰的一声拉到领口。"

    stop bgs fadeout 1.5
    stop music fadeout 1.5
    play sound sfx_strike
    show anon windbreaker smile at center_standee with dissolve

    anon windbreaker smile "{size=+3}{b}高松灯，我们会一起去看海，要比在这间千篇一律的病房里度过的日日夜夜还要长久。{/b}{/size}" with shake_h
    anon windbreaker excited "我们走吧，逃兵就要做疯狂的事！"

    # 2. 逃出医院奔跑与站台
    scene bg hospital_corridor with dissolve
    play sound sfx_door_slide
    play sound sfx_running_corridor
    play music bgm_soaring fadein 2.0 loop

    "她抓紧了我的手腕。"
    "病房的门锁被轻轻拧开，我们在清晨五点不到空无一人的走廊里奔跑起来。"
    "没有回头看一眼那张空下来的病床。"

    scene bg bus_stop with dissolve
    "我们一路奔跑，穿过清冷无人的街道，赶到了早班车的站台前。"
    "清晨的寒气在呼吸间化作白雾。"
    "个子稍矮的那个女孩迟疑片刻，环顾站台，然后转过身来朝拉着她的粉发少女点头。"
    "明摆着，两人是同伴。"
    "两人都穿着大号风衣，一样的狼狈。"
    "爱音套着一件宽大的深色防风夹克，而这衣服使她的肩膀显得单薄，有些发抖。"
    "我自己呢，裹着条纹睡衣。"

    # 3. 登上长途大巴
    scene bg bus_interior with dissolve
    play bgs bgs_bus_ride fadein 2.0 loop
    "她们离巴士车门很近。转瞬之间夜色与她们相融又相隔。"
    "拉着行李箱的那个粉发少女，深色夹克，正走到底层车厢的正中央。"
    "高松灯紧跟着走上前去，往前挪了几步。"
    "她停在离爱音半步的地方。注视着车窗外的黑暗。"
    "灯从检票口紧挨着走过来，她朝千早爱音靠过去，在她背后停下来，像她一样喘息。"
    "车窗玻璃上映出了两人的倒影。"
    "这个女孩为什么拉着自己？她要去哪里？谁也没有问。"
    "灯注视着她。千早爱音没有回过头来，她看着前路，她等待着发车，像个赌徒一样，在昏黄车灯下。"
    "售票员朝她们走过来。灯发凉的手指抓住了千早爱音的风衣衣角。她没有说话。"
    "引擎声低吼着，又震动起来了。是一辆长途大巴，驶向海边。"
    "冷风穿过开启的单向车门，朝车厢吹来。"
    "大巴驶出了站台。爱音转过头看着高松灯。爱音伸出手来，她没有松开灯的手。她把手覆在灯发冷的手背上。"
    "车轮开始转动。灯坐在座位上，一动不动。窗外飞速倒退的街景从她的眼前滑过，像黑色的潮水一样。"

    show anon windbreaker smile at center_standee with dissolve

    anon windbreaker smile "呼……终于坐稳了。{w=0.4}车里真暖和。"

    tomori windbreaker expressionless "嗯。{w=0.4}很暖和。"

    anon windbreaker smile "其实我们也没有想好去哪里。"

    tomori windbreaker expressionless "没有想好。"

    anon windbreaker smile "路程很远的，是吧？"

    tomori windbreaker expressionless "很远。"

    anon windbreaker smile "以前，这里是道路的尽头。"

    tomori windbreaker expressionless "风的尽头。"

    anon windbreaker smile "风的尽头，对。夏天的时候，所有人坐车穿过城市，去海边度假。"

    tomori windbreaker expressionless "夏天。"

    anon windbreaker smile "你以前去过海边吗？"

    tomori windbreaker expressionless "我忘了。也许只是一场雨。"

    anon windbreaker smile "那就算是一次旅行。没有终点的旅行。"

    "车窗玻璃上两人的倒影晃动着。"
    "爱音整个人陷在座椅里，两只手揣在宽大的口袋里，侧过脸看着我。"
    "她的神情不再像刚才在医院里那样紧绷，眉眼间浮现出浅浅的轻松，甚至带着些许好奇。"

    anon windbreaker smile "灯。"

    tomori windbreaker expressionless "……嗯？"

    anon windbreaker smile "我想更多了解你。"

    "我愣在座位上。在生命的尽头，在这个只剩下一百五十五个小时的早晨，我才突然反应过来：我对身边的千早爱音，几乎一无所知。"
    "而她却把自己的一切押在了一个快要死掉的人身上。"

    anon windbreaker smile "昨晚你说的那个乐队……叫CRYCHIC对吧？"
    anon windbreaker smile "还有你本子里写到的那些人，立希，还有那个叫祥子的女孩。"
    anon windbreaker smile "你们以前也是这样，坐着车去演出或者练习吗？"

    tomori windbreaker expressionless "祥子……立希……"

    # 4. 高松灯的解离体验
    stop music fadeout 1.5
    play music bgm_painful_memory fadein 2.0 loop

    "记忆里那场暴雨的声音骤然砸下来。"
    "把窗户关上。外面的光太亮了，我已经没有力气再去辨认那些树影。"
    "看哪，这就是我们剩下的全部时间。这么短，甚至来不及喝完一杯冷掉的水。"
    "你在这里。你却又离我这么远。"
    "不要说话。一旦开口，那些词就会碎在地板上，像干枯的叶子。"
    "我写了一辈子，最后只剩下一个词。但我把它弄丢了。"
    "冷。从脚趾开始的冷。"

    play sound sfx_impact
    "怀里的黑色笔记本啪的一声滑落在地上。"

    show anon windbreaker worried at center_standee with dissolve

    anon windbreaker worried "灯？灯？你怎么了？手怎么这么凉？！"

    "【高松灯的解离】爱音，把你的手给我。不，算了，你的手太热了，像某种我不熟悉的生命。"
    "来帮我把笔记本捡起来，我没有什么可写的了。"
    "我从未扔掉一块石头。"

    "爱音把整条毛毯盖在我的膝盖上，双手用力搓着我僵硬的手背。"
    "她的呼吸急促起来，声音里满是掩饰不住的慌乱。"

    play sound sfx_strike
    anon windbreaker worried "{size=+3}{b}高松灯！看着我！你别吓我啊！{/b}{/size}" with shake_h

    "【高松灯的解离】所有人都很耀眼。一个连怎样呼吸都做不好的女孩。这就是我。如此而已。"
    "别松开我的手，求求你们。"
    "别管我，我本来就应该一个人待在角落里。"
    "我的手指，她在贴创可贴。"
    "祥子，我要向你道歉，但我不知道自己做错了什么。"
    "我那么喜欢你们。而现在我要掉队了。"
    "这是尽头。结束了。这是终点。太突然了。终结让我感到迷惑。"
    "我感到一种寒意袭来：时间。真让人害怕。"
    "企鹅停止了游动。"
    "我很害怕。"

    anon windbreaker worried "是不是胸口又疼了？还是呼吸不上来？"

    tomori windbreaker expressionless "……没什么。{w=0.4}企鹅停下来了。"

    anon windbreaker worried "企鹅……？什么企鹅啊！水族馆的企鹅吗？"

    "【高松灯的审视】我不甘心。我感觉自己路过了你的一生，却没有推开过你的门。"
    "一无所知。除了你的名字和温度，我一无所知。"
    "我不能带着这样的空白闭上眼睛。"
    "我一直以为还有很多时间。没有办法，我一直以为“一辈子”是很久很久。"
    "你从来不说你自己的事。这是某种迁就。我呢，我理所当然地躲在你的温柔里。"
    "就一句话，快。告诉我你最讨厌的颜色。我们交换。快。"

    tomori windbreaker expressionless "我喜欢……"

    "我其实……我那么爱你。不是作为乐队的主唱，也不是作为迷路的孩子。"
    "我真不知道原来爱一个人……是可以连她几点睡觉都不知道的。"
    "有几秒钟我摸到了你手指上的茧。"
    "从我自己的世界里走出来，这让人眩晕。有时候你的眼睛深得让人害怕。"
    "我厌倦了只谈论我自己。"
    "我想写一首只有你的名字的歌。哪怕一个韵脚都没有。不管是喜欢还是爱。"
    "快来。在一切停下之前，告诉我你的全部。我要现在开始喜欢你。"

    anon windbreaker surprised "……哈？喜欢什么？"

    "爱音转过头来看我。"

    tomori windbreaker smile "……我喜欢和你玩。"

    anon windbreaker surprised "诶？{w=0.4}原来只是这样吗。"
    anon windbreaker smile "真是的！还以为你要说什么不得了的话呢！"
    anon windbreaker smile "哪有人大清早一本正经地向别人表白“喜欢和你玩”的啊！"

    "“我喜欢……”"
    "你转过头来看我了。"
    "……我喜欢和你玩。一个将要把我留在原地的女孩。"
    "除此以外，在舞台上或角落里，在我呼吸之前或停止之后，都无所谓。"
    "我爱你。"
    "人类是可以靠这种微小的动作活下去的。"

    # 5. 分享耳机与围巾
    play music bgm_dialogue_warm fadein 2.0 loop

    "大巴驶过一程又一程道路。车厢静了。乘客缩在座位里，早晨的首班车不比末班车清醒太多。我们成了后排唯一醒着的人。"

    anon windbreaker gentle "听歌吗？分你一只。"

    "我没有拒绝，安静地接过来塞进了耳廓里。"

    anon windbreaker smile "你不冷了吗，灯？"

    tomori windbreaker smile "不冷了。我想听着这首歌。"

    "后来，当车厢顶部的夜灯暗下去，路灯的第一道微光穿透蒙着水雾的车窗照进后排时，千早爱音没有松开我的手指。"
    "她把自己的围巾扯开一半，轻轻围在我的脖颈上。"
    "我看着爱音闭上的睫毛。颠簸慢了下来。晨光与夜色交织在一起。"

    # 6. 早班电车与池袋目标
    stop bgs fadeout 1.5
    scene bg train_window with dissolve
    play bgs bgs_train_interior fadein 2.0 loop

    "车厢里重新陷入了短暂的宁静。"
    "窗外的树木和电线杆一根接一根地退后。"
    "爱音两只手搓了搓自己的脸颊，轻咳了一声，把脸别向我。"

    show anon windbreaker smile at center_standee with dissolve

    anon windbreaker smile "好啦好啦！别总是一副要哭出来的表情嘛！"
    anon windbreaker smile "既然都跑出来了，我们一会去哪里？总要先找个落脚的地方吧？"

    tomori windbreaker expressionless "去哪里……我不知道。"

    anon windbreaker smile "不能一直坐在这趟车上，车总会到终点的。"

    tomori windbreaker expressionless "有时候……电车也会迷路。"

    anon windbreaker smirk "电车有轨道怎么会迷路啦！你做什么？一直沿着窗户看？"

    tomori windbreaker expressionless "嗯。沿着窗户看。"

    anon windbreaker smile "仅此而已？"

    tomori windbreaker expressionless "仅此而已。"

    anon windbreaker grin "真拿你没办法。那我们去商场吧！池袋那边的大商场！"

    tomori windbreaker expressionless "……商场？可是，爱音……现在才早上六点多。商场很明显这个时候不开门。"

    anon windbreaker smirk "哎呀！本小姐当然知道不开门啦！商场一般都要十点或者十一点才开始营业呢！"

    tomori windbreaker expressionless "那我们这么早过去……要做什么？"

    anon windbreaker excited "在外面等开门啊！"
    anon windbreaker excited "我们在车站周围转转，或者先去地下街找便利店买热饮！"
    anon windbreaker excited "等十点大门一开，我们做第一批冲进去的顾客！"

    tomori windbreaker expressionless "第一批……"

    anon windbreaker confident "对啊！第一批冲进去，把里面好吃的好玩的全部占领！然后两个人并排走在商场正中央！怎么样，听起来是不是超有排面！"

    tomori windbreaker expressionless "那里……人会很多吗。"

    anon windbreaker smile "大清早刚开门哪有什么人啊！只有我们两个！"

    tomori windbreaker expressionless "如果有人看到我们……"

    anon windbreaker gentle "谁都看得到我们，两个穿着大号夹克和病号服的怪人！不过，只有我看得到真正的你。"

    tomori windbreaker smile "爱音看到了什么？"

    anon windbreaker smile "看到一个说‘喜欢和我玩’的笨蛋主唱！"
    anon windbreaker excited "走啦，下一站换乘，目标池袋商场！"

    tomori windbreaker expressionless "……池袋商场。真是一个……很远的地方。"

    anon windbreaker smile "不远啦！换乘之后坐几站就到！怎么啦小灯，眼皮都在打架了？"

    tomori windbreaker expressionless "有一点……困。十六年来……从来没有这么早就跑出来过。"

    anon windbreaker gentle "困了就先靠着我的肩膀睡一会儿！等到了池袋，我叫你起床！"

    tomori windbreaker smile "……嗯。"

    stop music fadeout 2.5
    stop bgs fadeout 2.5
    scene black with slow_dissolve

    $ persistent.cleared_chapter_7 = True
    jump ch08_nightbus
