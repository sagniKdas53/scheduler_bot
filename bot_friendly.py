import csv
import re
from datetime import datetime

import pytz
import requests
import tabulate
from bs4 import BeautifulSoup as _soup_

'''Here i will write the functions that could and would be imported in the bot finally'''


class ExecFaster:
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
                 'Ritsumei', 'Calli', 'Ina', 'Roboco-san', 'Sora', 'Miko', 'Mio', 'AZKi', 'Yogiri', 'Civia', 'Echo',
                 'Doris', 'Artia', 'Rosalyn']

    checked_f = None
    data = None
    trans_d = None
    now = None

    def __init__(self):
        self.now = datetime.now()
        # make_file_html(file_name, False)
        self.checked_f = requests.get('https://schedule.hololive.tv/').content  # reads data from site
        self.data = self.start_reading(self.checked_f)  # parses it
        self.trans_d = self.translate_export(self.data, self.names_o, self.names_trs)  # translates it

    def show_in_time_zone(self, time_x):
        out_pt = self._convert_to_local_object(self.trans_d, time_x, 'show_all',
                                               True)  # takes in export_translated.csv and time zone
        print(out_pt)  # table of names and status in input time zone.

    def show_by_name(self, name_to_show, time_x, boole):
        if boole == 'not_over':
            out_pt = self._convert_to_local_object(self.trans_d, time_x,
                                                   name_to_show, False)
        else:
            out_pt = self._convert_to_local_object(self.trans_d, time_x,
                                                   name_to_show, True)
        return out_pt  # table of names and status in input time zone.

    def _convert_to_local_object(self, file, time_z, name, show_all):
        # print('\n', '*' * 25)
        list_table = []
        # list_details = []
        link_list = []
        indX = 0
        source_time_zone = pytz.timezone("Asia/Tokyo")
        reader = csv.DictReader(file)
        for row in reader:
            data = (row['MON'], row['DAY'], row['ID'], row['HR'], row['MN'], row['NAME'])  # MON,DAY,ID,HR,MN,NAME
            source_mon = data[0]
            source_day = data[1]
            source_link = '[Link](https://www.youtube.com/watch?v=' + data[2] + ')'
            source_hour = data[3]
            source_min = data[4]
            source_time = datetime(int(self.now.year), int(source_mon), int(source_day), int(source_hour),
                                   int(source_min), 00, 0000)
            source_date_with_timezone = source_time_zone.localize(source_time)
            # print(type(source_date_with_timezone))
            val = self.time_left(source_date_with_timezone)
            target_time_zone = pytz.timezone(time_z)
            writer = source_date_with_timezone.astimezone(target_time_zone)
            # list_details.append(['{},{},{},{}{}'.format(writer.strftime("%m,%d"), data[2],
            # writer.strftime("%H,%M"), data[5], '\n')])
            # print(val,type(val))
            if name == 'All' or name == data[5]:
                if val.days < 0:
                    if show_all:
                        list_table.append([indX, data[5], "Over", writer.hour, writer.minute])
                        link_list.append(source_link)
                else:
                    list_table.append([indX, data[5], str(val)[0:7], writer.hour, writer.minute])
                    link_list.append(source_link)
                indX += 1

        table = tabulate.tabulate(list_table, headers=['Index', 'Name', 'Status', 'Hour', 'Minute'], tablefmt="plain")
        return link_list, table

    def start_reading(self, file_content):
        day_list = []
        hold = [0, 0]
        ms = 0
        return_f = []
        # f = open(file_content)  # simplified for the example (no urllib)
        flip_soup = _soup_(file_content, "html.parser")
        # f.close()
        containers_date = flip_soup.find_all('div', class_="holodule navbar-text")
        containers_link = flip_soup.find_all('a', class_="thumbnail")
        for dates in containers_date:
            day = dates.text.strip().replace(' ', '').split()
            day_list.append(day[0].split('/'))
        print("Schedule contains: ")
        for month, day in day_list:
            print("{}/{},".format(month, day), end='')
        # f = open("export.csv", "w", encoding='utf8')
        return_f.append('MON,DAY,ID,HR,MN,NAME\n')
        for k in range(0, len(containers_link)):
            match = re.findall(r'href=\"https:[//]*www\.youtube\.com/watch\?v=([0-9A-Za-z_-]{10}[048AEIMQUYcgkosw]*)\"',
                               str(containers_link[k]))[0]
            time_name = containers_link[k].text.replace(' ', '').split()
            hr = time_name[0].split(':')
            if int(hr[0]) != 23 and int(hr[1]) <= 59 and hold[0] == 23:
                ms += 1
                return_f.append('{},{},{},{},{},{}{}'.format(day_list[ms][0], day_list[ms][1],
                                                             match,
                                                             hr[0], hr[1], time_name[1], '\n'))
                hold = [int(hr[0]), int(hr[1])]
            else:
                return_f.append('{},{},{},{},{},{}{}'.format(day_list[ms][0], day_list[ms][1],
                                                             match,
                                                             hr[0], hr[1], time_name[1], '\n'))
                hold = [int(hr[0]), int(hr[1])]
        return return_f

    def time_left(self, full_inp):
        self.now = datetime.now()
        target_time_zone = pytz.timezone('Asia/Kolkata')
        target_date_with_timezone = self.now.astimezone(target_time_zone)
        left = full_inp - target_date_with_timezone
        return left

    def translate_export(self, file, orig, tran):
        dict_name = {}
        for ele in range(len(orig)):
            dict_name[orig[ele].strip()] = tran[ele].strip()
        # print(name_list)
        # for name_data in name_list:
        # print(name_data[0],'\t',name_data[1])
        # dict_name = dict(name_list)  # idk how to fix this
        for key, val in dict_name.items():
            for idx, ele in enumerate(file):
                if key in ele:
                    file[idx] = ele.replace(key, val)
        return file

    def update(self):
        self.now = datetime.now()
        # make_file_html(file_name, False)
        self.checked_f = requests.get('https://schedule.hololive.tv/').content  # reads data from site
        self.data = self.start_reading(self.checked_f)  # parses it
        self.trans_d = self.translate_export(self.data, self.names_o, self.names_trs)  # translates it


'''
obJ_class = ExecFaster()
print(obJ_class.show_by_name('Fubuki', 'Asia/Kolkata', 'show_all'))
print(obJ_class.show_by_name('Coco', 'Asia/Kolkata', 'show_all'))
print(obJ_class.show_by_name('Ina', 'Asia/Kolkata', 'show_all'))
print(obJ_class.show_by_name('Gura', 'Asia/Kolkata', 'show_all'))

show_by_name()
takes first argument as name,
second is timezone third is Show show_all or over 
for seeing not over ones not over is the only input
for show_all anyting goes
print(show_by_name('Fubuki', 'Asia/Kolkata','show_all'))
print(show_by_name('show_all','Asia/Kolkata','not over'))

client = discord.Client()
@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("&&send"):
        text = message.content.split()
        response = show_by_name('Fubuki', 'Asia/Kolkata', 'show_all')
        await message.channel.send(response)
    elif message.content == 'raise-exception':
        raise discord.DiscordException
'''
