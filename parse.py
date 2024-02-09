import pandas as pd
import os


def main():
    input = os.getcwd() + "\modeleddata\\"

    # output_folder = os.getcwd() + "\topics\\"
    # if not os.path.exists(output_folder):
    #     print("creating output directory")
    #     os.makedirs(output_folder)

    for file in os.listdir(input):
        parsetopics(input+file)


def parsetopics(input_file_name):
    df = pd.read_csv(input_file_name, lineterminator="\n")
    base_file_name = os.path.splitext(input_file_name)[0].split("\\")[-1]
    NUMBER_OF_TOPICS = 10
    for i in range(NUMBER_OF_TOPICS):
        new = df.loc[df["Topic"] == i]
        new.to_csv("topics\\" + base_file_name + str(i)+".csv", index=False)


main()
