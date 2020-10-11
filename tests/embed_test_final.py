import discord

from token_cc import token

client = discord.Client()
link_s = [['[Link](https://www.youtube.com/watch?v=X4YCslrdvyc)'],
          ['[Link](https://www.youtube.com/watch?v=X4YCslrdvyc)']]

response = '   Index  Name    Status      Hour    Minute\n38  Kiara   LIVE NOW      19        35'

list_of_titles_and_thumbs = [['【ブレイブルー】続\u3000武\u3000者\u3000修\u3000行【ホロスターズ/夕刻ロベル】',
                              'https://i.ytimg.com/vi/oOV7jeR54PE/hqdefault.jpg'],
                             ['【マインクラフト】ついにこの時が来た。チェスト整理回！！！【角巻わため/ホロライブ４期生】',
                              'https://i.ytimg.com/vi/y3WPN1uBusg/hqdefault.jpg']
    ,
                             ['【雑談枠】初イベのわくVの感想会をする！【律可/荒咬オウガ/影山シエン】',
                              'https://i.ytimg.com/vi/ZlMt5wvCEW8/hqdefault.jpg']
    ,
                             ['【Dead by Daylight】今日から始めるDBD生活【雪花ラミィ/ホロライブ】',
                              'https://i.ytimg.com/vi/EgLwctUuu6M/hqdefault.jpg']
    ,
                             ['【Dead by Daylight】今日はキラー縛り!!ザクザクザクザクしてやる【#岸堂天真/ホロスターズ】',
                              'https://i.ytimg.com/vi/6ZfIkbqymh0/hqdefault.jpg']
    ,
                             ['【雑談】ゲリラ！新居ではじめての夜更かし【ホロライブ/猫又おかゆ】', 'https://i.ytimg.com/vi/2Nsp0z1AmV8/hqdefault.jpg']
    ,
                             ['早起きは三文の歌枠しっとり～♪【ホロライブ/尾丸ポルカ】', 'https://i.ytimg.com/vi/Es2ZdDDxS1s/hqdefault.jpg']
    ,
                             ['【ゼルダの伝説BotW】寄り道回🔥コログしれんやミニチャレンジしよ～💪✨【白銀ノエル/ホロライブ】',
                              'https://i.ytimg.com/vi/EdbkG0f5pV8/hqdefault.jpg']
    ,
                             ['【マイクラ】お昼のんびり作業の回（外装作りたい）【獅白ぼたん/ホロライブ】',
                              'https://i.ytimg.com/vi/M7YEhoiWfk8/hqdefault.jpg']
    ,
                             ['【耐久SP 】３５万人記念にみんなで出すぞ３５万ダメージ！！APEX参加型【ホロライブ/ロボ子さん】',
                              'https://i.ytimg.com/vi/ecEfC8XyNd0/hqdefault.jpg']
    ,
                             ['【MOTHER2/Earthbound】地球を救え！はじめてのマザー2ぺこ！【ホロライブ/兎田ぺこら】',
                              'https://i.ytimg.com/vi/G0seyxXfd4Y/hqdefault.jpg']
    ,
                             ['[MINECRAFT] HOLO EN SERVER #HololiveEnglish',
                              'https://i.ytimg.com/vi/NS3_sNTwIRw/hqdefault.jpg']
    ,
                             ['【初見実況】#6\u3000ゼルダの伝説・風のタクトやる！！！！The Legend of Zelda: The Wind Waker【ホロライブ/大空スバル】',
                              'https://i.ytimg.com/vi/czdJAMqyABQ/hqdefault.jpg']
    ,
                             ['【#姫森ルーナ誕生祭】みんなと一緒にお誕生日会を同時視聴！！枠バグなんてへっちゃらなのら！【姫森ルーナ/ホロライブ】',
                              'https://i.ytimg.com/vi/fke_19SYkow/hqdefault.jpg']
    ,
                             ['【APEX】そろそろホロスタ最底辺から脱却したい騎士【岸堂天真/ホロスターズ】',
                              'https://i.ytimg.com/vi/lW5A3Zb5Kk8/hqdefault.jpg']
    ,
                             ['【Minecraft】ホロ鯖でキツネ探しに行くYO！！【潤羽るしあ/ホロライブ】',
                              'https://i.ytimg.com/vi/t1eDPmIEFL0/hqdefault.jpg']
    ,
                             ['【 #FallGuys 】え？チャンピオン取れる気でいるんだけど甘い？【アルランディス】',
                              'https://i.ytimg.com/vi/1GcKrl7B0gM/hqdefault.jpg']
    ,
                             ['Name', 'Link']
    ,
                             ['【鳥魂】チキン度診断!! chicken race!!【ホロライブ/宝鐘マリン】',
                              'https://i.ytimg.com/vi/0no_i1t-x5k/hqdefault.jpg']
    ,
                             ['【ホロ村】占いの館を建てるための土地探し【マイクラ】', 'https://i.ytimg.com/vi/X6AfEL1nTCA/hqdefault.jpg']
    ,
                             ['【マリオ35】バトロワのマリオ！？目指すは1位！！【ホロライブ/紫咲シオン】',
                              'https://i.ytimg.com/vi/sYvKXfTLj4o/hqdefault.jpg']
    ,
                             ['【歌枠】テンションあげて盛り上がれ💥Sing and get excited!【ホロライブ/不知火フレア】',
                              'https://i.ytimg.com/vi/mx5mb9VrDdw/hqdefault.jpg']
    ,
                             ['ポルカ #02', 'https://i.ytimg.com/vi/aihfyFywJLQ/hqdefault.jpg']
    ,
                             ['Name', 'Link']
    ,
                             ['【真面目にバレンタイン他】Twitter動画まとめ【花咲みやび/ホロスターズ】',
                              'https://i.ytimg.com/vi/slo8jP-xhHw/hqdefault.jpg']
    ,
                             ['【にじさんじ身体測定】噂のお姉様白雪巴様診察いたします！【にじさんじ/白雪巴/ホロライブ/癒月ちょこ】',
                              'https://i.ytimg.com/vi/vrJJyXLLja8/hqdefault.jpg']
    ,
                             ['【日清カレーメシコラボ楽曲】「カレーメシ・イン・ミラクル」リリックビデオ【#ホロライブカレーメシWEEK】',
                              'https://i.ytimg.com/vi/3QJD9iekpDQ/hqdefault.jpg']
    ,
                             ['【 Passpartout】絵を描く、売る。【ホロライブ/宝鐘マリン】', 'https://i.ytimg.com/vi/LQontk074pY/hqdefault.jpg']
    ,
                             ['【Minecraft】まったり枠【＃ときのそら生放送】', 'https://i.ytimg.com/vi/ZaviNeTzE9o/hqdefault.jpg']
    ,
                             ['【雑談】～キャラ変雑談\u3000魔関西弁編～【荒咬オウガ/ホロスターズ】',
                              'https://i.ytimg.com/vi/jfJ4RbriM6I/hqdefault.jpg']
    ,
                             ['【歌枠】第２９回！わためぇ Night Fever!!【角巻わため/ホロライブ４期生】',
                              'https://i.ytimg.com/vi/79ENOpKJG64/hqdefault.jpg']
    ,
                             ['【Minecraft】ホロ鯖！マイクラで show♪ぺこ！【ホロライブ/兎田ぺこら】',
                              'https://i.ytimg.com/vi/KWha-oxX-48/hqdefault.jpg']
    ,
                             ['【Celebration】6month and 100K Thankyou!  - ID | EN【Moona】',
                              'https://i.ytimg.com/vi/aS4yelfhPq4/hqdefault.jpg']
    , ['【 #アランストリーム 】深夜のアルラジオ#11【アルランディス/ホロスターズ】',
       'https://i.ytimg.com/vi/48TDTk74aQc/hqdefault.jpg']
    , ['【歌枠】歌うぞ～～～～～～～～【桃鈴ねね/ホロライブ】', 'https://i.ytimg.com/vi/9C5CZ7hdcAo/hqdefault.jpg']
    , ['https://www.youtube.com/watch?v=X4YCslrdvyc', '【耐久SP 】３５万人記念にみんなで出すぞ３５万ダメージ！！APEX参加型#2【ホロライブ/ロボ子さん】',
       # this is the only live that's correct
       'https://i.ytimg.com/vi/XFO_4O-aBGM/hqdefault.jpg']
    , ['【アソビ大全】るしあ先輩と今日はアソビつくす大全！【ホロライブ/#るししし】', 'https://i.ytimg.com/vi/NKFFXwZx8hw/hqdefault.jpg']
    , ['【ASMR耳元雑談】新作歌ってみた同時視聴！【Hololive/Akirose】', 'https://i.ytimg.com/vi/96sBSzSp19o/hqdefault.jpg']
    , ['【300k THANK YOU】KARAOKE PARTY!  #kfp #キアライブ', 'https://i.ytimg.com/vi/X4YCslrdvyc/hqdefault.jpg']
    , ['気まぐれメルシィKimagure Mercy/アキ・ローゼンタール【歌ってみた】', 'https://i.ytimg.com/vi/MSX8QbJR0eQ/hqdefault.jpg']
    , ['【90万人記念】お休み中のお話とありがとうの歌【ホロライブ/戌神ころね】', 'https://i.ytimg.com/vi/7U5-eDzWLBY/hqdefault.jpg']
    , ['【作業配信】サムネ作りながらまったり雑談【雪花ラミィ/ホロライブ】', 'https://i.ytimg.com/vi/ByBEbEVdzSs/hqdefault.jpg']
    , ['【雑談】夜ふかし悪魔のお話し会【ホロライブ/癒月ちょこ】', 'https://i.ytimg.com/vi/Er0xgACkKRw/hqdefault.jpg']
    , ['【ゲリラ弾き語り枠】no archive：久しぶりなかんじがする【律可/ホロスターズ】', 'https://i.ytimg.com/vi/Y3KCe88ryog/hqdefault.jpg']
    , ['【マイクラホロ鯖】んなっ！地下倉庫がダンジョンっぽくなっちまったのら！ -Minecraft-【姫森ルーナ/ホロライブ】',
       'https://i.ytimg.com/vi/0UGxH_yHvoo/hqdefault.jpg']
    , ['【歌番組】わためのうた ーボイトレ編ー （１０月１２日）【角巻わため/ホロライブ４期生】', 'https://i.ytimg.com/vi/zndO75r4sB0/hqdefault.jpg']
    , ['【朝活】生活習慣改善－今週も始まったわ！夕刻ロベルの朝活の時間ね！－【ホロスターズ/夕刻ロベル】', 'https://i.ytimg.com/vi/GNn8OJHY1P4/hqdefault.jpg']
    , ['【ゼノブレイド】DLC攻略！－つながる未来の物語－【ホロスターズ/夕刻ロベル】#1', 'https://i.ytimg.com/vi/OQFRTxFG86U/hqdefault.jpg']
    , ['【マインクラフト/Minecraft】レンガで庭を造るよ！Build a garden with bricks!【ホロライブ/不知火フレア】',
       'https://i.ytimg.com/vi/TYXQluT5JYc/hqdefault.jpg']
                             ]


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("&&send"):
        print(link_s, response)
        embed = discord.Embed(title='Video')
        for item in link_s:
            for data in list_of_titles_and_thumbs:
                if item[0][7:-1] == data[0]:
                    print(data)
                    embed.add_field(name=data[1], value=item[0], inline=True)
                    embed.set_image(url=data[2])
                    await message.channel.send(embed=embed)
                    embed.clear_fields()


