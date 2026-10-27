## ch11_proposal.rpy - 事件 27+28+29：海边的奔跑与创口贴的求婚
## 对应剧本：立希登门道别、二手婚纱与时代的废墟、末班车奔赴九十九里滨、倒流的雨与太阳吞噬地球的极光

label ch11_proposal:
    $ current_chapter = 11

    # 1. 昏暗卧室中立希的到来
    scene bg apartment_bedroom with fade
    play music bgm_painful_memory fadein 2.0 loop

    "沙发很软，我坐在阴影里翻看膝盖上那本写满了字句的旧笔记本，等着千早回来。"
    "她那件粉色的旧外套就搭在沙发扶手上，我用双手紧紧握着袖口。"
    "我终于开始读着笔记本上的词句，而且理解我所读的了。但是，读这些旧日写下的句子，就像是在追随某个陌生人的生活过程，这太使我讨厌了。我极想生活。"
    "就在这时，玄关的门猛地被推开了。一股夹杂着潮湿水汽的穿堂风猛灌进来。"
    "我抬起头，以为只是千早回来了，但站在玄关那里的，却是一个我无论如何也想不到会在此时此地出现的人。"

    show taki casual concerned at center_standee with dissolve

    "立希就站在走廊过道的暗影里，紧跟在千早身后。"
    "她怎么会在这里？她是怎么找到这间房间的？"
    "千早默默地退到一旁，靠着墙壁垂下眼睛，把房间中央的空间留给了我和立希。"
    "立希向前走了一步，停在离沙发两米远的地方。她看着我，眼神里没有我预想中的愤怒与指责，只有一种深不见底的悲哀与温存——"
    "就在对上她目光的那一秒，我突然明白了：千早已经把一切都告诉她了。她什么都知道了。"

    tomori windbreaker expressionless "立希……你来了。"

    taki casual concerned "嗯。我来看看你。"

    tomori windbreaker sad "对不起……因为我的事情，把以前的乐队弄得一团糟……还让你一直那么难过。"
    tomori windbreaker sad "我从来没有讨厌过你，立希。不管从哪个角度，我都从来没有讨厌过你。"

    taki casual concerned "别说了，灯。那些事早就过去了。是我自己要来的。"

    "立希的目光慢慢扫过这间昏暗的房间。她看见了丢在墙角的吉他盒，看见了桌上冷掉的红茶，最后停在衣架上那件雪白的蕾丝婚纱上。"

    show item wedding dress at right with dissolve

    taki casual concerned "那件衣服……就是她说的婚纱？"

    tomori windbreaker expressionless "嗯。从旧货店买回来的。是别人穿剩下的。"

    hide item wedding dress with dissolve

    "立希望着那件婚纱，轻轻点了点头。"
    "在那一瞬间，我忽然意识到，无论是立希、千早还是我，我们都在使用二手词汇生活。"
    "用别人用过的词，表达别人感受过的痛苦，甚至连我们所经历的心碎、背叛与爱，也全都是二手的。"
    "那个伟大的、庞大的时代早就在那个暴雨天轰然倒塌了。我们站在那支乐队的瓦砾堆上，两手空空，试图用旧时代的碎砖破瓦拼凑出自己的生活。"
    "从前的我们曾相信未来，愿意为了一个虚无缥缈的理想献出全部的青春；而当我们醒来时，才发现未来早已被预先变卖了。"
    "但每个人身上又都带着抹不掉的旧时代的烙印。"

    tomori windbreaker smile "立希。我这两天写了一首歌。词和曲都写好了……让我给你唱一下吧。"

    taki casual concerned "不用了，灯。没有时间了。"

    tomori windbreaker expressionless "没有时间了？……"

    taki casual concerned "起风了。一会儿要下雨了。你们不是还要出门吗？那就得快一点。趁雨还没下大。"

    tomori windbreaker expressionless "那你呢？你要回去了？"

    taki casual concerned "我回去了。"

    tomori windbreaker smile "我们……以后还会再见吗？"

    "立希没有回答这个问题。"
    "远处传来电车驶过铁桥的鸣笛声，低沉而悠长，像一声穿透整个城市平原的哀鸣。"
    "立希转过身，准备朝玄关走去。但在迈出房门之前，她在离我半步远的地方停住脚步。"

    taki casual concerned "您不介意我最后再吻你一下吧？"

    tomori windbreaker expressionless "不介意……"

    "我闭上了眼睛。"
    "吻结束了。立希直起身，没有再看千早，也没有回头，快步走出玄关，轻轻带上了门。"
    "我再也没有见过她。"

    hide taki with dissolve

    # 2. 换上婚纱与最后的准备
    scene bg apartment_bedroom with dissolve
    play music bgm_dialogue_warm fadein 2.0 loop

    "房间里重新安静下来。窗外传来沉闷的雷声。"

    show anon wedding smile at center_standee with dissolve

    anon wedding smile "外面的天已经黑下来了。但是就算下雨又怎么样呢？要抓紧时间啊，我们还来得及。"

    "千早脸上挂着大大的笑容。她伸手帮我理了理脖子上的白头纱，又把一件针织开衫披在我肩上。"

    anon wedding gentle "外面很冷。裹紧一点。我只是不想你着凉，仅此而已。"

    "我看着她，大脑变得晕头转向的。"
    "两步之前还显而易见的事，现在却成了谜。似乎有太多的东西正在滑落，以前的乐队、学校的名字，全都从指缝里溜走了。"
    "但唯独胸口那种感觉一点都没有减弱。"

    tomori wedding shy "千早，我是什么时候遇见你的来着？我忘记了……但是我记得我喜欢你。"

    anon wedding blush "……这样啊。没关系。你不记得也没关系。因为我感觉我已经认识你很久很久了。"

    tomori wedding smile "我也是！这都不重要了。我们好长时间没见了！"

    anon wedding smile "对，一点都不重要了！走吧，我们去看海！"

    # 3. 终点站与海滩篝火余烬
    scene bg beach_sunset with dissolve
    "我们穿着宽大的白色婚纱，乘上末班列车，在空无一人的终点站下车，向着海岸线走去。"
    "太阳已经落山了。天边只剩下一抹暗红色的晚霞，像一道未愈合的伤口横贯在海平面上。"

    scene bg beach_night_fire with dissolve
    play bgs bgs_campfire fadein 2.0 loop
    play music bgm_seaside_view fadein 2.0 loop

    "海滩卵石堆旁残留着一堆旅人留下的篝火余烬，在海风里劈啪爆裂出成串暗红色的火星，照亮了我和千早被海风吹乱的头发，照亮了我们满是稚气与苍白的面孔。"

    # 4. 垂直暴雨与倒转的星辰
    stop bgs fadeout 1.0
    scene bg beach_rain with dissolve
    play bgs bgs_downpour fadein 1.5 loop

    "第一滴雨落在了我的鼻尖上。"
    "紧接着，倾盆大雨泼向了整片海洋与荒滩。世界任何地方都没有这样垂直下落的大雨。"
    "千早没有躲闪。她拖着湿透的白色婚纱，在布满卵石的海滩上跑来跑去，任凭狂风暴雨凶狠地抽打着她的脸。"

    show anon wedding smile at center_standee with dissolve

    anon wedding smile "嘿，小灯！过来！这里就是我们的舞台了！差不多是时候了！"

    tomori wedding smile "舞台……？对。我们是一支乐队。我还有最后一首歌要唱。"

    anon wedding smile "本小姐也没有带吉他，但我的手还记得所有的和弦！那你要把这最后一首歌唱给谁听呢，主唱大人？"

    "我环顾四周。就在这一瞬间，海滩、黑夜与沉闷的空气仿佛一道无形的墙壁，轰然倒塌了。"

    # 奇迹降临：逆流之雨
    scene bg beach_reverse_rain with slow_dissolve
    stop bgs fadeout 1.5
    play sound sfx_reverse_rain
    play music bgm_soaring fadein 2.0 loop

    "奇迹发生了。"
    "所有的重力在这一刻彻底消失。"
    "漫天倾盆的雨幕突然在半空中凝滞，然后开始倒转——成千上万颗晶莹的雨滴不再坠落，而是化作逆流的星辰，从漆黑的海面与卵石滩上腾空而起，向着深邃的夜空疯狂倒飞上去。"
    "我从婚纱口袋里掏出我收集了整整一整个青春的所有石头，把它们像棋子一样全部撒向倒转的雨幕与浩瀚的星空。"
    "我站在原地，浑身颤抖，一生中从未感受到如此纯粹的幸福。"
    "心底那些长达十几年的绝望、羞耻与恐惧荡然无存，一种从未有过的狂喜充盈了我身体的每一个细胞。"

    tomori wedding tears "千早……我有首歌要唱给你听。"

    anon wedding tears "什——什么？！只唱给我一个人听？！"

    tomori wedding smile "{size=+3}{b}没错。只唱给你听！所以，调好你的弦！演出开始。倒数三……二……{/b}{/size}" with shake_h

    anon wedding smile "吉他手千早爱音，准备就绪！随时可以开始！"

    tomori wedding smile "{size=+4}{b}一！！{/b}{/size}" with shake_h

    # 5. 太阳吞噬地球与纯白归宿
    scene bg whiteout with slow_dissolve
    stop music fadeout 2.5
    play sound sfx_whiteout_swell
    play music "audio/bgm/bgm_beyond.mp3" fadein 3.0 loop

    "爱音在虚空中用力挥下右手，拨响了那根看不见的琴弦。"
    "歌声冲破了厚达一万公里的大气层。"
    "就在最后一个音符落下的瞬间，海平面尽头那轮巨大的太阳轰然升起。"
    "炫目的白光从大海深处喷薄而出，地平线锯齿般的轮廓燃起了漫天大火，燃成红色、橙色和最刺眼的玫瑰粉色。"
    "太阳在疯狂地膨胀。它越来越大，越来越近，占满了整片天空。海浪在沸腾中蒸发，卵石在融化，远处的灯塔与身后的城市在刺目的白光中化作飞灰。"
    "垂死的、温柔的太阳正在吞噬整个地球。"
    "不再有两个物体了。天空、大海、倒飞的雨滴、白色的婚纱，还有我和她的身体，全都融化在同一片一万度的白光里。"
    "我在极度的光芒中扑进她的怀里，用尽全力抱紧她，用双手捧住她的脸，拼命地望着她，直到她失去一切世俗的意义，直到所有的轮廓都融为一体。"

    tomori "好亮啊。"

    anon "太阳掉下来了。"

    tomori "大海不见了。"

    anon "城市也不见了。地球要化掉了。"

    tomori "你还在吗？"

    anon "在。我抱着你呢。"

    tomori "好烫……你的手好烫。"

    anon "抓紧我。别松手。"

    tomori "{size=+2}{b}不松手。一辈子。{/b}{/size}" with shake_h

    anon "{size=+3}{b}小灯，我爱你。{/b}{/size}"

    tomori "{size=+3}{b}我也爱你。只爱你一个。{/b}{/size}"

    "白光吞没了我们的脚踝，吞没了我们的腰肢，吞没了我们交握的双手。脑海里的记忆像雪片一样剥落、飘向天空，留下来一片澄澈的纯白。"

    unknown "你……你叫什么名字来着？"

    unknown "我不知道。我忘了。"

    unknown "你是谁来着？"

    unknown "抱歉，我想不起来了。那你呢？你是谁？"

    unknown "……我也忘了。"

    unknown "没关系。"

    unknown "没关系？"

    unknown "嗯。是谁都没有关系了。"

    unknown "可是我还在抱着你。"

    "对。我还在这里。"

    "我爱你。"

    "我爱你。"

    "我爱你。我爱你。我爱你。"

    # 终局收尾
    stop music fadeout 4.0
    scene black with slow_dissolve

    $ persistent.cleared_chapter_11 = True
    $ persistent.cleared_game = True

    jump game_credits
