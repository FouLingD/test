## ch03_encounter.rpy - 事件 04+05：走廊的哭声与逃兵的驻足
## 对应剧本：503病房门外的偶遇、爱音的自尊与笨拙的破冰交谈
## 包含完整原案 138 个文本块、共 274 句对白与旁白，100% 完整保留无任何删节。

label ch03_encounter:
    $ current_chapter = 3

    # 走廊巡视与503病房门前
    scene bg hospital_room with fade
    play bgs bgs_hospital fadein 2.0 loop


    play sound sfx_door_slide
    play music bgm_anon_theme fadein 1.5 loop
    show anon hospital smirk at center_standee with dissolve

    tomori hospital expressionless "……！"

    unknown "哟。{w=0.4}醒啦？"

    "我下次应该记忆力再好一点，我敢打赌她认为医生也早就把她介绍给我了。"
    "她的名字在我的舌尖打转，但是就是想不起来……"
    "再配合上我的睡姿估计有够糟糕的，希望不要产生太糟糕的初印象吧！"

    unknown "喂喂，{w=0.4}你干嘛用那种看外星人的眼神看我啊？"
    unknown "我又不会咬人。"

    tomori hospital expressionless "……你、{w=0.3}你是谁？"

    unknown "诶？原来还需要我给你介绍吗？"

    tomori hospital pensive "……不知道。"

    unknown "真的假的？"
    unknown "隔壁503的啊！"
    unknown "早上医生查房的时候，在走廊里那么大声聊我的八卦，{w=0.4}你在屋里难道一点都没听到？"

    tomori hospital expressionless "……503？"

    pink_girl "对啊！{w=0.4}千早爱音！"

    tomori hospital expressionless "……千早同学。"

    voice "audio/voice/vo_anon_03_01.ogg"
    anon hospital smirk "叫爱音就好啦！"
    anon hospital smile "千早同学听起来太生疏了，{w=0.4}像教导主任点名一样。"

    tomori hospital expressionless "……千早同学。"

    anon hospital smile "好吧好吧，随你高兴。"
    anon hospital smile "所以，高松同学，你睡相还真是有够老实的，{w=0.4}整个人直挺挺地躺着，跟摆在博物馆里的展品一样。"

    tomori hospital tears "……对不起。"

    anon hospital smile "没必要突然道歉的呀，"
    anon hospital smile "睡相像展品又不是什么违反院规的事……就算真的有那东西的话。"
    anon hospital smile "你这个人平时在学校也是这样动不动就向人认错的吗？"
    anon hospital smile "一直这样的话，{w=0.4}会很辛苦的。"

    tomori hospital expressionless "……"

    "她拉过床边那把铁椅子，寻觅了一会病房里的空位，找个地方坐了下来。"

    anon hospital blush "真是个怪人。"
    anon hospital blush "不过算了，反正五楼全是一帮无聊透顶的怪人。"

    tomori hospital confused "……千早同学，为什么会在我的病房里？"

    anon hospital smile "这个嘛……"
    anon hospital smile "因为我那间病房太闷了！"

    tomori hospital expressionless "……闷？"

    anon hospital smile "对啊！电视机只能收到三个台，全是无聊的老年养生节目。"
    anon hospital smile "隔壁床那个阿姨一直在跟护工抱怨腰疼。"
    anon hospital tears "走廊里又冷得要死，护士长还整天盯着我不让我到处乱跑。"
    anon hospital smile "我本来想去活动室找人聊天的，结果活动室里只有两个大爷在下将棋，连个能说话的人都没有！"

    tomori hospital expressionless "可是……这里是单人病房。"

    anon hospital smile "就是因为是单人病房我才溜进来的啊！"

    tomori hospital expressionless "……？"

    anon hospital smile "你想想看嘛，要是多人病房，我推门进去多引人注目啊。"
    anon hospital smile "这里就你一个人。"
    anon hospital smile "而且早上护士说，501住着一个从来不开口说话、一口饭都不肯吃的人。"
    anon hospital smile "我一听就超级好奇好不好！"

    tomori hospital expressionless "……神秘？"

    anon hospital smile "对啊！听起来超有故事的感觉！"
    anon hospital smile "我还以为会看到什么阴郁系的大人物呢。"
    anon hospital smile "结果一推门进来，发现你正缩在被子里呼呼大睡，脸上还贴着退热贴。"

    tomori hospital confused "那是什么，我也说不清的。"

    "她应该听见了我的叹气声。"

    anon hospital smile "哎呀，差不多啦！反正都是冰冰凉凉贴在脑门上的东西！"

    "她说话语速很快。"
    "可能是坐的姿势不舒服了，她站起身来，在我的病房里四处转悠。"

    tomori hospital expressionless "还有就是……我不是大人物。"

    anon hospital smile "看得出来啦！"

    "她走到床头柜旁，目光落在那束白花上。"

    anon hospital smile "咦，这花是谁送的啊？"
    anon hospital smile "白百合？"

    tomori hospital expressionless "……朋友。"

    anon hospital smile "味道好浓哦，闻得我鼻子痒痒的。"

    tomori hospital expressionless "……"

    "她的视线移到了花瓶旁边的塑料盒子上。"

    anon hospital smile "哇！草莓布丁！"

    "像是一只发现了什么，爱音的眼睛一下子亮了起来。"
    "她伸出手指，戳了戳塑料盒表面那层透明的封膜。"

    anon hospital smile "喂，高松同学。"
    anon hospital smile "你……吃不吃这个啊？"

    tomori hospital expressionless "……千早同学想吃吗？"

    anon hospital smile "谁、谁想吃了！"

    "但是，明眼人都能看出来，明明是她被揭穿了吧。"
    "像一只发现零食的企鹅？但是企鹅又是分成很多种的……"
    "如果是企鹅科里的十八个物种，到底更接近哪一种呢？"
    "肯定不是皇帝企鹅。皇帝企鹅的身高超过一米一，她看起来大约一米六的样子？"
    "主要不是身高的问题，我是说，我认为她应该不会那么庄重？那么死板？"
    "王企鹅也不像。那么是阿德利企鹅吗？"
    "对。阿德利企鹅性格凶悍又极度爱面子，喜欢偷偷摸摸衔走邻居巢穴里的鹅卵石来炫耀。"
    "或者……更像是一只小蓝企鹅，或者是跳岩企鹅？"
    "而且，企鹅应该也见不到任何零食。"
    "从生物演化的常识来看，这个比喻从源头上就是不成立的。"
    "野生企鹅主要的食物来源是南极磷虾一类的东西。"
    "如果有谁突发奇想，丢下一整包拆开的饼干或者膨化薯片，一只路过的企鹅最多只会出于好奇去啄一啄包装袋。"
    "所以，这世上根本就不存在“发现零食的企鹅”。"
    "我大概盯着她看了太久。"
    "黑暗开始映衬着她的轮廓，她的耳根一点一点漫开红晕，终于忍无可忍地跺了跺脚。"

    anon hospital smile "喂！你一直面无表情盯着我发什么呆啊！"
    anon hospital smile "快点说话啊！"

    tomori hospital expressionless "阿德利企鹅，喜欢偷石头。"

    anon hospital surprised "哈？！这跟石头到底有什么关系啊！"
    anon hospital smile "我只是看它放在这里快要过期了，好心提醒你一句而已！"

    tomori hospital expressionless "保质期到后天。"

    anon hospital smile "……"

    tomori hospital expressionless "朋友买的。"
    tomori hospital expressionless "买来就是给别人吃的。"
    tomori hospital expressionless "千早同学想吃的话……拿去吃也可以。"

    anon hospital smile "真的？"
    anon hospital confident "你不会等会儿跟护士告状说我偷你东西吧？"

    tomori hospital pensive "不会。"
    tomori hospital expressionless "我不喜欢告状。"

    anon hospital smile "那我就不客气啦！"

    "她撕开塑料封膜，掰开附赠的小塑料勺。"
    "挖了一大勺布丁塞进嘴里。"

    anon hospital smile "唔！活过来了！"
    anon hospital smile "甜食果然是世界上最伟大的发明！"
    anon hospital smile "在英国的时候，那边的甜点太甜了，吃一口感觉牙齿都要被糖精腌入味了。"
    anon hospital smile "还是东京的布丁最合我的口味！"

    tomori hospital expressionless "……英国？"

    anon hospital smile "……对啊。"
    anon hospital excited "我之前在伦敦留学来着。"

    tomori hospital expressionless "伦敦……远吗？"

    anon hospital smile "当然远啦！坐飞机要飞十几个小时呢！"
    anon hospital excited "大本钟、伦敦眼、泰晤士河！"

    "她的手指在空中停不下来了喂。"

    anon hospital smile "满大街都是红色的双层巴士，超级洋气的！"

    tomori hospital expressionless "……听起来很厉害。"

    anon hospital smile "那是当然！"
    anon hospital smile "我在那边天天都和大家一起喝正统的英式下午茶！"

    tomori hospital expressionless "哇……"
    tomori hospital expressionless "……红茶，很苦吗？"

    "她一副拿我没办法的神情。"

    anon hospital smile "放两块方糖，再加一小勺鲜牛奶，一点都不苦。"
    anon hospital smile "每次我和同学们去茶室，我都会拍好多好看的照片发动态！"
    anon hospital smile "大家都在评论区里给我点赞呢！"

    tomori hospital expressionless "……千早同学的朋友很多呢。"

    anon hospital smile "那当然啦！"
    anon hospital smile "班上的外国同学经常围着我转呢！"
    anon hospital confident "如果有机会的话，你也一定要去一次才可以！"

    

    "国外。真好啊。"
    "我在心里默默地咀嚼着这几个字。"
    "在那个离东京坐飞机要十几个小时的地方，街上全都是不认识的人，到处都是听不懂的语言。"
    "有那么一瞬间，我突然想说，那你可以带我去吗？"
    "把我塞进你的行李箱里，或者拉着我的衣袖，带我离开东京，去到那个只要保持沉默就不会被苛责的世界去。"
    "毕竟，如果只是口头支持的话，那不就是在炫耀自己的经历吗？"
    "“如果有机会的话，你也一定要去一次才可以！”"
    "今天去这里，明天去那里，好像到哪里生活对于他们而言，只是在地图上指指点点就能完成的事情。"
    "不过，这也不能完全怪她啦。"
    "如果换成我是她的话，应该也会忍不住让别人流露出，“你好厉害！”这样的眼光吧。"
    "糟糕，我不应该把她想的那么坏的。"
    "对不起，我不应翻来覆去想这些用不着的东西。"
    "我想，她也许真的只是无聊了。"
    "我现在还不能下床……呃，其实这只是一句借口。我当然可以下床。不过，即使能下床，我也对同样的楼层中住着什么人没有兴趣。"
    "然而她不是这样，跋涉了那么遥远的路途，见识过那么多我没见过的风景。"
    "却依然想要被夸奖，想要成为焦点，想要证明自己的特别……"
    "这种心情，即便是我这样僻的人，其实也是能够模糊理解的。"

    tomori hospital expressionless "外国同学……会讲日语吗？"

    anon hospital smile "呃……怎么可能！"
    anon hospital excited "在伦敦当然全讲英文啦！"

    tomori hospital expressionless "千早同学的英文……很厉害吧。"

    "她眼神微微飘向窗外。明明外面什么都没有，她刚检查过了。"

    anon hospital smile "咳，还、还行吧！"
    anon hospital smile "日常交流完全没问题！"

    tomori hospital confused "那在学校上课的时候……大家都在聊些什么？"

    "她用小塑料勺漫无目的地戳着布丁边缘。"
    "诶？这么快就吃完了吗？"

    anon hospital smile "就……就聊流行音乐啊。"
    anon hospital smile "还有周末去哪里逛街，哪家店的裙子好看之类的……"

    tomori hospital smile "听起来……好热闹。"

    play sound sfx_heartbeat
    anon hospital smile "……嗯。"
    anon hospital smile "挺热闹的。"

    stop music

    "她低声应了一句。原本高高扬起的下巴慢慢垂了下来。"
    "病房里一下子安静下来。"

    tomori hospital expressionless "……千早同学？"

    anon hospital smile "啊？怎么了？"

    tomori hospital smile "伦敦的红茶那么好喝……学校也那么漂亮。"
    tomori hospital confused "千早同学……怎么会突然回东京了？"

    anon hospital smile "呃……这个嘛……"
    anon hospital smile "就、就放假了回国看看啊！"
    anon hospital smile "东京都内那么多好玩的地方，偶尔也想回来逛逛街嘛！"

    tomori hospital expressionless "可是……千早同学现在住在503病房。"

    anon hospital smile "那、那是意外！"
    anon hospital smile "突发情况懂不懂！"

    tomori hospital expressionless "……意外？"

    anon hospital smile "……就、就是水土不服而已啦！"
    anon hospital excited "伦敦的天气天天都在下雨，到处都是灰蒙蒙的冷风，吃的东西又油腻，胃一下子受不了就病倒了。"
    anon hospital smile "医生说需要回国静养一段时间，我才回来的！"
    anon hospital smile "才不是我想回来的呢！"

    play music bgm_anon_theme loop

    tomori hospital expressionless "……下雨。"

    anon hospital smile "嗯？怎么了？"

    tomori hospital expressionless "下雨天……确实很让人讨厌。"
    tomori hospital expressionless "衣服会湿透，鞋子里全都是泥水。"
    tomori hospital expressionless "浑身冷冰冰的。"

    anon hospital smile "对吧！你也这么觉得对吧！"
    anon hospital excited "伦敦的雨下起来根本没完没了，连打伞都没用，风一吹伞全被掀翻了！"
    anon hospital tears "讨厌死了！"

    tomori hospital expressionless "……嗯。"

    "她用勺子把盒底最后一点布丁刮干净，心情似乎又好了一点。"

    anon hospital smile "不过话说回来，高松同学你又是怎么进来的啊？"
    anon hospital smile "我看你手上包着纱布，肋骨好像也固定着夹板。"
    anon hospital smile "总不可能是跟我一样吃坏肚子了吧？"

    "她的视线一边在我的病床上扫来扫去，一边好奇地探着脑袋。"
    "我的心猛地揪紧了，余光瞥向枕头边那个摊开的黑色活页笔记本。"
    "本子里密密麻麻写满了像咒语一样碎裂的词句，关于西瓜虫，关于一种别的孩子避之不及的动物，关于沉在水底发不出声音的石头，全都是我最见不得人的奇怪自言自语。"
    "我祈祷她不会看到那些本子上奇怪的东西！"
    "……好吧，照她这种把别人的病房当成自家后花园、到处乱晃乱看的自来熟性格，她一定会看到的。"
    "我还不如祈祷点别的。"
    "比如祈祷外面的大雨突然把整栋大楼冲走，或者祈祷天花板现在就掉下来把我砸晕过去。"
    "晕过去就好了！眼前一黑，陷入彻底的昏迷，医生和护士就会惊慌失措地推着仪器冲进房间，把我的本子顺手放在桌子上。"

    tomori hospital expressionless "我……"
    tomori hospital expressionless "从高处掉下来了。"

    stop music


    anon hospital smile "高处？楼梯吗？"

    tomori hospital confused "……学校的天台。"

    play sound sfx_heartbeat
    anon hospital surprised "{size=+4}天、天台？！{/size}"

    "她很惊讶，像做错了什么一样把刚打开的本子合上了。"

    tomori hospital expressionless "……嗯。四楼。"

    anon hospital surprised "{size=+4}真的假的？！{/size}"

    tomori hospital expressionless "真的。"

    anon hospital smile "这、这也太夸张了吧……"
    anon hospital smile "你是不小心踩空了吗？"

    tomori hospital expressionless "……不是。"

    anon hospital smile "那难道是……"
    anon hospital smile "……你自己跳的？"

    tomori hospital expressionless "……嗯。"

    anon hospital smile "为什么啊……？！"

    tomori hospital expressionless "……"

    anon hospital smile "……很疼吗？"

    tomori hospital confused "……什么？"

    anon hospital surprised "从四楼跳下来……"
    anon hospital smile "摔在塑料棚上的时候，很疼吗？"



    #这里把音乐切换成test/game/audio/bgm/bgm_painful_memory.mp3吧，给一个闭眼的效果，全黑，这里变成类似nvl的。

    tomori hospital tears "{cps=20}……其实，跳下去的时候不疼。{/cps}"
    tomori hospital expressionless "风很大。"
    tomori hospital tears "在医院醒过来的时候……浑身都很疼。"

    "千早爱音原本晃来晃去的动作彻底停住了。"
    "但很快，她用力拍了拍自己的脸颊。"

    #睁眼

    anon hospital smile "那、那就说明你超走运的啊！"
    anon hospital smile "四楼掉下来居然还能好端端地在这里跟我说话，神明大人肯定在暗中保佑你呢！"
    anon hospital tears "俗话不是说嘛——大难不死，必有后福！"
    anon hospital smile "以后肯定会有超级棒的事情发生在你身上的！"

    tomori hospital confused "……那，千早同学什么时候带我去伦敦呢？"

    anon hospital smile "咳！"
    anon hospital smile "咳咳咳……！"

    tomori hospital expressionless "……千早同学？"

    anon hospital surprised "哈？！"
    anon hospital excited "伦、伦敦？！"
    anon hospital smile "你……你怎么突然问起这个啊！"

    tomori hospital expressionless "千早同学刚才说……如果有机会的话，一定要去一次才可以。"
    tomori hospital expressionless "去喝三层点心架的红茶，去坐红色的双层巴士。"
    tomori hospital confused "所以……我想知道什么时候可以去。"

    anon hospital smile "这、这种事……当然要等以后啦！"
    anon hospital smile "去英国要办很多手续的！护照啊，签证啊，机票也超级贵的！"
    anon hospital smile "至少……至少也要等我们都高中毕业以后吧！"
    anon hospital smile "不对！要等本小姐什么时候有空了才行！"

    tomori hospital smile "……好。"
    tomori hospital expressionless "那我等千早同学有空。"

    #音乐停止

    anon hospital smile "喂！你干嘛用这么一本正经的表情说这种话啊！"
    anon hospital smile "真是个超级麻烦的家伙……！"

    tomori hospital expressionless "……"

    anon hospital smile "哇！你刚才是不是笑了？！"
    anon hospital confident "高松同学你绝对笑了对吧！"

    tomori hospital smile "……没有笑。"

    anon hospital confident "绝对笑了！我都看到了！"

    "走廊外远处传来推车声。"
    "503床的千早同学？千早同学人呢？又跑哪去了？"

    play sound sfx_footsteps
    anon hospital smirk "好啦好啦。"
    anon hospital smile "高松同学，我先撤了！"
    anon hospital smile "明天下午要是没被抓，我再来找你玩！"
    anon hospital smile "草莓布丁超好吃的，谢啦！"

    tomori hospital expressionless "……千早同学。"

    "她停在门边，回头对我眨了眨右眼，比了个剪刀手。"

    anon hospital smirk "都说了叫我爱音啦！"
    anon hospital smile "明天见，{w=0.4}灯！"

    #播放音乐test/game/audio/bgm/bgm_anon_vulnerable.mp3

    play sound sfx_door_close
    hide anon with dissolve
    "门被迅速拉开，又轻轻关上。"
    "病房里重新只剩下我一个人。"
    "她真是一个可爱的，十足可爱的人。"
    "可爱到，足以让我第一次没有满脑子想着“为什么我还没有死掉”。"
    "什么时候带我去伦敦？是啊，什么时候呢。"
    "连我自己都搞不清楚，那究竟只是为了配合她的随口附和，还是心底深处真的冒出了一点点想去看看的念头。"
    "我甚至开始在脑海里默默编造着明天的对话。"
    "要是她明天又偷跑过来，我该对她说些什么？"
    "我不是在说她麻烦！相反，说是期待还来不及呢。"
    "万一她明天睡醒就忘了呢？万一她推开门，发现我其实沉闷又无趣、连一句讨人喜欢的话都挤不出来呢？"
    "不能这样。我必须避免这种情况。"
    play sound sfx_impact
    "{b}她不能走。我不能让她失望。她那么好。她在乎我，{w=0.4}哪怕是虚假的，也是在乎我！{/b}" with shake_h

    # 章节结束过渡
    stop music fadeout 2.5
    stop bgs fadeout 2.0
    scene black with slow_dissolve

    $ persistent.cleared_chapter_3 = True
    jump ch04_intrusion
