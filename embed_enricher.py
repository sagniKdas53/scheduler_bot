import json
import pprint
from urllib import request, parse


# change to yours VideoID or change url inparams
# VideoID = "A67ZkAd1wmI"


def video_details(vid):
    params = {"format": "json", "url": vid}
    url = "https://www.youtube.com/oembed"
    query_string = parse.urlencode(params)
    print(query_string)
    url = url + "?" + query_string
    print(url)
    details = []
    with request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        pprint.pprint(data)
        details = [data['title'], data['thumbnail_url']]
    return details


str = '[Link](https://www.youtube.com/watch?v=8kxthB-jp_Y)'
print(video_details(str[7:-1]))
stt = 'https://www.youtube.com/watch?v=NJkQzZOdOsI'
print(video_details(stt))
