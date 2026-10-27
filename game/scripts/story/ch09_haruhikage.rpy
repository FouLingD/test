## ch09_haruhikage.rpy - 事件 22：爱音的房间与放声歌唱的春日影
## 对应剧本：深夜水族馆海底长廊、二楼卧室换上居家服、偷翻粉色日记本、黑暗中的真心告白、春日影独唱与身体的触碰

label ch09_haruhikage:
    $ current_chapter = 9

    # 1. 夜晚漫无目的电车与水族馆
    scene bg aquarium_tunnel with fade
    play music bgm_dreamy fadein 2.0 loop
    play bgs bgs_aquarium fadein 2.0 loop

    "在乘上列车后，我们去了很多地方。"
    "我们像两个真正拥有大把时间可以挥霍的高中女生一样，在东京的夜晚漫无目的地换乘。"
    "后来，我们去了水族馆。"
    "闭馆前的海底长廊空无一人。"
    "人造的冷光从巨大的亚克力水箱顶部打下来，打到水箱里时，灯光看起来很像星星。"

    show anon windbreaker smile at center_standee with dissolve

    tomori windbreaker smile "……爱音。我们要不要办一张年卡呢？"

    anon windbreaker smile "年卡？好呀！只要来三次就回本了呢！"

    "【高松灯的独白】但其实我心里清楚，好像已经没机会再来第二次了。"
    "我把头靠在她的肩膀上。"
    "为什么呢？我也说不清是怎样的想法。只是觉得如果不靠着点什么，身体就会在列车到站前彻底散架。"

    # 2. 夜里十一点半到达爱音家
    stop bgs fadeout 1.5
    scene bg apartment_entrance with dissolve
    play sound sfx_key_unlock
    $ renpy.pause(0.5, hard=False)
    play sound sfx_door_close
    scene bg apartment_bedroom with dissolve
    play music bgm_dialogue_warm fadein 2.0 loop

    "夜里十一点半。"
    "千早爱音的家。"
    "玄关的感应灯亮起又熄灭，我们轻手轻脚地走上二楼，关上了她房间的门。"

    show anon loungewear smile at center_standee with dissolve

    anon loungewear smile "病号服穿了那么长时间，肯定不舒服吧？"
    play sound sfx_clothes_rustle
    anon loungewear smile "给，换上我的居家服！虽然尺码可能稍微大一点点。"
    anon loungewear gentle "我去楼下端两杯热饮上来，小灯你随便坐哦！"

    hide anon with dissolve

    # 3. 书桌前的粉色日记本
    "房门轻轻合上。"
    "我在铺着毛绒地毯的书桌旁坐下，从书包里拿出自己那本边缘磨损的歌词本，摊开在桌面上。"
    "就在挪动笔筒的时候，我的指尖碰到了压在桌垫底下的一本粉色硬壳笔记本。"
    "封皮上贴着伦敦巴士的贴纸。"
    "那是爱音的本子。"
    "我鬼使神差地伸出手，翻开了第一页。"

    show item anon diary at center with dissolve

    play sound sfx_door_slide
    anon loungewear excited "——喂！小灯！"

    tomori windbreaker confused "……啊。对不起。"

    hide item anon diary with dissolve
    show anon loungewear blush at center_standee with dissolve

    "她低着头，把日记本紧紧护在胸口，我看着她的脸，她也正喘着气低头看着我。"

    anon loungewear blush "讨厌啦！怎么可以随便偷看别人的东西！"
    anon loungewear smirk "里面全都是我在伦敦大受欢迎的记录，小灯看了可是会嫉妒的哦！"

    # 4. 爱的觉醒与独白
    "【高松灯的独白】她笑得比平时更欢。"
    "末了我发现，我胸口闷得没法，眼睛里都噙满了眼泪。"
    "我几乎不明白自己正在发生什么变化。一种新的、莫名其妙的感觉激荡着我的身心，我可以毫不夸大地说，我在为这一新的感情而苦闷，而烦恼。"
    "简单地说——请原谅我用这样的语汇——我爱上了我的爱音。"
    "是的，这是爱，真正的爱，伴有眼泪和欢欣的爱，热情洋溢的爱。"
    "请相信我，没有一个人像我这样死心塌地、这样舍身忘己地注视过你。"
    "因为在世界上，没有什么东西可以比得上一个快要死去的孩子暗中怀有的、不为人所觉察的爱情。"
    "因为这种爱情不抱希望，低声下气，全神贯注，这和那些拥有漫长寿命的普通人完全不同。"
    "可我身边没有别人，我没法向别人诉说我的心事，我一头栽进我的命运，就像跌进一个深渊。"

    anon loungewear gentle "……小灯？你哭什么呀？我又没有真的生你的气！"

    tomori windbreaker expressionless "我没有哭……"

    anon loungewear tears "小灯！……我真是笨死了。其实我很早很早就喜欢上你了！你可知道是打什么时候开始的？"

    tomori windbreaker confused "……什么时候？"

    anon loungewear smile "打从你在天台上抓着栏杆，明明怕得发抖，却还是对我大声喊出心里话的那一次开始的……傻——瓜——小——灯！"

    "她拉长了调子说着，额头抵在我的手背上，又是哭，又是笑。"

    tomori windbreaker smile "爱音……"

    anon loungewear smile "什么事？说呀，什么事？"

    tomori windbreaker expressionless "为什么我们俩这么多时间一直……一直……"

    "我没把这句话说完。"
    "她从地毯上站起身，一把抱住我。我们互相拥抱，足有三分钟一句话也不说。"

    anon loungewear blush "你倒说说看，你对我是怎么想的？看到那个本子之后，是不是觉得我特别逊？"

    tomori windbreaker expressionless "没有。并且，事实上，我什么都没看见。不过我也能猜到里面的内容。"
    tomori windbreaker smile "至于我想得可太多了，爱音。我老是在想，白天夜里都想。"

    anon loungewear smirk "刚才在电车上睡着的时候，你还小声叫我名字来着，我听见过。"

    tomori windbreaker expressionless "……真的？"

    anon loungewear smile "还在病房里偷偷哭了不知多少次。我都看得出来。"

    tomori windbreaker expressionless "那你为什么总是要装出一副什么都不在乎的样子？"

    anon loungewear tears "因为我实在太蠢了，小灯！不知怎么的，我往往犯这样的毛病，完全没有旁的原因。有时候我甚至老是生你的气。"

    tomori windbreaker expressionless "为什么？"

    anon loungewear tears "就为了我自己是个爱慕虚荣的坏东西呗！先是因为你比我纯粹；后来因为不管走到哪里，像立希她们那样的人，眼里永远只有你。"
    anon loungewear gentle "听着，有时候我很想对你好，后来看到你把心事全锁在本子里，我一下子又想生你的气！可是后来我看到你离开了我根本没法在商场里走下去，我就在想：这个笨手笨脚的主唱，还得靠我千早爱音拉着才行！"

    tomori windbreaker smile "爱音很勇敢。"

    anon loungewear tears "其实，我怕——得——要——死！"
    anon loungewear tears "不管是在英国一个朋友都交不到的时候，还是第一次站在台上弹错和弦的时候，我都怕得要死！"
    anon loungewear tears "你知道我为什么非要装出那么神气的样子吗？因为当时你在场！我看到你在旁边瞧着……懂吗？！所以我不管不顾地往前冲。"
    anon loungewear gentle "其实，我非常担心你认为我肤浅、认为我愚蠢！你挺聪明，小灯，你写的每一句歌词都那么厉害，难道不是吗？"

    # 5. 关灯后的房间与春日影唱响
    scene bg apartment_bedroom_dark with slow_dissolve
    stop music fadeout 2.0
    play music bgm_music_box fadein 2.5 loop

    "关于这首歌本身，我并不想再说太多，属于歌声的，留给歌声。"
    "关于这首歌之外的，也许我想说一点。世事变化得太快了，自以为永远铭记的诺言，说不定几个月之后就模糊了一半。"
    "这首歌从初稿到今天走过了漫长的旅程，我几次想要放弃，把歌词本撕碎扔进垃圾桶，而促使我留下稿子、扔掉垃圾桶的，是眼前这个在黑暗中把后背靠在床边的女孩。"
    "她给我的每一句话，我都牢记；她对我的信任，让我第一次觉得自己可以重新开口。"

    "{cps=25}人知れず\n肩落としてる君がいるのに\n碧すぎてる空ばかりが眩しい\n僕はどんな言葉を君に\n言えばいいのか\n君に何を{/cps}"

    "窗帘边缘漏进来的夜空繁星闪烁，清新透明。"
    "举目一望，人会情不自禁地反问自己：在这样的天空底下，难道还会有人怒气冲冲、喜怒无常吗？"

    "{cps=25}脆くやわい こころで生きる\n僕らは 傷つく生き物で\nなのに 今日だって\n頑張ってる 十分 君はもう\n躓いて 転んだって\n立ち上がり来たんだ{/cps}"

    "打从大清早跟着爱音翻出医院大门起，我就受到一种莫名其妙的苦恼的折磨。"
    "我忽然觉得：我孤零零的，正在受到所有人的抛弃，所有的人都在离我而去。"
    "窗外远处的电车轨道与干线公路像一条发光的河流。"
    "但在这样一种流移变幻之中，我认识到自己在城市这巨大的马赛克当中，只不过一块微小的彩片；"
    "但这块微小的彩片，此刻在这个房间里，被另一块彩片握住了手心。"

    "{cps=25}こころを隠さないでほしい\nらしさなんて\nまだわからないままだけど\nぶつかるたび痛んで\nでも浮かびあがる輪郭\nああ 見つける{/cps}"

    # 闪回
    scene bg music_room with dissolve
    "【闪回】“如果你知道自己是谁，你可以去任何地方。”长崎爽世每次带我去月之森的沙龙茶室，总要微笑着对我说这个。"
    "【闪回】“他们根本不在乎你客不客气，”那时候丰川祥子坐在三角钢琴前，手指重重按在琴键上，冷淡地接上一句。"

    scene bg apartment_bedroom_dark with dissolve

    "{cps=25}逃げてもいい 道が見えなくても\n迷っても 君と走っていたいんだよ\n一緒に{/cps}"

    "有些篱笆从一开始就在那里。"

    play sound sfx_strike
    anon loungewear tears "{size=+3}{b}小灯……太犯规了……你这家伙，怎么能唱出这种歌啊……{/b}{/size}" with shake_h
    anon loungewear tears "我听见了……在黑暗里我全都听见了……什么篱笆，什么以前的人，全都去他的吧！"

    tomori windbreaker tears "爱音……你在哭吗？对不起，我最后一句唱破音了……"
    tomori windbreaker tears "我以为唱完这首歌我就会死掉，可是没有……爱音，你还在这里，你真的在听……"

    "我们像两个突然丧失了语言能力的傻瓜，在漆黑的被窝里紧紧抱成一团，颠三倒四、语无伦次地抢着说话。"
    "直闹到两个人都哭得精疲力尽、嗓子发哑，胸口剧烈地一起一伏，爱音才猛地吸了吸鼻子。"

    anon loungewear smile "小灯！首先，今天晚上你不准回医院，明天也不准，后天也不行！就睡在我的床上！"
    anon loungewear gentle "其次，我不喜欢你愁眉苦脸的样子！"

    tomori windbreaker smile "……嗯。"

    anon loungewear gentle "呐，小灯……刚才你唱的那首歌，我还有几个地方没听懂呢。"
    anon loungewear gentle "你看，这一句——“每次相撞都会作痛，却也因此浮现出轮廓”。小灯写这一句的时候，脑子里想的到底是什么呀？"

    tomori windbreaker expressionless "唔……想的是，不知道该怎么和别人靠近……每次靠近，都会把彼此弄疼……"

    "爱音低低地笑了一声。她贴着我的嘴角和耳廓轻声耳语。"
    "手指顺着我的衣领边缘探进去，轻轻摩挲着我锁骨下方微微凸起的骨节。"

    anon loungewear blush "骗人。刚才我扑过来抱住你的时候，小灯明明就没有躲开。"
    anon loungewear gentle "你在歌里不是唱了吗……“希望你不要把心藏起来”。小灯，你那些歌词，到底是写给我的脑子听的，还是写给我的身体听的？"

    "写歌的人，身体也参与了她的写作。那些词句进入她的头脑，同时又在这一刻进入了我们的身体。"

    tomori windbreaker smile "爱音……那句词后面，其实还有半句。“啊，找到了。”"
    tomori windbreaker smile "我不藏了，爱音。你刚才听到的每一个字……全都是因为想要触碰你，才写出来的。"

    "房间里骤然安静下来。"
    "爱音撑起身子，居高临下地望着我。"

    anon loungewear gentle "我现在就要你。"

    tomori windbreaker smile "嗯。"

    # 6. 海浪翻涌与约定去海边
    play bgs bgs_beach_night fadein 3.0
    "我听到一片海洋的声音，就在我身旁，只隔着爱音这间卧室的一道薄墙与砂堤。"
    "街区的市声摩擦着百叶窗，就像潮水拍打着海岸。那天夜里，大海就在情人们的房间里。"

    tomori windbreaker smile "我们一定要去海边一次，可以吗？"

    anon loungewear gentle "为什么，一定要海边？"

    tomori windbreaker smile "我听到了大海的声音。"

    anon loungewear gentle "好。我们去海边。随你的意，什么时候去都可以。"

    tomori windbreaker expressionless "我还是忘不了之前的乐队。"

    anon loungewear gentle "让我去解决吧。"

    "是的，爱音，哪怕明知道只剩下最后一百四十个小时，哪怕明知道这一切建立在一场谎言之上，人也会情不自禁地相信：真正的、诚挚的激动是能够彻底触动灵魂的；"
    "在这原本无血无肉、虚无缥缈的幻想之中，是有着可以感触得到的、活生生的东西的。"

    stop music fadeout 2.5
    stop bgs fadeout 2.5
    scene black with slow_dissolve

    $ persistent.cleared_chapter_9 = True
    jump ch10_wedding
