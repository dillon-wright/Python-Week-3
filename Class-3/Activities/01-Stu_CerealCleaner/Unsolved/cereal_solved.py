import os
import csv

cereal_csv = os.path.join("..", "Resources", "cereal_bonus.csv")
open_csv = open(cereal_csv)
csvd = csv.reader(open_csv, delimiter=",")
for row in csvd:
    if float(row[7]) >= 5:
        print(row)
