# code to extract User X User, User X Hashtag, and User x URL networks
# By: Chris He and Samer Al-khateeb
import copy
import csv
import os


def processFile(inputFilename):
    count = 0
    # initialize lists for output to write to csv
    hashtagOutput = []
    urlOutput = []
    userOutput = []
    baseFileName = os.path.splitext(inputFilename)[0]
    # open file and read
    with open(inputFilename, newline="", encoding="utf-8") as inputCSV:
        csvFileAsList = csv.reader(inputCSV, skipinitialspace=True)
        next(csvFileAsList)  # skip first row of headers
        for row in csvFileAsList:
            count = count + 1
            if count % 250 == 0:
                print("Processing " + baseFileName + ".csv, row #", count)
            # if count > 8128:
            #     print(count)
            #     print(row)
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
            # strip string of " and convert to dictionary
            columnData = eval(row[5].strip('"'))

            if type(columnData) == dict:
                # useruser
                if columnData.get("mentions") != None:
                    for eachUser in columnData["mentions"]:
                        userList = copy.deepcopy(baseList)
                        userList.append(eachUser["username"])
                        userOutput.append(userList)
                # hashtag
                if columnData.get("hashtags") != None:
                    for eachHashtag in columnData["hashtags"]:
                        hashtagList = copy.deepcopy(baseList)
                        hashtagList.append(eachHashtag["tag"])
                        hashtagOutput.append(hashtagList)
                # urls
                if columnData.get("urls") != None:
                    for eachUrl in columnData["urls"]:
                        urlList = copy.deepcopy(baseList)
                        urlList.append(eachUrl["expanded_url"])
                        urlOutput.append(urlList)
    inputCSV.close()

    # if output folder does not exist, create it
    outputFolder = os.getcwd() + "\output\\"
    if not os.path.exists(outputFolder):
        os.makedirs(outputFolder)
    # write to csv
    with open(
        os.getcwd() + "\output\\" + baseFileName + "hashtag.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as csvHashtagFile:
        # creating a csv writer object
        hashtagWriter = csv.writer(csvHashtagFile)
        hashtagWriter.writerow(
            [
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
        )
        hashtagWriter.writerows(hashtagOutput)

    with open(
        os.getcwd() + "\output\\" + baseFileName + "url.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as csvUrlFile:
        # creating a csv writer object
        urlWriter = csv.writer(csvUrlFile)
        urlWriter.writerow(
            [
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
                "url",
            ]
        )
        urlWriter.writerows(urlOutput)

    with open(
        os.getcwd() + "\output\\" + baseFileName + "user.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as csvUserFile:
        # creating a csv writer object
        userCsvWriter = csv.writer(csvUserFile)
        userCsvWriter.writerow(
            [
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
                "user",
            ]
        )
        userCsvWriter.writerows(userOutput)

