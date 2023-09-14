# Code to extract User X User, User X Hashtag, and User x URL networks
# Modified By: Chris He
# Originally from : Samer Al-khateeb
import copy
import csv
import os


def process_file(input_file_name):
    # initalize counts
    count = 0
    total = 0
    data_count = 0
    # initialize lists for output to write to csv
    hashtag_output = []
    url_output = []
    user_output = []

    # get base file name
    base_file_name = os.path.splitext(input_file_name)[0].split("\\")[-1]
    # open file and read
    with open(input_file_name, newline="", encoding="utf-8") as input_csv:
        csv_file_as_list = csv.reader(input_csv, skipinitialspace=True)
        next(csv_file_as_list)  # skip first row of headers
        for row in csv_file_as_list:
            total = total + 1
            # removes incomplete data points
            if len(row) < 15:
                continue
            # removes data without entity dictionary
            if row[5] == "No Entities":
                continue
            count = count + 1

            # print every 500 rows
            if count % 500 == 0:
                print("Processing " + base_file_name + ".csv, row", count)

            # shared info
            base_list = [
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
            column_data = eval(row[5].strip('"'))

            # process entities dictionary

            # useruser
            if column_data.get("mentions") != None:
                for each_user in column_data["mentions"]:
                    user_list = copy.deepcopy(base_list)
                    user_list.append(each_user["username"])
                    user_output.append(user_list)
                    data_count = data_count + 1

            # hashtag
            if column_data.get("hashtags") != None:
                for each_hashtag in column_data["hashtags"]:
                    hashtag_list = copy.deepcopy(base_list)
                    hashtag_list.append(each_hashtag["tag"])
                    hashtag_output.append(hashtag_list)
                    data_count = data_count + 1

            # urls
            if column_data.get("urls") != None:
                for each_url in column_data["urls"]:
                    url_list = copy.deepcopy(base_list)
                    url_list.append(each_url["expanded_url"])
                    url_output.append(url_list)
                    data_count = data_count + 1
    input_csv.close()

    # if output folder does not exist, create it
    output_folder = os.getcwd() + "\output\\"
    if not os.path.exists(output_folder):
        print("creating output directory")
        os.makedirs(output_folder)

    print()
    print(
        "writing",
        data_count,
        "rows of data from",
        count,
        "data points from",
        base_file_name,
        "to csv.",
    )
    print()
    # writing to user x hashtag csv file
    with open(
        output_folder + base_file_name + "hashtag.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_hashtag_file:
        hashtag_writer = csv.writer(csv_hashtag_file)
        hashtag_writer.writerow(
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
        hashtag_writer.writerows(hashtag_output)

    # writing user x url csv file
    with open(
        output_folder + base_file_name + "url.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_url_file:
        url_writer = csv.writer(csv_url_file)
        url_writer.writerow(
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
        url_writer.writerows(url_output)

    # writing user x user csv file
    with open(
        output_folder + base_file_name + "user.csv",
        "w",
        newline="",
        encoding="utf-8",
    ) as csv_user_file:
        user_csv_writer = csv.writer(csv_user_file)
        user_csv_writer.writerow(
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
        user_csv_writer.writerows(user_output)
    return total - count, count, data_count
