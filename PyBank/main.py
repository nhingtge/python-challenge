import os
import csv

pybank_csv = os.path.join('.', 'PyBank', 'Resources','budget_data.csv')


#set variables to baseline of 0
total_profit = 0
total_months = 0
increase = 0
decrease = 0
previous_row = 0


#create list to store monthly change 
#Example: Day2 12-Stu_UdemyZip
monthly_changes_list = []

with open(pybank_csv) as pybank:
    csvreader = csv.reader(pybank, delimiter = ",")
    next(pybank)

    #start loop
    for row in csvreader:
        #looping through each row, add 1 to month variable for each new row
        total_months += 1
        #looping through each row, add current row to running profut value
        total_profit += int(row[1])
        #have to create something that adds the change in valuve betweem rows to monthly changes list
        current_row = int(row[1])
        monthly_change = current_row - previous_row
        monthly_changes_list.append(monthly_change)
        #initially have to set last row = 0, but as it moves forward has to change value to the current row
        previous_row = current_row
        #check for greatest profit/loss integers
        if int(row[1]) > increase:
            increase = int(row[1])
            increase_month = row[0]
        if int(row[1]) < decrease:
            decrease = int(row[1])
            decrease_month = row[0]

    #get rid of first null value in monthly changes list
    monthly_changes_list.pop(0)
    #calculate average change
    average_change = sum(monthly_changes_list) / len(monthly_changes_list)

    highest = max(monthly_changes_list)
    lowest = min(monthly_changes_list)

#print in terminal
print("Financial Analysis")
print("-----------------------------")
print(f"Total Months: {total_months}")
print(f"Total: ${total_profit}")
print(f"Average Change: -${0 - (average_change):.2f}")
print(f"Greatest Increase in Profits: {increase_month} ${highest}")
print(f"Greatest Decrease in Profits: {decrease_month} -${0 - lowest}")

#set output path
output_file = os.path.join('.', 'PyBank', 'Analysis', 'financial_analysis.txt')

#print .txt
with open(output_file,'w') as txtfile:
    txtfile.write(f"Financial Analysis\n")
    txtfile.write(f"-----------------------------\n")
    txtfile.write(f"Total Months: {total_months}\n")
    txtfile.write(f"Total: ${total_profit}\n")
    txtfile.write(f"Average Change: ${average_change}\n")
    txtfile.write(f"Greatest Increase in Profits:, {increase_month}, (${highest})\n")
    txtfile.write(f"Greatest Decrease in Profits:, {decrease_month}, (-${0 - lowest})\n")
