import pandas as pd
import os


def all():
    stuff = [
        "bard",
        "elevenlabs",
        "copilot",
        "jasper",
        "all",
        "midjourney",
        "openai",
        "stablediffusion",
    ]
    for file in stuff:
        merge(file)


def merge(dir):
    file_path = dir + "/"
    file_list = os.listdir(file_path)
    print(file_list)
    df_append = pd.DataFrame()
    for file in file_list:
        df_temp = pd.read_csv(file_path + file, lineterminator="\n")
        df_append = df_append._append(df_temp, ignore_index=True)

    initial = int(df_append.size / 15)
    # print(df_append.head)
    df_append.drop_duplicates(
        keep="first",
        inplace=True,
        subset=["TEXT"]
    )
    final = int(df_append.size / 15)
    df_append.to_csv("input/" + file, index=False)
    print(f"{dir} initial data size: {initial} Final data size: {final}")


all()
