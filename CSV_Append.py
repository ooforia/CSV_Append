import pandas as pd
import glob
import os

#-------------------------------------------------------
# Appends multiple csv files that have similar case sensitive column headers.
# Different columns headers will be appended at the end.
#-------------------------------------------------------
path = r"D:\Python Projects\CSV_Append\FILES_TO_APPEND"
files_to_append = glob.glob(path + "/*.csv")

#create empty list
li = []

#loop through list and read into one dataframe and append to list
for filename in files_to_append:
    filename_nopath = os.path.basename(filename)
    #Reads with the index columns intact
    temp_df = pd.read_csv(filename, index_col=None, header=0)
    #append
    li.append(temp_df)
    print(f"Dataframe created for: {filename_nopath} | Shape:{temp_df.shape}")

df = pd.concat(li, axis=0, ignore_index=True)

#Replaces NaN with None in dataframe (csv is not affected)
df = df.astype(object).where(pd.notnull(df),None)

#export df into csv, removes index columns in CSV
#df.to_csv('D:\Python Projects\CSV_Append\OUTPUT.csv', index=False)
print("------------------------------------")
print(f"Created csv with shape: {df.shape}")

print(df)