import pandas as pd
import os

def main():
    file_path = "input/copilot/"
    file_list = os.listdir(file_path)
    print(file_list)
    df_append = pd.DataFrame()
    for file in file_list:
        df_temp = pd.read_csv(file_path+file)
        df_append = df_append._append(df_temp, ignore_index=True)

    print(df_append.size)
    df_append.drop_duplicates(inplace=True)
    print(df_append.size)
    df_append.to_csv("copilot.csv", index=False)

main()