import tensorflow as tf
import numpy as np
from subprocess import check_output

import csv

tensorfd = open('../datasets/tensorfiles.csv', 'r')
tensorbridge = csv.reader(tensorfd)


videoIDfd = open('../datasets/tensorVideoID.csv', 'w')
headers = ('videoID', 'Lolcats')
videoIDBridge = csv.DictWriter(videoIDfd,headers)
videoIDBridge.writeheader()
#print(check_output(["ls", "../datasets/YTDS"]).decode("utf-8"))
#exit()
videoids = []
count = 0
for data in tensorbridge:
    videodata_file = data[0]
    path = '../datasets/YTDS/'+videodata_file
    for example in tf.python_io.tf_record_iterator(path=path):
        videoIDDict = {}
        video_data = tf.train.Example.FromString(example)
        print("This record is sexy! <3")
        videoids.append(video_data.features.feature['video_id'].bytes_list.value[0].decode(encoding="UTF-8"))
        videoIDDict[headers[0]] = video_data.features.feature['video_id'].bytes_list.value[0].decode(encoding="UTF-8")
        videoIDDict[headers[1]] = "lolcats"
        videoIDBridge.writerow(videoIDDict)
        if count % 100 == 0:
            print(count)
        count = count + 1




