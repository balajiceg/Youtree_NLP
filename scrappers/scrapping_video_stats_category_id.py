import csv
import json
import requests
import time
categoryIDfd = open('../datasets/categoryID.csv', 'r')
categoryIDBridge = csv.DictReader(categoryIDfd)

videostat1milfd = open('../datasets/videoStats1Mil.csv', 'w')
headers = ("videoId", "channelId")
videostat1milbridge = csv.DictWriter(videostat1milfd, headers)
videostat1milbridge.writeheader()
nextPageToken = ""
for data in categoryIDBridge:
    nextPageToken = ""
    flag = 0
    for i in range(0,3125):
        if flag == 1:
            print("Inside flag = 1")
            break
        ids = {}
        payload = "https://www.googleapis.com/youtube/v3/search?key=AIzaSyDraPMr8KRfkux5u9DgCjfWh1SA_xJmIl8" \
                  "&type=video&part=snippet&videoCategoryID="+data['categoryID']+\
                  "&maxResults=50&pageToken="+nextPageToken
        r = requests.get(payload)
        videoDataRaw = r.json()

        print(videoDataRaw)
        videoDataAll = videoDataRaw["items"]
        if not videoDataAll:
            print("Inside videoDataAll")
            flag = 1
        for videoData in videoDataAll:
            ids = {}
            if "videoId" in videoData["id"].keys() and "channelId" in videoData["snippet"].keys():
                ids["videoId"] = videoData["id"]["videoId"]
                ids["channelId"] = videoData["snippet"]["channelId"]
                videostat1milbridge.writerow(ids)
                print(ids)

        if "nextPageToken" in videoDataRaw.keys():
            nextPageToken = videoDataRaw["nextPageToken"]
        else:
            pass
        time.sleep(5)


