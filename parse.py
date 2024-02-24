import pandas as pd
import os


def main():
    input = os.getcwd() + "\modeleddata\\"

    for file in os.listdir(input):

        parsetopics(input + file)


def parsetopics(input_file_name):

    print(f"parsing {input_file_name} now")
    df = pd.read_csv(input_file_name, lineterminator="\n")
    base_file_name = os.path.splitext(input_file_name)[0].split("\\")[-1]

    for i in range(df["Topic"].max() + 1):
        new = df.loc[df["Topic"] == i]
        new.to_csv("topics\\" + base_file_name + str(i) + ".csv", index=False)


main()
