import csv
import sys

csvpath = ('S:/Bootcamp/Python-Week-3/Homework/Instructions/PyPoll/Resources/election_data.csv')
Total_Votes = 0
Candidate_list = []
Candidate_Dict = {}

# count the number of votes and store it in var Total_Votes
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        Total_Votes += 1

# Create a list of candidates and store it in list Candidate_list
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        if row[2] not in Candidate_list:
            Candidate_list.append(str(row[2]))

# create the Candidate dict
    for key in Candidate_list:
        Candidate_Dict[key] = 0 #value

# Increment values int he candidate dict
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    next(csvreader, None)
    for row in csvreader:
        Candidate_Dict[row[2]] += 1

# Print to console
print('Election Results')
print('-------------------------')
print('Total Votes: '+ str(Total_Votes))
print('-------------------------')
for key in Candidate_Dict:
    print(key + ': ' + str(round((Candidate_Dict[key] / Total_Votes)*100, 3))+'% ('+str(Candidate_Dict[key])+')')
print('-------------------------')
print('Winner : '+str(max(Candidate_Dict, key=Candidate_Dict.get)))
print('-------------------------')

# Print to file
Analysis_File = open('S:/Bootcamp/Python-Week-3/Homework/Instructions/PyPoll/Analysis/Analysis_File.txt', 'w')
sys.stdout = Analysis_File
print('Election Results')
print('-------------------------')
print('Total Votes: '+ str(Total_Votes))
print('-------------------------')
for key in Candidate_Dict:
    print(key + ': ' + str(round((Candidate_Dict[key] / Total_Votes)*100, 3))+'% ('+str(Candidate_Dict[key])+')')
print('-------------------------')
print('Winner : '+str(max(Candidate_Dict, key=Candidate_Dict.get)))
print('-------------------------')
Analysis_File.close()