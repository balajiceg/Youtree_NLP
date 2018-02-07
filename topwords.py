import Analysis
import math
import json
import heapq
import numpy as np

top_k=1000


#############################

word_list = []

avg = sum(Analysis.vectorizer.idf_) / Analysis.vectorizer.idf_.__len__()
scores = Analysis.get_scores()

print("Analysis done....")

writer1 = open('scores.txt', 'w', encoding="utf8")
writer = open('words.txt', 'w', encoding="utf8")


def cosine_similarity(v1, v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]
        y = v2[i]
        sumxx += x * x
        sumyy += y * y
        sumxy += x * y

    # word_list[:]=[i/math.sqrt(sumxx*sumyy) for i in word_list]
    return sumxy / math.sqrt(sumxx * sumyy)


def word_list_writer(index):
    v1 = score_query
    v2 = scores[index]
    for i in range(v1.__len__()):
        val = v1[i] * v2[i]
        den = abs((v1[i] - v2[i]))
        idf = Analysis.vectorizer.idf_[Analysis.feature_index[i]]
        # if (val):
        #     word_list.append(idf / val)
        # else:
        #     word_list.append(idf / (den))v
        if (val):
            word_list.append(idf * val)
            # elif (den):
            #    word_list.append(idf / (den))
        else:
            word_list.append(0)
    writer1.write(str(word_list))
    writer1.write("\n newprofile \n")


def print_max_5_words(K):
    a = np.array(K)
    indices = heapq.nlargest(20, range(len(a)), a.take)
    # print(Analysis.feature_names[Analysis.feature_index[K.index(max(K))]])
    tmp_str=""
    for i in indices:
        true_max_index = Analysis.feature_index[i]
        # if(K[i] >0):
        # print(Analysis.feature_names[true_max_index])
        tmp_str+=str(Analysis.feature_names[true_max_index])
        tmp_str+=" "
        tmp_str+=str(K[i])
        tmp_str+="\n"
    writer.write(tmp_str)
    del word_list[:]


def merge(v1, v2):
    v3 = []
    for i in range(v1.__len__()):
        v3.append(max(v1[i], v2[i]))
    return v3


# scores=[[1.1,1.1],[1.25,1.25],[1.45,1.45],[2,2],[2.5,2.3],[4,5]]
query_index = Analysis.doc
score_query = [x for x in scores[query_index]]
score_dup = [x for x in scores]

c = 0
mergers = []
dist_list = []

distances = []
max = 1

for i in range(scores.__len__()):
    try:
        a = scores[i]
    except IndexError:
        distances.append(max)
        continue
    dist = 1 - cosine_similarity(score_query, scores[i])
    if str(dist) == 'nan':
        distances.append(max)
        continue
    distances.append(dist)

distances=np.array(distances)
scores=np.array(scores)
Analysis.files_in_dir=np.array(Analysis.files_in_dir)
inds = distances.argsort()
Analysis.files_in_dir = Analysis.files_in_dir[inds]
distances = distances[inds]
scores=scores[inds]
scores=scores.tolist()

print("Distances sorted...")


for i in range(top_k):
    print(str(i+1)+" "+Analysis.files_in_dir[i][:-4])
    try:
        a = scores[i]
    except IndexError:
        continue
    dist = 1 - cosine_similarity(score_query, scores[i])
    writer.write(Analysis.files_in_dir[i][:-4] + " top impact words")
    writer.write(str(i))
    writer.write("\n")
    word_list_writer(i)
    print_max_5_words(word_list)
    writer.write("\n\n")

with open('sorted_video_ids.json', 'w') as outfile:
    json.dump(Analysis.files_in_dir.tolist()[:top_k], outfile)

writer.close()
writer1.close()