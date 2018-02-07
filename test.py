import json
import numpy as np
import warnings
import pandas as pd
np.set_printoptions(precision=2,threshold=np.nan)

video_id='--DwgB78t-c'
mvideo_id='7up68liKhsE'


data_file='YouTubeDataset_withChannelElapsed.json'
#data_file='test_dat.json'
no_intervals=10

with open(data_file) as data_file:
    videos = json.load(data_file)


with open('bins.json') as data_file:
    bins = json.load(data_file)
bins=np.array(bins)


with open('bin_id_vectors.json') as data_file:
    abins = json.load(data_file)


v_features=[]
video_ids=[]
for i,video in enumerate(videos):
    v_features.append(np.array([video['likes/views'],
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
    video_ids.append(video['videoId'])
v_features=np.array(v_features)


pos=video_ids.index(video_id)
mpos=video_ids.index(mvideo_id)

print(abins[pos])
print(v_features[pos])

print('\n')

print(abins[mpos])
print(v_features[mpos])

print('\n')
print(bins)

