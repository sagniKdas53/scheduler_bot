import json
import pickle as pk
import re
from datetime import datetime
from urllib import request, parse

import pytz
import requests
import time
from bs4 import BeautifulSoup as _soup_


class ExecFaster:
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

    checked_f = None
    data = None
    now = None
    list_url = []
    titles_and_thumbs = {}
    main_storage = {}
    db = {'list_url': list_url, 'titles_and_thumbs': titles_and_thumbs, 'main_storage': main_storage}

    def __init__(self):
        self.now = datetime.now()
        self.checked_f = requests.get('https://schedule.hololive.tv/').content  # reads data from site
        self.start_reading(self.checked_f)  # parses it
        self.video_details(self.list_url)
        self.make_pick()  # only to be used for fast testing
        '''
        self.get_picked()
        '''
        print("Initialized")

    def show_in_time_zone(self, time_x):
        out_pt = self._generate_output_(self.main_storage, time_x, 'show_all',
                                        True)  # takes in export_translated.csv and time zone
        return out_pt  # table of names and status in input time zone.

    def show_by_name(self, name_to_show, time_x, boole):
        print(name_to_show, time_x, boole)
        if boole == 'not_over':
            out_pt = self._generate_output_(self.main_storage, time_x,
                                            name_to_show, False)
        else:
            out_pt = self._generate_output_(self.main_storage, time_x,
                                            name_to_show, True)
        return out_pt  # table of names and status in input time zone.

    '''This function needs some work on it why is it reading all the entries when it clearly knows what to pare and 
    what to not'''

    def _generate_output_(self, dict_data, time_z, name, show_all):
        print('entered')
        table = '{:<5}{:' '^8} {:8}{:<3}:{:<3}'.format('Index', 'Name', 'Status', 'Hour', 'Minute')
        link_list = []
        # times_dict = {}
        indX = 0
        source_time_zone = pytz.timezone("Asia/Tokyo")
        for row in dict_data.items():
            # MON,DAY,ID,HR,MN,NAME,LIVE,THUMBNAIL_URL
            print(row)
            source_mon = row[1]['MON']
            source_day = row[1]['DAY']
            source_link = '[Link](' + row[1]['URL'] + ')'
            source_hour = row[1]['HR']
            source_min = row[1]['MN']
            source_stat = row[1]['LIVE']
            source_name = row[1]['NAME']
            source_time = datetime(int(self.now.year), int(source_mon), int(source_day), int(source_hour),
                                   int(source_min), 00, 0000)
            source_date_with_timezone = source_time_zone.localize(source_time)
            val = self.time_left(source_date_with_timezone, time_z)
            print(source_name, " has ", val, " time left")
            target_time_zone = pytz.timezone(time_z)
            time_ob = source_date_with_timezone.astimezone(target_time_zone)
            if source_stat == "NOT":
                if name == 'All' or name == source_name:
                    if val.days < 0:
                        if show_all:
                            table += '{}{:<5}{:' '^8} {:' '^8}{:' '>4}:{:<3}'.format('\n', indX, source_name, "OVER",
                                                                                     time_ob.hour, time_ob.minute)
                            link_list.append(source_link)
                    else:
                        table += '{}{:<5}{:' '^8} {:' '^8}{:' '>4}:{:<3}'.format('\n', indX, source_name, str(val)[0:7],
                                                                                 time_ob.hour, time_ob.minute)
                        link_list.append(source_link)

            elif source_stat == "LIVE":
                if name == 'All' or name == source_name:
                    table += '{}{:<5}{:' '^8} {:' '^8}{:' '>4}:{:<3}'.format('\n', indX, source_name, "LIVE NOW",
                                                                             time_ob.hour, time_ob.minute)
                    link_list.append(source_link)
            indX += 1
        print(link_list, table)
        return link_list, table

    '''What could be done here is that main storage stores the data as dictionary with the names as the key and the 
    items in the dict could be the '''

    @classmethod
    def start_reading(cls, file_content):
        day_list = []
        hold = [0, 0]
        ms = 0
        flip_soup = _soup_(file_content, "html.parser")
        containers_date = flip_soup.find_all('div', class_="holodule navbar-text")
        containers_link = flip_soup.find_all('a', class_="thumbnail")
        for dates in containers_date:
            day = dates.text.strip().replace(' ', '').split()
            day_list.append(day[0].split('/'))
        print("Schedule contains: ")
        for month, day in day_list:
            print("{}/{},".format(month, day), end='')
        print('\n\n')
        for k in range(0, len(containers_link)):
            match = re.findall(r'href=\"(https:[//]*www\.youtube\.com/watch\?v=[0-9A-Za-z_-]{10}[048AEIMQUYcgkosw]*)\"',
                               str(containers_link[k]))[0]
            match_S = re.findall(r'border:( 3px red solid| 0)',
                                 str(containers_link[k]))[0]
            match_thumb = re.findall(r'https://img\.youtube\.com/vi/[0-9A-Za-z_-]{10}[048AEIMQUYcgkosw]*/',
                                     str(containers_link[k]))[0] + 'hqdefault.jpg'
            # add this to the db, this can be used in embeds later probably won't be
            if match_S == ' 3px red solid':
                live = "LIVE"
            else:
                live = "NOT"
            cls.list_url.append(match)
            time_name = containers_link[k].text.replace(' ', '').split()
            hr = time_name[0].split(':')
            try:
                print('MON:', day_list[ms][0], 'DAY:', day_list[ms][1],
                      'URL:', match,
                      'HR:', hr[0], 'MN:', hr[1], 'NAME:', cls.dict_translated[time_name[1]],
                      'LIVE:', live,
                      'THUMBNAIL_URL:', match_thumb)
            except KeyError:
                print('MON:', day_list[ms][0], 'DAY:', day_list[ms][1],
                      'URL:', match,
                      'HR:', hr[0], 'MN:', hr[1], 'NAME:', time_name[1],
                      'LIVE:', live,
                      'THUMBNAIL_URL:', match_thumb)
            if int(hr[0]) != 23 and int(hr[1]) <= 59 and hold[0] == 23:
                ms += 1
                # MON,DAY,ID,HR,MN,NAME,LIVE,THUMBNAIL_URL
                # return_f.append('MON,DAY,URL,HR,MN,NAME,LIVE,THUMBNAIL_URL\n')
                try:
                    cls.main_storage[match] = {'MON': day_list[ms][0], 'DAY': day_list[ms][1],
                                               'URL': match,
                                               'HR': hr[0], 'MN': hr[1], 'NAME': cls.dict_translated[time_name[1]],
                                               'LIVE': live,
                                               'THUMBNAIL_URL': match_thumb}
                except KeyError:
                    cls.main_storage[match] = {'MON': day_list[ms][0], 'DAY': day_list[ms][1],
                                               'URL': match,
                                               'HR': hr[0], 'MN': hr[1], 'NAME': time_name[1],
                                               'LIVE': live,
                                               'THUMBNAIL_URL': match_thumb}
                hold = [int(hr[0]), int(hr[1])]
            else:
                try:
                    cls.main_storage[match] = {'MON': day_list[ms][0], 'DAY': day_list[ms][1],
                                               'URL': match,
                                               'HR': hr[0], 'MN': hr[1], 'NAME': cls.dict_translated[time_name[1]],
                                               'LIVE': live,
                                               'THUMBNAIL_URL': match_thumb}
                except KeyError:
                    cls.main_storage[match] = {'MON': day_list[ms][0], 'DAY': day_list[ms][1],
                                               'URL': match,
                                               'HR': hr[0], 'MN': hr[1], 'NAME': time_name[1],
                                               'LIVE': live,
                                               'THUMBNAIL_URL': match_thumb}
                hold = [int(hr[0]), int(hr[1])]

    def time_left(self, full_inp, target):
        self.now = datetime.now()
        target_time_zone = pytz.timezone(target)
        target_date_with_timezone = self.now.astimezone(target_time_zone)
        left = full_inp - target_date_with_timezone
        return left

    @classmethod
    def make_pick(cls):
        pk.dump(cls.db, open('pickled_data', 'ab'))

    @classmethod
    def get_picked(cls):
        unpack = open('pickled_data', 'rb')
        cls.db = pk.load(unpack)
        for keys in cls.db:
            print(keys, '=>', cls.db[keys])
        unpack.close()
        print("Unpacked Successfully")

    @classmethod
    def video_details(cls, video):
        for vid in video:
            print(vid)
            params = {"format": "json", "url": vid}
            url = "https://www.youtube.com/oembed"
            query_string = parse.urlencode(params)
            url = url + "?" + query_string
            print(url)
            try:
                with request.urlopen(url) as response:
                    response_text = response.read()
                    data = json.loads(response_text.decode())
                    details = (data['title'], data['thumbnail_url'])
                    print(details)
                    cls.titles_and_thumbs[vid] = details
                    time.sleep(0.1)
                    # max ping is 65.307 ms so it takes 0.065307 seconds to get the response so 100 ms seems good enough
            except Exception as e:
                print(e)
                details = ('ERROR', 'ERROR')
                cls.titles_and_thumbs[vid] = details
        print(cls.titles_and_thumbs)

    def update(self):
        self.now = datetime.now()
        self.checked_f = requests.get('https://schedule.hololive.tv/').content  # reads data from site
        self.start_reading(self.checked_f)  # parses it
        self.video_details(self.list_url)
        self.make_pick()  # only to be used for fast testing
        print("RE-Initialized")
        return True
