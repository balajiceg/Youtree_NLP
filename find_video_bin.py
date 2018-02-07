import json
import numpy as np

data_file='YouTubeDataset_withChannelElapsed.json'

#data_file='test_dat.json'
np.set_printoptions(precision=2,threshold=np.nan)
no_intervals=10

with open(data_file) as data_file:
    videos = json.load(data_file)
    videos=videos[:]

with open('bins.json') as data_file:
    bins = json.load(data_file)
bins=np.array(bins)
nos_videos=len(videos)

v_features=[]
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
v_features=np.array(v_features)

bin_id_vectors=np.zeros(shape=(nos_videos,v_features.shape[1]),dtype=np.uint16)
for i,v_feature in enumerate(v_features):
    for j,feature in enumerate(v_feature):
        if feature<0:
            break

        for k in range(bins.shape[1]-1):
            if(feature>=bins[j,k] and feature<bins[j,k+1] ):
                bin_id_vectors[i, j] = k+1
                break

        if(feature==bins[j,bins.shape[1]-1]) :bin_id_vectors[i,j]=bins.shape[1]-1


with open('bin_id_vectors.json', 'w') as outfile:
    json.dump(bin_id_vectors.tolist(), outfile)


