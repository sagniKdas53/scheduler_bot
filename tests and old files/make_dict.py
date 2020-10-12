names_o = ['Iofi', '常闇トワ', '猫又おかゆ', 'アルランディス', '花咲みやび', '白銀ノエル', '桐生ココ', '鏡見キラ', '百鬼あやめ',
           '天音かなた', '影山シエン', 'Gura', 'Amelia', '姫森ルーナ', '癒月ちょこ', '岸堂天真', 'アステル・レダ', '夜空メル',
           '星街すいせい', '紫咲シオン', '兎田ぺこら', 'Risu', '荒咬オウガ', '桃鈴ねね', '雪花ラミィ', '白上フブキ', '奏手イヅル',
           '戌神ころね', '湊あくあ', '大空スバル', '角巻わため', 'Moona', '不知火フレア', '夕刻ロベル', 'アキロゼ', '潤羽るしあ',
           '赤井はあと', '尾丸ポルカ', '獅白ぼたん', '夏色まつり', 'Kiara', '宝鐘マリン', '律可', 'Calli', 'Ina', 'ロボ子さん',
           'ときのそら', 'さくらみこ', '大神ミオ', 'AZKi', '夜霧', '希薇娅', '黑桃影', '朵莉丝', '阿媂娅', '罗莎琳']

names_trs = ['Iofi', 'Towa', 'Okayu', 'Aruran', 'Miyabi', 'Noel', 'Coco', 'Kira', 'Ayame', 'Kanata', 'Shien',
             'Gura', 'Amelia', 'Luna', 'Choco', 'Temma', 'Reda', 'Mel', 'Suisei', 'Shion', 'Pekora', 'Risu',
             'Ouga', 'Nene', 'Lamy', 'Fubuki', 'Izuru', 'Korone', 'Aqua', 'Subaru', 'Watame', 'Moona',
             'Flare', 'Robert', 'Akirose', 'Rushia', 'Haato', 'Polka', 'Botan', 'Matsuri', 'Kiara', 'Marine',
             'Ritsumei', 'Calli', 'Ina', 'Roboco', 'Sora', 'Miko', 'Mio', 'AZKi', 'Yogiri', 'Civia', 'Echo',
             'Doris', 'Artia', 'Rosalyn']

dict_translated = {}

for o in range(0, len(names_o)):
    dict_translated[names_o[o]] = names_trs[o]

print(dict_translated)
