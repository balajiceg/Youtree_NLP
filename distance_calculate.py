import json
import numpy as np
import warnings
import pandas as pd

import timeit

start = timeit.default_timer()


video_id='4fndeDfaWCg'

top_k=50

##############################################################
no_intervals=10 #bins

data_file='test_dat.json'
data_file='YouTubeDataset_withChannelElapsed.json'

np.set_printoptions(precision=2,threshold=np.nan)
no_intervals=10

with open(data_file) as data_file:
    videos = json.load(data_file)
    videos=videos[:]

with open("sorted_video_ids.json") as data_file:
    videos_id_filter = json.load(data_file)
    


with open('bin_id_vectors.json') as data_file:
    bin_id_vectors = json.load(data_file)

bin_id_vectors=np.array(bin_id_vectors,dtype=np.int32)
bin_id_vectors=bin_id_vectors[:len(videos)]


video_ids=[]
for video in videos:
    video_ids.append(video['videoId'])
pos=video_ids.index(video_id)



filter_inds=[]
for i in videos_id_filter:
    filter_inds.append(video_ids.index(i[:-4]))



video_ids=np.array(video_ids)
target_vector=bin_id_vectors[pos]
if not np.all(target_vector) :
    warnings.warn("Some attributes of given videos is missing in data")
distances=[]

print("ok")

for i,vector in enumerate(bin_id_vectors):
    if np.all(vector):
        distances.append(np.sum(np.abs(vector-target_vector)))
    else :
        distances.append(no_intervals*len(vector)+1)

distances=np.array(distances,dtype=np.uint32)



sorted_video_ids = video_ids[filter_inds]
sorted_distances = distances[filter_inds]

inds = sorted_distances.argsort()

sorted_video_ids = sorted_video_ids[inds]
sorted_distances = sorted_distances[inds]

sorted_video_ids=sorted_video_ids[:top_k]
sorted_distances = sorted_distances[:top_k]

merged=[]
for id,distance in zip(sorted_video_ids,sorted_distances):
    if distance==no_intervals*len(vector)+1:
        distance='Nan'
    merged.append([video_id,id,distance])

#print(merged)
merged = pd.DataFrame(merged,columns = ['givenVideo','comparedVideo','distance'])
merged.to_csv('top'+video_id+'.csv',index=False)
print("completed")



stop = timeit.default_timer()

print (stop - start )





import mraa
u=mraa.Uart(0)

# Set UART parameters
u.setBaudRate(9600)
u.setMode(8, mraa.UART_PARITY_NONE, 1)
u.setFlowcontrol(False, False)

# Start a neverending loop waiting for data to arrive.
# Press Ctrl+C to get out of it.
while True:
  if u.dataAvailable():
    # We are doing 1-byte reads here
    string=""
    c=u.readStr(1)
    if(c=='$')
        string=""
    if(c=='\n')
        print string