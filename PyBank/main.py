# First we'll import the os module
# This will allow us to create file paths across operating systems
import os

# Module for reading CSV files
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

#setting up some lists to eitehr fill or reference
months_count = 0
total_value = 0
change_list = []
month_change = []
greatest_increase = []
greatest_decrease = []

#Reading using CSV module

with open(csvpath) as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile)

    print(csvreader)

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")
    first_row = next(csvreader)
    first_value = int(first_row[1])
    months_count+=1
    total_value+=first_value
    #print(first_value)

    #Read each row of data after the header
    for row in csvreader:
        months_count+=1
        total_value+=int(row[1])

        net_change = int(row[1])-first_value
        first_value = int(row[1])
        change_list.append(net_change)
        month_change+=[row[0]]

    
    max_increase = max(change_list)
    min_increase = min(change_list)

    index_change = (change_list.index(max_increase))
    min_index_change = (change_list.index(min_increase))
    average = sum(change_list)/len(change_list)


    results = (f"Financial Analysis\n"
    f"---------------------\n"
    f"Total Months in file: {months_count}\n"
    f"Total Change in file: {total_value}\n"
    f"Average Change in file: {average} \n"
    f"Greatest Increase in Profits {month_change[index_change]}: {max_increase}\n"
    f"Greatest Descrease in Profits {month_change[min_index_change]}: {min_increase} ")
    
    print(results)

 # Specify the file to write to
output_path = os.path.join("Resources", "financialsummary.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w') as txtfile:

    txtfile.write(results)      