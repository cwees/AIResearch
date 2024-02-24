import pandas as pd
import os
from pathlib import Path


def main():
    input = os.getcwd() + "\input\\"
    Path("englishdata").mkdir(parents=True, exist_ok=True)
    for file in os.listdir(input):
        print(file)
        df = pd.read_csv(input + file, lineterminator="\n", low_memory=False)
        df = df.loc[:, ["TEXT"]]
        df.drop_duplicates(keep="first", inplace=True, subset=["TEXT"])
        df.to_csv("englishdata\\" + file, index=False)


main()
