import os

commments_dir="/home/idiot/Desktop/Youtube-View-Predictor/datasets/8mcsvs/8mcomments/"

des_dir="/home/idiot/Desktop/Youtube-View-Predictor/datasets/8mcsvs/8mdescriptions/"

output_dir="/home/idiot/Desktop/Youtube-View-Predictor/datasets/8mcsvs/8mcombined/"

writer=open('errors.txt', 'w', encoding="utf8")

count=0
for i in [i for j in (range(1,23), range(77,88)) for i in j]:
    for f in os.listdir(commments_dir+"totalComments"+str(i)):
        count += 1
        if count<=542951:continue
        try:
            print(count)
            open(output_dir+ f, "w").writelines([l for l in open(des_dir +"totalStat"+str(i)+"/"+f.split('.')[0]+"_desc.txt").readlines()]+
                ["\n"] + [l for l in open(commments_dir +"totalComments"+str(i)+"/"+f).readlines()])
        except OSError as e:
            writer.write(str(count)+"\n")
            print("error:"+str(count))

print("completed")

writer.close()