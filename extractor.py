import copy
import csv
import os.path
import json


def processFile(file):
    count = 0
    items = [
        "source",
        "text",
        "relationship_type",
        "relation_date",
        "relation_time",
        "user_followers_count",
        "user_following_count",
        "location",
        "user_verification",
        "user_id",
        "hashtag",
    ]

    # initialize lists for output to write to csv
    hashtagOutput = []
    urlOutput = []
    userOutput = []

    # open file and read
    with open(file, newline="", encoding="utf-8") as csv_input_file:
        csvFileAsList = csv.reader(csv_input_file, skipinitialspace=True)
        next(csvFileAsList)  # skip first row of headers
        for row in csvFileAsList:
            count = count + 1
            if count % 100 == 0:
                print("Processing row #", count)
            jsonRaw = (row[5]).replace("'", '''"''').replace("/", "//")
            print(jsonRaw)
            jsonColumnData = json.loads(
                jsonRaw
                # .replace("“", '"')
                # .replace("”", '"')
                # .replace("‘", "'")
                # .replace("’", "'")
                # .replace("—", "-")
                # .replace("❤", "")
                # .replace("◌️", "'")
            )
            baseList = [
                row[10],  # from user
                row[1],  # text
                row[2],  # relationship type
                row[3],  # date
                row[4],  # time
                row[11],  # follower count
                row[12],  # following count
                row[8],  # location
                row[14],  # verification
                row[0],  # user id
            ]
            # user
            if "mentions" in jsonColumnData.keys():
                for eachUserMentioned in jsonColumnData["mentions"]:
                    mentionList = copy.deepcopy(baseList)
                    mentionList.append(eachUserMentioned.get("username"))
                    userOutput.append(mentionList)

            # urls
            if "urls" in jsonColumnData.keys():
                for eachUrlMentioned in jsonColumnData["urls"]:
                    urlList = copy.deepcopy(baseList)
                    urlList.append(eachUrlMentioned.get("unwound_url"))
                    urlOutput.append(urlList)

            # hashtags
            if "hashtags" in jsonColumnData.keys():
                for eachHashtagMentioned in jsonColumnData["urls"]:
                    hashtagList = copy.deepcopy(baseList)
                    hashtagList.append(eachHashtagMentioned.get("unwound_url"))
                    hashtagOutput.append(hashtagList)

    csv_input_file.close()

    baseFileName = os.path.splitext(file)[0]

    with open(baseFileName + "hashtag.csv", "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(hashtagOutput)

    with open(baseFileName + "url.csv", "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(urlOutput)

    with open(baseFileName + "user.csv", "w") as csvfile:
        # creating a csv writer object
        csvwriter = csv.writer(csvfile)
        csvwriter.writerows(userOutput)


# def processHashtags():
#     list = []
#     return list


# def processMentions():
#     list = []
#     return list


# def writeFile(list, filename):
#     print()

# create list of fields from input file
# parse entities json
# if "urls" in jsonColumnData.keys(): # urls
# iterate through urls in jsonColumnData and append to filenameurl.csv with list of fields

# if "hashtags" in jsonColumnData.keys(): #hashtags
# iterate through hashtags in jsonColumnData and append to filenameurl.csv with list of fields

# if "mentions" in jsonColumnData.keys():  # user
# iterate through mentions in jsonColumnData and append to filenameurl.csv with list of fields

# add to another csv with just text for sentiment analysis?
