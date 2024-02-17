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
    df = pd.DataFrame()
    for file in file_list:
        df_temp = pd.read_csv(file_path + file, lineterminator="\n")
        df = df._append(df_temp, ignore_index=True)

    df.head()

    initial = int(df.size / 15)
    df.drop_duplicates(keep="first", inplace=True)
    final = int(df.size / 15)
    df.to_csv(file, index=False)
    print(f"{dir} initial data size: {initial} Final data size: {final}")


all()
