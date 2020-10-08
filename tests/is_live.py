"""
data:
FBK : https://www.youtube.com/channel/UCdn5BQ06XqgXoAxIhbqw5Rg [Live]:datetime.datetime(2020, 10, 8, 20, 18, 40, 826442)
Kiara : https://www.youtube.com/channel/UCHsx4Hqa-1ORjQTh9TYDhww [will go live in 10 minutes]
<span class="view-count style-scope yt-view-count-renderer">12,496 watching now</span> This can be used to get but this
will slow it sown significantly

possible workaround is to check only the last 3 url's or the ones within +-4 hours of check but it won't work for Korone
and her 9+ hours streams
"""
import re

import requests
from bs4 import BeautifulSoup as _soup_


# from working_bot_newer import ExecFaster

# this ain't gonna work
def check_live(vid):
    pg = requests.get(vid).content
    pg_soup = _soup_(pg, "html.parser")
    viewers = pg_soup.find_all('div', class_="style-scope ytd-video-primary-info-renderer")
    print(viewers)
    if viewers:
        return True
    else:
        return False


FBK = "https://www.youtube.com/channel/UCdn5BQ06XqgXoAxIhbqw5Rg"
'''pg = requests.get('https://schedule.hololive.tv/').content  # reads data from site
with open("bkp.html", 'w') as bk:
    bk.writelines(str(pg))'''
pg = open('bkp.html', 'r')
flip_soup = _soup_(pg, "html.parser")
containers_link = flip_soup.find_all('a', class_="thumbnail")
for k in range(0, len(containers_link)):
    match_S = re.findall(r'border:( 3px red solid| 0)',
                         str(containers_link[k]))[0]
    match = re.findall(r'href=\"(https:[//]*www\.youtube\.com/watch\?v=[0-9A-Za-z_-]{10}[048AEIMQUYcgkosw]*)\"',
                       str(containers_link[k]))[0]
    if match_S == ' 3px red solid':
        print(match + "  LIVE")
    else:
        print(match + "  !LIVE")

"""
LIVE::
<a href="https://www.youtube.com/watch?v=C4SHRcuOS5Y" class="thumbnail" target="_blank" style="color:#212529;border-radius: 4px;box-shadow: 0 0 4px rgba(0,0,0,0.4);margin-bottom: 5px;margin-top:5px;
                  border: 3px red solid;
                  " onclick="gtag('event','movieClick',{'event_category':'白上フブキ','event_label':'https://www.youtube.com/watch?v=C4SHRcuOS5Y','value':1});">

        <div class="container" style="padding:1px;">
            <div class="row" style="width:100%;margin:0;">
                <div class="col-12 col-sm-12 col-md-12" style="padding:0;">
                    <div class="row no-gutters">
                        <div class="col-5 col-sm-5 col-md-5 text-left datetime" style="line-height:30px;">
                            <img src="https://schedule.hololive.tv/dist/images/icons/youtube.png" style="vertical-align:middle;position: relative;top:-0.1em; width:17px;height:17px;">
                            19:27
                        </div>
                        <div class="col text-right name" style="line-height:30px;margin-right:5px;">
                                                            白上フブキ
                                                    </div>
                    </div>
                </div>
                <div class="col-12 col-sm-12 col-md-12" style="padding:0 0 5px 0;text-align: center;">
                                            <img src="https://img.youtube.com/vi/C4SHRcuOS5Y/mqdefault.jpg" style="box-shadow: 0 0 5px 5px black inset;">
                                    </div>
                <div class="col-12 col-sm-12 col-md-12" style="padding:0;">
                    <div class="row no-gutters justify-content-between" style="height: 60px;overflow: hidden;">
                        <div class="col col-sm col-md col-lg col-xl" style="width:60px;text-align: center;">
                            <img src="https://yt3.ggpht.com/a/AGF-l7-oeSvjxgdwMoDyT1LMH8nyqkWJCZH8MAOjzg=s88-c-k-c0xffffffff-no-rj-mo" style="border-radius: 50%;width: 60px;border: 2px #43bfef solid;">
                        </div>
                                                                                                </div>
                </div>
            </div>
        </div>
    </a>
    
NOT LIVE::
<a href="https://www.youtube.com/watch?v=BQUnJTQnQHQ" class="thumbnail" target="_blank" style="color:#212529;border-radius: 4px;box-shadow: 0 0 4px rgba(0,0,0,0.4);margin-bottom: 5px;margin-top:5px;
                  border: 0;
                  " onclick="gtag('event','movieClick',{'event_category':'Calli','event_label':'https://www.youtube.com/watch?v=BQUnJTQnQHQ','value':1});">

        <div class="container" style="padding:1px;">
            <div class="row" style="width:100%;margin:0;">
                <div class="col-12 col-sm-12 col-md-12" style="padding:0;">
                    <div class="row no-gutters">
                        <div class="col-5 col-sm-5 col-md-5 text-left datetime" style="line-height:30px;">
                            <img src="https://schedule.hololive.tv/dist/images/icons/youtube.png" style="vertical-align:middle;position: relative;top:-0.1em; width:17px;height:17px;">
                            19:01
                        </div>
                        <div class="col text-right name" style="line-height:30px;margin-right:5px;">
                                                            Calli
                                                    </div>
                    </div>
                </div>
                <div class="col-12 col-sm-12 col-md-12" style="padding:0 0 5px 0;text-align: center;">
                                            <img src="https://img.youtube.com/vi/BQUnJTQnQHQ/mqdefault.jpg" style="box-shadow: 0 0 5px 5px black inset;">
                                    </div>
                <div class="col-12 col-sm-12 col-md-12" style="padding:0;">
                    <div class="row no-gutters justify-content-between" style="height: 60px;overflow: hidden;">
                        <div class="col col-sm col-md col-lg col-xl" style="width:60px;text-align: center;">
                            <img src="https://yt3.ggpht.com/a/AATXAJyQbZx8HMH0-qpLVU-GP21qqkIQ2Lc_InI1nw=s100-c-k-c0xffffffff-no-rj-mo" style="border-radius: 50%;width: 60px;border: 2px #C90D40 solid;">
                        </div>
                                                                                                </div>
                </div>
            </div>
        </div>
    </a>
    
"""
