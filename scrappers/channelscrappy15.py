import json
import csv
import requests

#url = "https://www.googleapis.com/youtube/v3/videos?" \
#      "id=7lCDEYXw3mM&key=AIzaSyAjkrSgzR6voSP3ut1Mj1ukkAZ_xYtEC_0&part=snippet,contentDetails,statistics,status"

videoStatsFile = open('../datasets/8mcsvs/videoStats15.csv', 'r')
videoStatsBridge = csv.DictReader(videoStatsFile)
cunt = 0
channelStatsFile = open('../datasets/8mcsvs/8mchannels/channelStats15.csv', 'w')
headers = ("channelId", "videoId", "publishedAt", "viewCount", "commentCount",
           "subscriberCount", "videoCount")
channelStatsBridge = csv.DictWriter(channelStatsFile,headers)
channelStatsBridge.writeheader()
i = 0
donechannels = []
c = 0
for videoStat in videoStatsBridge:
    payload_video = "https://www.googleapis.com/youtube/v3/videos?id=" + videoStat['videoId'] + \
              "&key=AIzaSyD73e0oCduelRXcdSLFQdRGTxRk2z6UiVM&part=snippet"
    r_video = requests.get(payload_video)
    videoData = r_video.json()

    if "items" in videoData.keys():
        if not videoData["items"]:
            print("Inside Channel Data raw")
            continue
    else:
        continue

    channelId = videoData['items'][0]['snippet']['channelId']
    donechannels.append(channelId)
    payload_channel = "https://www.googleapis.com/youtube/v3/channels?key=AIzaSyDV4OZNVdUR55_9od5HmK7xJPKnVeVY1mY" \
                          "&part=snippet,statistics&id="+channelId
    r = requests.get(payload_channel)
    raw_data = r.json()

    if "items" in raw_data.keys():
        if "items" in raw_data.keys():
            if not raw_data["items"]:
                print("Inside Channel Data raw")
                continue
        else:
            continue
    if "items" not in raw_data.keys():
        continue

    dataitem = raw_data["items"]
    details = {}

    details["channelId"] = channelId
    details["videoId"] = videoStat['videoId']

    if "publishedAt" in dataitem[0]["snippet"].keys():
        details["publishedAt"] = dataitem[0]["snippet"]["publishedAt"]
    else:
        details["publishedAt"] = "NULL"

    if "viewCount" in dataitem[0]["statistics"].keys():
        details["viewCount"] = dataitem[0]["statistics"]["viewCount"]
    else:
        details["viewCount"] = -1

    if "commentCount" in dataitem[0]["statistics"].keys():
        details["commentCount"] = dataitem[0]["statistics"]["commentCount"]
    else:
        details["commentCount"] = -1

    if "subscriberCount" in dataitem[0]["statistics"].keys():
        details["subscriberCount"] = dataitem[0]["statistics"]["subscriberCount"]
    else:
        details["subscriberCount"] = -1

    if "videoCount" in dataitem[0]["statistics"].keys():
        details["videoCount"] = dataitem[0]["statistics"]["videoCount"]
    else:
        details["videoCount"] = -1
    i = i + 1
    if i%100 == 0:
        print(i)
    print(details)
    channelStatsBridge.writerow(details)