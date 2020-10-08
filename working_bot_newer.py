import csv
import json
import re
from datetime import datetime
from urllib import request, parse

import pytz
import requests
import tabulate
from bs4 import BeautifulSoup as _soup_


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
                 'Ritsumei', 'Calli', 'Ina', 'Roboco', 'Sora', 'Miko', 'Mio', 'AZKi', 'Yogiri', 'Civia', 'Echo',
                 'Doris', 'Artia', 'Rosalyn']

    checked_f = None
    data = None
    trans_d = None
    now = None
    list_of_titles_and_thumbs = []
    list_url = []

    def __init__(self):
        self.now = datetime.now()
        self.checked_f = requests.get('https://schedule.hololive.tv/').content  # reads data from site
        self.data = self.start_reading(self.checked_f)  # parses it
        self.trans_d = self.translate_export(self.data, self.names_o, self.names_trs)  # translates it
        self.list_of_titles_and_thumbs = self.video_details(self.list_url)
        print(self.list_of_titles_and_thumbs)

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
        list_table = []
        link_list = []
        indX = 0
        source_time_zone = pytz.timezone("Asia/Tokyo")
        reader = csv.DictReader(file)
        for row in reader:
            data = (row['MON'], row['DAY'], row['URL'], row['HR'], row['MN'], row['NAME'], row['LIVE'])  # MON,DAY,ID,HR
            # ,MN,NAME, LIVE
            source_mon = data[0]
            source_day = data[1]
            source_link = '[Link](' + data[2] + ')'
            source_hour = data[3]
            source_min = data[4]
            source_time = datetime(int(self.now.year), int(source_mon), int(source_day), int(source_hour),
                                   int(source_min), 00, 0000)
            source_date_with_timezone = source_time_zone.localize(source_time)
            val = self.time_left(source_date_with_timezone)
            target_time_zone = pytz.timezone(time_z)
            writer = source_date_with_timezone.astimezone(target_time_zone)
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
        print(link_list)
        return link_list, table

    @classmethod
    def start_reading(cls, file_content):
        day_list = []
        hold = [0, 0]
        ms = 0
        live = ''
        return_f = []
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
        print('\n\n')
        return_f.append('MON,DAY,URL,HR,MN,NAME,LIVE\n')
        for k in range(0, len(containers_link)):
            match = re.findall(r'href=\"(https:[//]*www\.youtube\.com/watch\?v=[0-9A-Za-z_-]{10}[048AEIMQUYcgkosw]*)\"',
                               str(containers_link[k]))[0]
            match_S = re.findall(r'border:( 3px red solid| 0)',
                                 str(containers_link[k]))[0]
            if match_S == ' 3px red solid':
                live = "LIVE"
            else:
                live = "NOT"
            cls.list_url.append(match)
            time_name = containers_link[k].text.replace(' ', '').split()
            hr = time_name[0].split(':')
            if int(hr[0]) != 23 and int(hr[1]) <= 59 and hold[0] == 23:
                ms += 1
                return_f.append('{},{},{},{},{},{},{}{}'.format(day_list[ms][0], day_list[ms][1],
                                                                match,
                                                                hr[0], hr[1], time_name[1], live, '\n'))
                hold = [int(hr[0]), int(hr[1])]
            else:
                return_f.append('{},{},{},{},{},{}{}'.format(day_list[ms][0], day_list[ms][1],
                                                             match,
                                                             hr[0], hr[1], time_name[1], live, '\n'))
                hold = [int(hr[0]), int(hr[1])]
        return return_f

    @classmethod
    def video_details(cls, video):
        details = []
        for vid in video:
            params = {"format": "json", "url": vid}
            url = "https://www.youtube.com/oembed"
            query_string = parse.urlencode(params)
            url = url + "?" + query_string
            with request.urlopen(url) as response:
                response_text = response.read()
                data = json.loads(response_text.decode())
                details.append([vid, data['title'], data['thumbnail_url']])
        return details

    def time_left(self, full_inp):
        self.now = datetime.now()
        target_time_zone = pytz.timezone('Asia/Kolkata')
        target_date_with_timezone = self.now.astimezone(target_time_zone)
        left = full_inp - target_date_with_timezone
        return left

    @classmethod
    def translate_export(cls, file, orig, tran):
        dict_name = {}
        for ele in range(len(orig)):
            dict_name[orig[ele].strip()] = tran[ele].strip()
        for key, val in dict_name.items():
            for idx, ele in enumerate(file):
                if key in ele:
                    file[idx] = ele.replace(key, val)
        return file

    @classmethod
    def check_live(cls, vid):
        pg = requests.get(vid).content
        pg_soup = _soup_(pg, "html.parser")
        viewers = pg_soup.find_all('div', class_="view-count style-scope yt-view-count-renderer")
        print(viewers)
        if viewers:
            return True
        else:
            return False

    def update(self):
        self.now = datetime.now()
        self.checked_f = requests.get('https://schedule.hololive.tv/').content  # reads data from site
        self.data = self.start_reading(self.checked_f)  # parses it
        self.trans_d = self.translate_export(self.data, self.names_o, self.names_trs)  # translates it
        self.list_of_titles_and_thumbs = self.video_details(self.list_url)