import csv
import json

videostatbridge = open('../datasets/videoStats.csv', 'r')
top20headings = ("videoId", "dislikeCount")

videoStats = csv.DictReader(videostatbridge)

allVideoRequiredList = []
impDataDict = {}
for videoStat in videoStats:
    impDataDict = {}
    impDataDict["videoId"] = videoStat["videoId"]
    impDataDict["dislikeCount"] = int(videoStat["dislikeCount"])
    allVideoRequiredList.append(impDataDict)

#print(allVideoRequiredList)
sortedAllVideoList = sorted(allVideoRequiredList, key=lambda k:k['dislikeCount'], reverse=True)
#print(sortedAllVideoList)

top20videos = sortedAllVideoList[:21]

top20csvfile = open("../datasets/top20dislikes.csv", "w")
top20filebridge = csv.DictWriter(top20csvfile, top20headings)
top20filebridge.writeheader()
for row in top20videos:
    top20filebridge.writerow(row)