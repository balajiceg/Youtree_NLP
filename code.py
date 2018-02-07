import json
import numpy as np

# 'videoId'
# 'likes/views'
# 'dislikes/views'
# 'comments/views'
# 'views/subscribers'
# 'totviews/totsubs'
# 'totvideos/videocount'
# 'elapsedtime'
# 'views/elapsedtime'
# 'comments/subscriber'
# 'dislikes/subscriber'
# 'likes/subscriber'
# 'totalviews/channelelapsedtime'

#writing subset for test purpose
# with open('test_dat.json', 'w') as outfile:
#     json.dump(data[:10000], outfile)

data_file='YouTubeDataset_withChannelElapsed.json'

# data_file='test_dat.json'

no_intervals=10





def get_bins(data, intervals=[]):
    if intervals ==[]:
        intervals.append(np.amax(data))

    if len(intervals) >= no_intervals:
        return intervals[::-1]

    hist, bins = np.histogram(data,no_intervals, range=(0, intervals[-1]))
    hist = hist / nos_videos
    last = 0
    done=False
    for i in reversed(range(1, no_intervals)):
        last += hist[i]
        if last >= 0.1:
            intervals.append(bins[i])
            return (get_bins(data, intervals))
            done=True
    if not done:
        intervals.append(bins[1])
        return (get_bins(data, intervals))



with open(data_file) as data_file:
    videos = json.load(data_file)

nos_videos=len(videos)

features=[]
for i,video in enumerate(videos):
    features.append(np.array([video['likes/views'],
                    video['dislikes/views'],
                    video['comments/views'],
                    video['views/subscribers'],
                    video['totviews/totsubs'],
                    video['totvideos/videocount'],
                    video['elapsedtime'],
                    video['views/elapsedtime'],
                    video['comments/subscriber'],
                    video['dislikes/subscriber'],
                    video['likes/subscriber'],
                    video['totalviews/channelelapsedtime']]).astype(np.float))
features=np.array(features)
bins=[]
for i in range(features.shape[1]):
    data=np.copy(features[:,i])
    h,b=np.histogram(data, [0] + get_bins(data, []), range=(0, np.amax(data)))
    bins.append(b.tolist())
    # print(bins)
    # print(np.int16(h*100/nos_videos))
#
with open('bins.json', 'w') as outfile:
     json.dump(bins, outfile)

print(bins)




