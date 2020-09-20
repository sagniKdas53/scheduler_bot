import re
from bs4 import BeautifulSoup as _soup_


def start_reading(file):
    day_list = []
    hold = [0, 0]
    ms = 0
    f = open(file)  # simplified for the example (no urllib)
    flip_soup = _soup_(f, "html.parser")
    f.close()
    containers_date = flip_soup.find_all('div', class_="holodule navbar-text")
    containers_link = flip_soup.find_all('a', class_="thumbnail")
    for dates in containers_date:
        day = dates.text.strip().replace(' ', '').split()
        day_list.append(day[0].split('/'))
    print("Schedule contains: ")
    for month,day in day_list:
        print("{}/{},".format(month,day),end='')
    f = open("export.csv", "w", encoding='utf8')
    f.write('MON,DAY,ID,HR,MN,NAME\n')
    for k in range(0, len(containers_link)):
        match = re.findall(r'href="https:[//]*www\.youtube\.com/watch\?v=([0-9A-Za-z_-]{10}[048AEIMQUYcgkosw]*)',
                           str(containers_link[k]))[0]
        time_name = containers_link[k].text.replace(' ', '').split()
        hr = time_name[0].split(':')
        if int(hr[0]) != 23 and int(hr[1]) <= 59 and hold[0] == 23:
            ms += 1
            f.write('{},{},{},{},{},{}{}'.format(day_list[ms][0], day_list[ms][1],
                                                 match,
                                                 hr[0], hr[1], time_name[1], '\n'))
            hold = [int(hr[0]), int(hr[1])]
        else:
            f.write('{},{},{},{},{},{}{}'.format(day_list[ms][0], day_list[ms][1],
                                                 match,
                                                 hr[0], hr[1], time_name[1], '\n'))
            hold = [int(hr[0]), int(hr[1])]
    f.close()
