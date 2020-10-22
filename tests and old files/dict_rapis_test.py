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
                   '罗莎琳': 'Rosalyn', 'holoID': 'Hololive Indonesia'}

rapid_access_via_names = {}

for name in dict_translated.values():
    rapid_access_via_names[name] = {}

print(rapid_access_via_names)

rapid_access_via_names['Iofi']['id'] = {'Stuff': 'More stuff'}
rapid_access_via_names['Iofi']['id2'] = {'Stuff': 'More stuff'}

print(rapid_access_via_names)
print(rapid_access_via_names['Iofi'])
res = rapid_access_via_names['Iofi']
print(res)

'''
{'Iofi': {}, 'Towa': {}, 'Okayu': {}, 'Aruran': {}, 'Miyabi': {}, 'Noel': {}, 'Coco': {}, 'Kira': {}, 'Ayame': {}, 
'Kanata': {}, 'Shien': {}, 'Gura': {}, 'Amelia': {}, 'Luna': {}, 'Choco': {}, 'Temma': {}, 'Reda': {}, 'Mel': {}, 
'Suisei': {}, 'Shion': {}, 'Pekora': {}, 'Risu': {}, 'Ouga': {}, 'Nene': {}, 'Lamy': {}, 'Fubuki': {}, 'Izuru': {}, 
'Korone': {}, 'Aqua': {}, 'Subaru': {}, 'Watame': {}, 'Moona': {}, 'Flare': {}, 'Robert': {}, 'Akirose': {}, 
'Rushia': {}, 'Haato': {}, 'Polka': {}, 'Botan': {}, 'Matsuri': {}, 'Kiara': {}, 'Marine': {}, 'Ritsumei': {}, 
'Calli': {}, 'Ina': {}, 'Roboco': {}, 'Sora': {}, 'Miko': {}, 'Mio': {}, 'AZKi': {}, 'Yogiri': {}, 'Civia': {}, 
'Echo': {}, 'Doris': {}, 'Artia': {}, 'Rosalyn': {}, 'Hololive Indonesia': {}}
{'Iofi': {'id': {'Stuff': 'More stuff'}, 'id2': {'Stuff': 'More stuff'}}, 'Towa': {}, 'Okayu': {}, 'Aruran': {}, 
'Miyabi': {}, 'Noel': {}, 'Coco': {}, 'Kira': {}, 'Ayame': {}, 'Kanata': {}, 'Shien': {}, 'Gura': {}, 'Amelia': {}, 
'Luna': {}, 'Choco': {}, 'Temma': {}, 'Reda': {}, 'Mel': {}, 'Suisei': {}, 'Shion': {}, 'Pekora': {}, 'Risu': {}, 
'Ouga': {}, 'Nene': {}, 'Lamy': {}, 'Fubuki': {}, 'Izuru': {}, 'Korone': {}, 'Aqua': {}, 'Subaru': {}, 'Watame': {}, 
'Moona': {}, 'Flare': {}, 'Robert': {}, 'Akirose': {}, 'Rushia': {}, 'Haato': {}, 'Polka': {}, 'Botan': {}, 
'Matsuri': {}, 'Kiara': {}, 'Marine': {}, 'Ritsumei': {}, 'Calli': {}, 'Ina': {}, 'Roboco': {}, 'Sora': {}, 'Miko': {},
 'Mio': {}, 'AZKi': {}, 'Yogiri': {}, 'Civia': {}, 'Echo': {}, 'Doris': {}, 'Artia': {}, 'Rosalyn': {}, '
 Hololive Indonesia': {}}
{'id': {'Stuff': 'More stuff'}, 'id2': {'Stuff': 'More stuff'}}
{'id': {'Stuff': 'More stuff'}, 'id2': {'Stuff': 'More stuff'}}
'''
