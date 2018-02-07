import csv
import json

videostatbridge = open('../datasets/dislikesbyview.csv', 'r')
top20headings = ("videoId", "dislikes/view")

videoStats = csv.DictReader(videostatbridge)

allVideoRequiredList = []
impDataDict = {}
for videoStat in videoStats:
    impDataDict = {}
    impDataDict["videoId"] = videoStat["videoId"]
    impDataDict["dislikes/view"] = float(videoStat["dislikes/view"])
    allVideoRequiredList.append(impDataDict)

#print(allVideoRequiredList)
sortedAllVideoList = sorted(allVideoRequiredList, key=lambda k:k['dislikes/view'], reverse=True)
#print(sortedAllVideoList)

top20videos = sortedAllVideoList[:21]

top20csvfile = open("../datasets/top20dislikesbyviews.csv", "w")
top20filebridge = csv.DictWriter(top20csvfile, top20headings)
top20filebridge.writeheader()
for row in top20videos:
    top20filebridge.writerow(row)