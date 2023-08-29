# A code to extract User X User network
# By: Samer Al-khateeb
# Revised by Chris He
#################################################################
# How to use this file:
# After collecting Twitter data from TAGs(Twitter Archiving Google Sheet, https://tags.hawksey.info)
# Download the file you used to collect data as CSV file
# save this file to the same directory as this code
# change the name of the file (the value of the "input_filename" variable)
# in the code to match your file name, you should see the output file
# "User-User-Network.csv" generated

import csv

def test(file):
    with open(file, newline="", encoding="utf-8") as csv_input_file:
        CSV_file_as_list = csv.reader(csv_input_file, skipinitialspace=True)
        print(CSV_file_as_list)

def user(filename):
    # counter to keep track of the rows processed
    count = 0

    # creating a list to hold the output values so we can write it to CSV file
    CSV_output_list = []

    # variable that hold the file name
    input_filename = filename + ".csv"
    output_filename = filename.split(".")[0] + "UserUserNework.csv"

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
    ]

    # open the input file and read it
    with open(input_filename, newline="", encoding="utf-8") as csv_input_file:
        CSV_file_as_list = csv.reader(csv_input_file, skipinitialspace=True)
        next(CSV_file_as_list)  # skip first row of headers
        # process each row in the input file
        for row in CSV_file_as_list:
            count = count + 1
            if count % 100 == 0:  # print count every 100 rows
                print()
                print("Processing row #", count)
                print()
            baselist = [
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
            # convert entity string to Dictionary
            jsonColumnData = eval(row[5].replace("'", '''"'''))
            # id_str = row[0]
            # from_user = row[10]
            # text = row[1]

            # # to determin the type of the relationship
            # relationship_type = row[2]

            # # taking the time column and splitting it into date and time
            # relation_date = row[3]
            # relation_time = row[4]

            # user_followers_count = row[11]
            # user_friends_count = row[12]
            # user_location = row[8]

            # user_verification = row[14]

            # each User Mentioned in the jsonColumnData is
            # nested inside the jsonColumnData["urls"]
            if "mentions" in jsonColumnData.keys():  # user
                for eachUserMentioned in jsonColumnData["mentions"]:
                    # creating a file to save the output
                    with open(
                        output_filename, "w", newline="", encoding="utf-8"
                    ) as csv_output_file:
                        # creating a csv writer object
                        csvwriter = csv.writer(
                            csv_output_file, delimiter=",", lineterminator="\n"
                        )
                        # write the columns headers
                        csvwriter.writerow(
                            [
                                "source",
                                "text",
                                "relationship_type",
                                "relation_date",
                                "relation_time",
                                "user_followers_count",
                                "user_friends_count",
                                
                                "location",
                                "user_verification",
                                "user_id",
                                "user",
                            ]
                        )

                        # creating a list of values (a row)
                        CSV_output_row = [
                            from_user,
                            text,
                            relationship_type,
                            relation_date,
                            relation_time,
                            user_followers_count,
                            user_friends_count,
                            eachUserMentioned["screen_name"],
                            user_location,
                            user_verification,
                            id_str,
                        ]

                        # adding the row to the list of output
                        CSV_output_list.append(CSV_output_row)

                        # writing/inserting the list to the output file
                        csvwriter.writerows(CSV_output_list)

                    csv_output_file.close()
            # if "urls" in jsonColumnData.keys(): # urls
            # if "hashtags" in jsonColumnData.keys(): #hashtags
    csv_input_file.close()


def analyze():
    print()
