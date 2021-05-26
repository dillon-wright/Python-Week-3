import csv
import numpy as np
import sys

# declare all of the important variables
row_count = 0
sum_total = 0
mean_list = []
change_list = []
last_value = 0
csvpath = ('S:/Bootcamp/Python-Week-3/Homework/Instructions/PyBank/Resources/budget_data.csv')
cur_value = 0
largest_loss = 0
largest_l_date = ''
largest_increase = 0
largest_i_date = ''
date_list = []
Head_0 = ''

# Open the CSV File and iterate through all rows and also store the header in head0
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    head_0 = next(csvreader, None)
    for row in csvreader:
        sum_total = sum_total + int(row[1])
        mean_list.append(int(row[1]))
        date_list.append(str(row[0]))
        row_count += 1

# Iterate though the list of all values and determien the change

for counter in mean_list:
    cur_value = counter
    if last_value != 0:
        change_list.append((cur_value - last_value))
    last_value = counter

# Set the final vars via an index or min / max

largest_increase = max(change_list)
largest_loss = min(change_list)
largest_i_date = date_list[change_list.index(largest_increase) + 1]
largest_l_date = date_list[change_list.index(largest_loss) + 1]

# print to console

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(row_count))
print('Total: $' + str(sum_total))
print('Average  Change: $' + str(round(np.mean(change_list), 2)))
print('Greatest Increase in Profits: ' + largest_i_date + ' ($' + str(largest_increase) + ')')
print('Greatest Decrease in Profits: ' + largest_l_date + ' ($' + str(largest_loss) + ')')
# Print to file

Analysis_File = open('S:/Bootcamp/Python-Week-3/Homework/Instructions/PyBank/Analysis/Analysis_File.txt', 'w')
sys.stdout = Analysis_File
print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(row_count))
print('Total: $' + str(sum_total))
print('Average  Change: $' + str(round(np.mean(change_list), 2)))
print('Greatest Increase in Profits: ' + largest_i_date + ' ($' + str(largest_increase) + ')')
print('Greatest Decrease in Profits: ' + largest_l_date + ' ($' + str(largest_loss) + ')')
Analysis_File.close()
