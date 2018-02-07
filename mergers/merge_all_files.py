import glob
import pandas as pd

files_to_transfer = glob.glob('../datasets/8mcsvs/*.csv')

list_dataframe = []

for filename in sorted(files_to_transfer):
    list_dataframe.append(pd.read_csv(filename))
    print("Finished adding the file")

all_files_dataframe = pd.concat(list_dataframe)

all_files_dataframe.to_csv('../datasets/8mcsvs/videoStatsMerged_Python_Try2.csv')