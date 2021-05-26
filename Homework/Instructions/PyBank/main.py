import os
import csv
import numpy as np

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


with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader,None)

    for row in csvreader:
        sum_total = sum_total + int(row[1])
        mean_list.append(int(row[1]))
        row_count += 1
        if largest_increase < int(row[1]):
            largest_i_date = row[0]
        if largest_loss > int(row[1]):
            largest_l_date = row[0]
        #print(row)
        #print(np.mean(mean_list))


for counter in mean_list:
    cur_value = counter
    if last_value != 0:
        change_list.append((cur_value - last_value))
    last_value = counter
    print(counter)

largest_increase = max(change_list)
largest_loss = min(change_list)

print('Financial Analysis')
print('----------------------------')
print('Total Months: ' + str(row_count))
print('Total: $' + str(sum_total))
print('Average  Change: $'+str(round(np.mean(change_list), 2)))
print('Greatest Increase in Profits: '+largest_i_date+' ($'+str(largest_increase)+')')
print('Greatest Decrease in Profits: '+largest_l_date+' ($'+str(largest_loss)+')')
