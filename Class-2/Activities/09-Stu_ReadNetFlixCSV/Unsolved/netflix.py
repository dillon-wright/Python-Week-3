import os
import csv

csvpath = os.path.join('..', 'Resources', 'netflix_ratings.csv')

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    for row in csvreader:
        print(row)



