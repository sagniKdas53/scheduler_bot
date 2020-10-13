import datetime

import pytz


def _generate_output_(dict_data, time_z, name, show_all):
    print('entered')
    table = '{:<5}{:' '^8} {:8}{:<3}:{:<3}'.format('Index', 'Name', 'Status', 'Hour', 'Minute')
    link_list = []
    indX = 0
    source_time_zone = pytz.timezone("Asia/Tokyo")
    for row in dict_data.items():
        # MON,DAY,ID,HR,MN,NAME,LIVE,THUMBNAIL_URL
        print(row)
        source_mon = row['MON']
        source_day = row['DAY']
        source_link = '[Link](' + row['URL'] + ')'
        source_hour = row['HR']
        source_min = row['MN']
        source_stat = row['LIVE']
        source_name = row['NAME']
        source_time = datetime.datetime(int(2020), int(source_mon), int(source_day), int(source_hour),
                                        int(source_min), 00, 0000)
        source_date_with_timezone = source_time_zone.localize(source_time)
        val = time_left(source_date_with_timezone, time_z)
        target_time_zone = pytz.timezone(time_z)
        time_ob = source_date_with_timezone.astimezone(target_time_zone)
        if source_stat == "NOT":
            if name == 'All' or name == source_name:
                if val.days < 0:
                    if show_all:
                        table += '{}{:<5}{:' '^8} {:' '^8}{:>4}:{:<3}'.format('\n', indX, source_name, "OVER",
                                                                              time_ob.hour, time_ob.minute)
                        link_list.append(source_link)
                else:
                    table += '{}{:<5}{:' '^8} {:' '^8}{:>4}:{:<3}'.format('\n', indX, source_name, str(val)[0:7],
                                                                          time_ob.hour, time_ob.minute)
                    link_list.append(source_link)
        elif source_stat == "LIVE":
            if name == 'All' or name == source_name:
                table += '{}{:<5}{:' '^8} {:' '^8}{:>4}:{:<3}'.format('\n', indX, source_name, "LIVE NOW",
                                                                      time_ob.hour, time_ob.minute)
                link_list.append(source_link)
        indX += 1
    print(link_list, table)
    return link_list, table


def time_left(full_inp, target):
    now = datetime.datetime.now()
    target_time_zone = pytz.timezone(target)
    target_date_with_timezone = now.astimezone(target_time_zone)
    left = full_inp - target_date_with_timezone
    return left
