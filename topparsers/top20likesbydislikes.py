import csv
import json

videostatbridge = open('../datasets/likesbydislikes.csv', 'r')
top20headings = ("videoId", "likes/dislikes")

videoStats = csv.DictReader(videostatbridge)

allVideoRequiredList = []
impDataDict = {}
for videoStat in videoStats:
    impDataDict = {}
    impDataDict["videoId"] = videoStat["videoId"]
    impDataDict["likes/dislikes"] = float(videoStat["likes/dislikes"])
    allVideoRequiredList.append(impDataDict)

#print(allVideoRequiredList)
sortedAllVideoList = sorted(allVideoRequiredList, key=lambda k:k['likes/dislikes'], reverse=True)
#print(sortedAllVideoList)

top20videos = sortedAllVideoList[:21]

top20csvfile = open("../datasets/top20likesbydislikes.csv", "w")
top20filebridge = csv.DictWriter(top20csvfile, top20headings)
top20filebridge.writeheader()
for row in top20videos:
    top20filebridge.writerow(row)