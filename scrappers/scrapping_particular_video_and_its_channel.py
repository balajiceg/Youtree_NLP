import requests

def ScrappingVideoDetails(videoId):

    payload = "https://www.googleapis.com/youtube/v3/videos?id=" + videoId + \
              "&key=AIzaSyAjkrSgzR6voSP3ut1Mj1ukkAZ_xYtEC_0&part=snippet,contentDetails,statistics,status"

    ids = {}
    r = requests.get(url=payload)
    videoDataRaw = r.json()

    channelId = videoDataRaw["items"][0]["snippet"]["channelId"]
    payload_channel = "https://www.googleapis.com/youtube/v3/channels?key=AIzaSyDraPMr8KRfkux5u9DgCjfWh1SA_xJmIl8&part=snippet,statistics" \
                "&id="+channelId
    r_channel = requests.get(url=payload_channel)
    channelDataRaw = r_channel.json()
    subscriberCount = channelDataRaw["items"][0]["statistics"]["subscriberCount"]
    print(channelId)

    videoData = videoDataRaw["items"][0]
    if "id" in videoData.keys():
        ids["videoId"] = videoData["id"]
    else:
        ids["videoId"] = "NULL"
    if "publishedAt" in videoData["snippet"].keys():
        ids["publishTime"] = videoData["snippet"]["publishedAt"]
    else:
        ids["publishTime"] = "lolcats"
    if "categoryId" in videoData["snippet"].keys():
        ids["categoryId"] = videoData["snippet"]["categoryId"]
    else:
        ids["categoryId"] = "-1"

    if "viewCount" in videoData["statistics"].keys():
        ids["viewCount"] = videoData["statistics"]["viewCount"]
    else:
        ids["viewCount"] = "-1"

    if "likeCount" in videoData["statistics"].keys():
        ids["likeCount"] = videoData["statistics"]["likeCount"]
    else:
        ids["likeCount"] = "-1"

    if "dislikeCount" in videoData["statistics"].keys():
        ids["dislikeCount"] = videoData["statistics"]["dislikeCount"]
    else:
        ids["dislikeCount"] = "-1"

    if "favoriteCount" in videoData["statistics"].keys():
        ids["favouriteCount"] = videoData["statistics"]["favoriteCount"]
    else:
        ids["favouriteCount"] = "-1"

    if "commentCount" in videoData["statistics"].keys():
        ids["commentCount"] = videoData["statistics"]["commentCount"]
    else:
        ids["commentCount"] = "-1"

    required_data = [int(ids["commentCount"]), int(ids["dislikeCount"]), int(ids["viewCount"]),
                     float(int(ids["viewCount"]) / int(subscriberCount))]

    #print(required_data)
    return required_data


if __name__ == '__main__':
    ScrappingVideoDetails("ABMLDdaopbk")
