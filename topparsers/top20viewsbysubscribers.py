import csv
import json

channelstatbridge = open('../datasets/viewsbysubscribers.csv', 'r')
top20headings = ("videoId", "views/subscribers")

channelStats = csv.DictReader(channelstatbridge)

allChannelRequiredList = []
impDataDict = {}
for channelStat in channelStats:
    impDataDict = {}
    impDataDict["videoId"] = channelStat["videoId"]
    impDataDict["views/subscribers"] = float(channelStat["views/subscribers"])
    allChannelRequiredList.append(impDataDict)

#print(allVideoRequiredList)
sortedAllChannelList = sorted(allChannelRequiredList, key=lambda k:k['views/subscribers'], reverse=True)
#print(sortedAllVideoList)

top20channel = sortedAllChannelList[:21]

top20csvfile = open("../datasets/top20viewsbysubscribers.csv", "w")
top20filebridge = csv.DictWriter(top20csvfile, top20headings)
top20filebridge.writeheader()
for row in top20channel:
    top20filebridge.writerow(row)
