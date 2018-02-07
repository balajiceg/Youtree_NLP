import Analysis
from scipy import spatial
import math
import heapq
import numpy

word_list = []

avg = sum(Analysis.vectorizer.idf_) / Analysis.vectorizer.idf_.__len__()
scores = Analysis.get_scores()

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
    v1=score_query
    v2=scores[index]
    for i in range(v1.__len__()):
     val = v1[i] * v2[i]
     den = abs((v1[i] - v2[i]))
     idf = Analysis.vectorizer.idf_[Analysis.feature_index[i]]
    # if (val):
    #     word_list.append(idf / val)
    # else:
    #     word_list.append(idf / (den))
     if (val):
        word_list.append(idf * val)
    # elif (den):
    #    word_list.append(idf / (den))
     else:
        word_list.append(0)
    writer1.write(str(word_list))
    writer1.write("\n newprofile \n")

def print_max_5_words(K):
    a = numpy.array(K)
    indices=heapq.nlargest(20, range(len(a)), a.take)
    #print(Analysis.feature_names[Analysis.feature_index[K.index(max(K))]])
    for i in indices:
        true_max_index = Analysis.feature_index[i]
        if(K[i] >0):
         print(Analysis.feature_names[true_max_index])
        writer.write(str(Analysis.feature_names[true_max_index]))
        writer.write(" ")
        writer.write(str(K[i]))
        writer.write("\n")
    del word_list[:]

def merge(v1,v2):
    v3=[]
    for i in range(v1.__len__()):
        v3.append(max(v1[i],v2[i]))
    return v3


# scores=[[1.1,1.1],[1.25,1.25],[1.45,1.45],[2,2],[2.5,2.3],[4,5]]
query_index = Analysis.doc
n_of_clusters = scores.__len__()
score_query = [x for x in scores[query_index]]
scores.pop(query_index)
score_dup = [x for x in scores]

c = 0
mergers = []
dist_list = []




for i in range(scores.__len__()):
    dist = 1 - cosine_similarity(score_query, scores[i])
    merge_index=i
    #score_query=merge(score_query,scores[merge_index])
    ind = score_dup.index(scores[merge_index])
    if ind >= query_index:
        mergers.append(ind + 1)
    else:
        mergers.append(ind)

    dind=score_dup.index(scores[merge_index])
    print(dind)
    if dind <query_index:
        print(Analysis.twitterdata.files_in_dir[dind][:-11]+ " top impact words")
        writer.write(Analysis.twitterdata.files_in_dir[dind][:-11]+ " top impact words")
    else:
        print(Analysis.twitterdata.files_in_dir[dind+1][:-11]+" top impact words")
        writer.write(Analysis.twitterdata.files_in_dir[dind+1][:-11]+" top impact words")
    writer.write(str(score_dup.index(scores[merge_index])))
    writer.write("\n")
    word_list_writer(merge_index)
    scores.pop(merge_index)
    print("max impact word")
    print_max_5_words(word_list)
    writer.write("\n\n")
    # max_value = max(word_list)
    # max_index = word_list.index(max_value)
    #print(word_list)
    #print([Analysis.feature_names[i] for i in Analysis.feature_index])

writer.close()
writer1.close()