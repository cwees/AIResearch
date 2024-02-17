# textSentiments.py                             By: Samer Al-khateeb
# a script that use NLTK library and a pretrained sentiment analyzer
# called VADER (Valence Aware Dictionary and sEntiment Reasoner).
# It is good for short social media posts, however, it does not
# perform well for long text. This code was built based on this page:
# https://realpython.com/python-nltk-sentiment-analysis/

# Dependencies: you will need to install the following library
# before you can run this code.
# For Mac users, open terminal and type:
#       python3 -m pip install nltk
# For Windows users, open CMD and type:
#       py -m pip install nltk


import nltk
import os

# the line below needs to run only once
nltk.download("vader_lexicon")

# if you receive an error stating you can not download vader_lexicon
# comment the nltk.download('vader_lexicon') line and uncomment the
# block of code below

"""
import ssl
try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download('vader_lexicon')
"""

from nltk.sentiment import SentimentIntensityAnalyzer
import csv


def write_output_to_CSV(biglist, inputfilename):    


    columnNames = ["Text", "Sentiment"]
    outputfolder = "analyzed\\"
    filename = outputfolder + inputfilename[:-4] + "analyzed.csv"
    # creating a file to save the output
    with open(filename, "w", newline="", encoding="utf-8") as csvOutputFile:
        # creating a csv writer object
        csvwriter = csv.writer(csvOutputFile, delimiter=",", lineterminator="\n")
        # write the columns headers
        csvwriter.writerow(columnNames)
        csvwriter.writerows(biglist)


def main():
    # set the file name here
    folder = "topics\\"
    for file in os.listdir("topics"):
        print(file)

        inputfilename = file
        CSVInputFileName = folder + file

        # creating an instance of the class
        sia = SentimentIntensityAnalyzer()
        # creating a list to hold the output
        CSVoutputList = []

        # open the input file and read it
        with open(CSVInputFileName, newline="", encoding="utf-8") as csvInputFile:
            CSVFileAsList = csv.reader(csvInputFile, skipinitialspace=True)
            # skipping the first row in the csv input file
            next(CSVFileAsList)
            # for each row in the CSV file
            for row in CSVFileAsList:
                text = row[0]
                # this give you all the sentiments positive,
                # negative, neutral (add up to 1), and compound
                # sentiments = sia.polarity_scores(text)

                # this give you a score between [-1,1]
                sentiments = sia.polarity_scores(text)["compound"]
                # create a csv row
                CSVRow = [row[0], sentiments]
                # append the row to the output list
                CSVoutputList.append(CSVRow)

                # print(CSVRow)
                # print()
            # write the list to a CSV file
            write_output_to_CSV(CSVoutputList, inputfilename)


if __name__ == "__main__":
    main()
