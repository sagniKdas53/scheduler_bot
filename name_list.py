dict_translated = {'Iofi': 'Iofi', '常闇トワ': 'Towa', '猫又おかゆ': 'Okayu', 'アルランディス': 'Aruran',
                   '花咲みやび': 'Miyabi', '白銀ノエル': 'Noel', '桐生ココ': 'Coco', '鏡見キラ': 'Kira',
                   '百鬼あやめ': 'Ayame', '天音かなた': 'Kanata', '影山シエン': 'Shien', 'Gura': 'Gura',
                   'Amelia': 'Amelia', '姫森ルーナ': 'Luna', '癒月ちょこ': 'Choco', '岸堂天真': 'Temma',
                   'アステル・レダ': 'Reda', '夜空メル': 'Mel', '星街すいせい': 'Suisei', '紫咲シオン': 'Shion',
                   '兎田ぺこら': 'Pekora', 'Risu': 'Risu', '荒咬オウガ': 'Ouga', '桃鈴ねね': 'Nene', '雪花ラミィ': 'Lamy',
                   '白上フブキ': 'Fubuki', '奏手イヅル': 'Izuru', '戌神ころね': 'Korone', '湊あくあ': 'Aqua',
                   '大空スバル': 'Subaru', '角巻わため': 'Watame', 'Moona': 'Moona', '不知火フレア': 'Flare',
                   '夕刻ロベル': 'Robert', 'アキロゼ': 'Akirose', '潤羽るしあ': 'Rushia', '赤井はあと': 'Haato',
                   '尾丸ポルカ': 'Polka', '獅白ぼたん': 'Botan', '夏色まつり': 'Matsuri',
                   'Kiara': 'Kiara', '宝鐘マリン': 'Marine', '律可': 'Ritsumei', 'Calli': 'Calli', 'Ina': 'Ina',
                   'ロボ子さん': 'Roboco', 'ときのそら': 'Sora', 'さくらみこ': 'Miko', '大神ミオ': 'Mio', 'AZKi': 'AZKi',
                   '夜霧': 'Yogiri', '希薇娅': 'Civia', '黑桃影': 'Echo', '朵莉丝': 'Doris', '阿媂娅': 'Artia',
                   '罗莎琳': 'Rosalyn', 'holo': 'Some branch channel'}

na = open('names', 'w')
na.write('The names in jp and eng are:\n')
for nam in dict_translated.keys():
    na.write(nam + ':' + dict_translated[nam] + '\n')
