# A code to extract User X URL network   By: Samer Al-khateeb
#################################################################
#How to use this file:
#After collecting Twitter data from TAGs(Twitter Archiving Google Sheet, https://tags.hawksey.info)
#Download the file you used to collect data as CSV file 
#save this file to the same directory as this code
#remove the header of the file (the first row in the file)
#change the name of the file (the value of the "input_filename" variable) 
#in the code to match your file name, you should see the output file 
#"User-URL-Network.csv" generated 

import csv

def main():
  #counter to keep track of the rows processed
  count = 0
  
  #creating a list to hold the output values so we can write it to CSV file
  CSV_output_list =[]

  #variable that hold the file name
  input_filename = 'input.csv'

  #open the input file and read it
  with open(input_filename, newline='', encoding='utf-8') as csv_input_file:
    CSV_file_as_list = csv.reader(csv_input_file, skipinitialspace=True)
    
    #process each ron in the input file
    for row in CSV_file_as_list:
      count = count +1
      print()
      print("Processing row#", count)
      print()
    
      id_str = row[0]
      from_user = row[1]
      text = row[2]

      #to determin the type of the relationship
      if(text[0] == 'R' and text[1] == 'T'):
        relationship_type = 'retweet'
      elif (text.find('@') != -1):
        relationship_type = 'mention'
      else:
        relationship_type = 'tweet'

      #taking the time column and splitting it into date and time
      relation_date_and_time = row[4].split(" ")
      relation_date = relation_date_and_time[0].strip()
      relation_time = relation_date_and_time[1].strip()

      user_followers_count = row[13]
      user_friends_count = row[14]
      user_location = row[15]
      entities_str = row[17]

      #removing quotes from entities_str column
      entities_Str_NoQuotes = entities_str.strip('"')

      #converting the string to Dictionary
      jsonColumnData = eval(entities_Str_NoQuotes)

      #each User Mentioned in the jsonColumnData is 
      #nested inside the jsonColumnData["urls"]
      for eachURL in jsonColumnData["urls"]:
        
        #creating a file to save the output
        with open('User-URL-Network.csv', 'w', newline='', encoding='utf-8') as csv_output_file:
          #creating a csv writer object 
          csvwriter = csv.writer(csv_output_file, delimiter=',', lineterminator='\n')
          
          #write the columns headers
          csvwriter.writerow(["source", "text", "relationship_type", "relation_date", "relation_time", "user_followers_count", "user_friends_count", "URL"])
          
          #creating a list of values (a row) 
          CSV_output_row = [from_user, text, relationship_type, relation_date, relation_time, user_followers_count, user_friends_count, eachURL["expanded_url"]]
          
          #adding the row to the list of output
          CSV_output_list.append(CSV_output_row) 
          
          #writing/inserting the list to the output file 
          csvwriter.writerows(CSV_output_list)


        csv_output_file.close()
  csv_input_file.close()
main()


