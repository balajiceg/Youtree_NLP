import csv
import json

videostatbridge = open('../datasets/videoStats.csv', 'r')
top20headings = ("videoId", "viewCount")

videoStats = csv.DictReader(videostatbridge)

allVideoRequiredList = []
impDataDict = {}
for videoStat in videoStats:
    impDataDict = {}
    impDataDict["videoId"] = videoStat["videoId"]
    impDataDict["viewCount"] = int(videoStat["viewCount"])
    allVideoRequiredList.append(impDataDict)

#print(allVideoRequiredList)
sortedAllVideoList = sorted(allVideoRequiredList, key=lambda k:k['viewCount'], reverse=True)
#print(sortedAllVideoList)

top20videos = sortedAllVideoList[:20]

top20csvfile = open("../datasets/top20views.csv", "w")
top20filebridge = csv.DictWriter(top20csvfile, top20headings)
top20filebridge.writeheader()
for row in top20videos:
    top20filebridge.writerow(row)