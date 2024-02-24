import pandas as pd
import os
from pathlib import Path


def main():
    input = os.getcwd() + "\input\\"
    Path("englishdata").mkdir(parents=True, exist_ok=True)
    total = 0
    for file in os.listdir(input):
        
        df = pd.read_csv(input + file, lineterminator="\n", low_memory=False)
        df = df.loc[:, ["TEXT"]]
        initial = df.size
        df.drop_duplicates(keep="first", inplace=True, subset=["TEXT"])
        deduped = df.size
        print(f"{file} before: {initial} deduped: {deduped}")
        df.to_csv("englishdata\\" + file, index=False)
        total+=deduped
    print(f"total unique lines: {total}")
main()
