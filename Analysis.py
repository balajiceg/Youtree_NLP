
from sklearn.feature_extraction.text import TfidfVectorizer
from scipy import spatial
from os import listdir
from os.path import isfile, join
import json

print("starting")
dir="/home/idiot/Desktop/Youtube-View-Predictor/datasets/8mcsvs/8mcombined/"

video_id="4fndeDfaWCg"

files_in_dir = [f for f in listdir(dir) if isfile(join(dir, f))]
path = dir+"/"
each_profile_data = []
ue=0
for file in files_in_dir:
    dat=""
    with open(path + file, 'r', encoding="utf8") as f:
        try:
            for line in f:
                dat += str(line)
        except UnicodeDecodeError:
                ue+=1
    each_profile_data.append(dat)

print("skipped:"+str(ue))


print(str(len(files_in_dir))+" files")
# for i in files_in_dir:
#     print(i)
print("data loaded...")

corpus = each_profile_data

print(len(corpus))
print(len(files_in_dir))

#print(corpus)

n_of_articles = corpus.__len__()
vectorizer = TfidfVectorizer(min_df=1)
vectorizer.__init__(norm=u'l1', smooth_idf=False)

X = vectorizer.fit_transform(corpus)


feature_names = vectorizer.get_feature_names()
scores_relative_to_comparing = []
ss = []
doc = files_in_dir.index(video_id+".txt")

print("video found....")

print(video_id+"  "+str(doc))
feature_index = X[doc, :].nonzero()[1]


# writer = open('idf.txt', 'w', encoding="utf8")
# for i in range(vectorizer.idf_.__len__()):
#     writer.write(str(vectorizer.idf_[i]))
#     writer.write(" ")
#     writer.write(str(feature_names[i]))
#     writer.write("\n")
# writer.close()

c = files_in_dir

print("printing idf done....")

cc=0

for tt in range(n_of_articles):
    # writer = open('query_' + str(c[cc]), 'w', encoding="utf8")
    tfidf_scores = zip(feature_index, [X[tt, x] for x in feature_index])

    ss = []
    for w, s in [(feature_names[i], s) for (i, s) in tfidf_scores]:
        ss.append(s)
        # writer.write(w)
        # writer.write(" ")
        # writer.write(str(s))
        # writer.write("\n")
    if cc%1000==0:print("scores:" + str(cc) + " of " + str(n_of_articles))
    cc += 1
    scores_relative_to_comparing.append(ss)
# writer.close()

print("scores computed... :)")

with open('scores.json', 'w') as outfile:
    json.dump(scores_relative_to_comparing, outfile)


c = 0
distance_txt=""

distance_txt+="The file contains distance and similarity of the query profile and corpus consecutively \n"
for i in range(n_of_articles):
    result = 1 - (spatial.distance.cosine(scores_relative_to_comparing[doc], scores_relative_to_comparing[i]))
    distance_txt+="Between document "+str(files_in_dir[doc][:-4])+ " and " + str(files_in_dir[c][:-4]) + " "
    distance_txt+=str(1 - result) + " "
    distance_txt+=str(result)
    distance_txt+="\n"
    c += 1
    if i%1000==0:print("distance:"+str(i)+" of "+str(n_of_articles))
writer = open('distance.txt', 'w', encoding="utf8")
writer.write(distance_txt)

del distance_txt
writer.close()
print("Distance file completed...")



def get_scores():
    return scores_relative_to_comparing
