import json
import urllib.request

# change to yours VideoID or change url inparams
VideoID = "A67ZkAd1wmI"


def video_details(vid):
    params = {"format": "json", "url": "https://www.youtube.com/watch?v=%s" % vid}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string
    details = []
    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        # pprint.pprint(data)
        details.append([data['title'], data['thumbnail_url']])
    return details

# video_details(VideoID)