"""    embed = discord.Embed(title='LIST')
    size = len(link_s)
    print("Number of entries =" + str(size))
    for link in link_s:
        for sub_l in obJ_class.list_of_titles_and_thumbs:
            if link in sub_l:
                embed.add_field(name=sub_l[1], value='[Video](' + link + ')',
                                inline=True)  # something is wrong here i can't remember what it is tho
                embed.set_image(url=sub_l[2])
                await message.channel.send(embed=embed)
                embed.clear_fields()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
embed = discord.Embed(title='Video')
    for row in range(0, size):
        print(list_of_titles_and_thumbs[row])
        embed.add_field(name=list_of_titles_and_thumbs[row][0], value='[Vid](' + test_list[row] + ')', inline=True)
        embed.set_image(url=list_of_titles_and_thumbs[row][1])
        await message.channel.send(embed=embed)
        embed.clear_fields()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
if message.content.startswith("&&testC"):
    embed = discord.Embed(title='Video')
    for row in range(0, size):
        print(list_of_titles_and_thumbs[row])
        embed.add_field(name=list_of_titles_and_thumbs[row][0], value='[Vid](' + test_list[row] + ')', inline=True)
        embed.set_image(url=list_of_titles_and_thumbs[row][1])
        await message.channel.send(embed=embed)
        embed.clear_fields()"""

client.run(token(), bot=True)
