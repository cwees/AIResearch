import os
import csv
import re


def cleaner():
    input = os.getcwd() + "\input\\"
    for file in os.listdir(input):
        cleanfile(file)


if __name__ == "__cleaner__":
    cleaner()


def cleanfile(input_file_name):
    count = 0
    base_file_name = os.path.splitext(input_file_name)[0].split("\\")[-1]
    with open(input_file_name, newline="", encoding="utf-8") as input_csv:
        csv_file_as_list = csv.reader(input_csv, skipinitialspace=True)
        next(csv_file_as_list)  # skip first row of headers
        for row in csv_file_as_list:
            if len(row) < 15:
                continue
            if row[5] == "No Entities":
                continue
            count = count + 1
            if count % 500 == 0:
                print("Processing " + base_file_name + ".csv, row", count)
            base_list = [row[10]]  # from user


def clean_text(tweet):
    tweet = tweet.replace("\n", " ")  # remove newlines
    tweet = re.sub(r"(@[A-Za-z0–9_]+)|[^\w\s]|#|http\S+", "", tweet) # remove hashtags,
    return tweet

