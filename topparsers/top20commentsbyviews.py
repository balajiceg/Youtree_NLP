import csv
import json

videostatbridge = open('../datasets/commentsbyviews.csv', 'r')
top20headings = ("videoId", "comments/views")

videoStats = csv.DictReader(videostatbridge)

allVideoRequiredList = []
impDataDict = {}
for videoStat in videoStats:
    impDataDict = {}
    impDataDict["videoId"] = videoStat["videoId"]
    impDataDict["comments/views"] = float(videoStat["comments/views"])
    allVideoRequiredList.append(impDataDict)

#print(allVideoRequiredList)
sortedAllVideoList = sorted(allVideoRequiredList, key=lambda k:k['comments/views'], reverse=True)
#print(sortedAllVideoList)

top20videos = sortedAllVideoList[:21]

top20csvfile = open("../datasets/top20commentsbyviews.csv", "w")
top20filebridge = csv.DictWriter(top20csvfile, top20headings)
top20filebridge.writeheader()
for row in top20videos:
    top20filebridge.writerow(row)