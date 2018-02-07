import csv

videoStatfd = open('../datasets/8mcsvs/videoStats1.csv', 'r')
videoStatBridge = csv.DictReader(videoStatfd)

headers = ('videoId', 'publishTime', 'categoryId', 'viewCount', 'likeCount', 'dislikeCount',
           'favouriteCount', 'commentCount')
editedVideoStatFD = open('../datasets/8mcsvs/videoStats87_edited.csv', 'w')
editedVideoStatBridge = csv.DictWriter(editedVideoStatFD, headers)
editedVideoStatBridge.writeheader()
count = 0

editVideoDict = {}
for data in videoStatBridge:
    print(data["videoId"])

print("DONE!!!")

