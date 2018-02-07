import csv
import glob
import json

files = glob.glob('../datasets/8mcsvs/*.csv')
print(files)
headers = ('videoId', 'publishTime', 'categoryId', 'viewCount', 'likeCount', 'dislikeCount',
           'favouriteCount', 'commentCount')
editedVideoStatFD = open('../datasets/8mcsvs/videoStatsAll.csv', 'w')
editedVideoStatBridge = csv.DictWriter(editedVideoStatFD, headers)
editedVideoStatBridge.writeheader()

count = 0
allVideoList = []
for file in files:
    videoStatFD = open(file,'r')
    videoStatBridge = csv.DictReader(videoStatFD)
    for videoStat in videoStatBridge:
        allVideoList.append(videoStat)
        count = count + 1
        if count % 1000 == 0:
            print(count)

allVideoJSON = json.dumps(allVideoList)
outfile = open('../datasets/videoStatData.json', 'w')
outfile.write(allVideoJSON)