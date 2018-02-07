
from sklearn.feature_extraction.text import TfidfVectorizer
from os import listdir
from os.path import isfile, join


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


writer = open('idf.txt', 'w', encoding="utf8")
tmp_str=""
for i in range(vectorizer.idf_.__len__()):
    tmp_str+=str(vectorizer.idf_[i])
    tmp_str+=" "
    tmp_str+=str(feature_names[i])
    tmp_str+="\n"
    if i % 100 == 0: print("idf:" + str(i) + " of " + str(vectorizer.idf_.__len__()))
print("writing....")
writer.write(tmp_str)
writer.write("\n\nCompleted...")
print("completed")
writer.close()
