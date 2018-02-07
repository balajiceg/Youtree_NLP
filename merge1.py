import os

commments_dir="/home/idiot/Desktop/Youtube-View-Predictor/datasets/8mcsvs/8mcomments/"

des_dir="/home/idiot/Desktop/Youtube-View-Predictor/datasets/8mcsvs/8mdescriptions/"

output_dir="/home/idiot/Desktop/temp/"

reFiles=[]
with open('er.txt','r') as erfile:
    for l in erfile.readlines():
        print(int(l))
        reFiles.append(int(l))



count=0
for i in [i for j in (range(1,23), range(77,88)) for i in j]:
    for f in os.listdir(commments_dir+"totalComments"+str(i)):
        count += 1
        if count not in reFiles:
            continue
        try:
            print (count)
            with open(output_dir+ f, "w") as o:
                with open (des_dir +"totalStat"+str(i)+"/"+f.split('.')[0]+"_desc.txt","r") as ds:
                    with open(commments_dir +"totalComments"+str(i)+"/"+f,"r") as com:
                        o.write(ds.read()+"\n"+com.read())
        except OSError as e:
            #writer.write(str(count)+"\n")
            print(des_dir + "totalStat" + str(i) + "/" + f.split('.')[0] + "_desc.txt")
            print("error:"+str(count))
            print(e)

print("completed")
