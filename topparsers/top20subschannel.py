import csv
import json

channelstatbridge = open('../datasets/channelStats.csv', 'r')
top20headings = ("channelId", "subscriberCount")

channelStats = csv.DictReader(channelstatbridge)

allChannelRequiredList = []
impDataDict = {}
for channelStat in channelStats:
    impDataDict = {}
    impDataDict["channelId"] = channelStat["channelId"]
    impDataDict["subscriberCount"] = int(channelStat["subscriberCount"])
    allChannelRequiredList.append(impDataDict)

#print(allVideoRequiredList)
sortedAllChannelList = sorted(allChannelRequiredList, key=lambda k:k['subscriberCount'], reverse=True)
#print(sortedAllVideoList)

top20channel = sortedAllChannelList[:21]

top20csvfile = open("../datasets/top20channels.csv", "w")
top20filebridge = csv.DictWriter(top20csvfile, top20headings)
top20filebridge.writeheader()
for row in top20channel:
    top20filebridge.writerow(row)