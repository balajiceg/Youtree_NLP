import requests
import csv
import json

#url = "https://www.googleapis.com/youtube/v3/channels?part=snippet,statistics&id=UCr-gTfI7au9UaEjNCbnp_Nw" \
      #"&key=AIzaSyD1fGnUYGPjdfpklW9PmjbQkOqlUKxQ3o8"

#r = requests.get(url)
#data = r.json()

headers = ("categoryID", "Title", "channelID")
categoryIDfd = open('../datasets/categoryID.csv', 'w')
categoryIDBridge = csv.DictWriter(categoryIDfd,headers)
categoryIDBridge.writeheader()

payload = "https://www.googleapis.com/youtube/v3/videoCategories?part=snippet&key=AIzaSyD1fGnUYGPjdfpklW9PmjbQkOqlUKxQ3o8" \
          "&regionCode=IN"

r = requests.get(payload)
data = r.json()

categoryDict = {}

for item in data["items"]:
    categoryDict[headers[0]] = item['id']
    categoryDict[headers[1]] = item['snippet']['title']
    categoryDict[headers[2]] = item['snippet']['channelId']
    print(categoryDict)
    categoryIDBridge.writerow(categoryDict)
    #print(item)


