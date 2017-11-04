import os
import csv


path = os.path.dirname(os.path.realpath(__file__))
csvpath = os.path.join(path, "raw_data", "election_data_2.csv")

votes = 0
candidates = []
vote_count = {}
vote_percent = {}

with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    

    for row in csvreader:
        
        votes = votes + 1        

        if row[2] not in candidates and row[2] not in "Candidate":
            candidates.append(row[2])
            vote_count[row[2]] = 1
        elif row[2] in candidates and row[2] not in "Candidate":
            vote_count[row[2]] = vote_count[row[2]] + 1

    for key, value in vote_count.items():
        vote_percent[key] = str(round(((value/votes)*100),3)) + "% ("+str(value) + ")"
    maxi = max(vote_count.keys(), key=(lambda k: vote_count[k]))    
    
 
    
    # print(vote_percent)
   
    print("Election Results")
    print("-------------------------------")
    print("Total Votes: "+ str(votes))
    print("-------------------------------")
    for key, val in vote_percent.items():
        print(key, ": ", val)
    print("-------------------------------")
    print("Winner: ", str(maxi))
    print("-------------------------------")
    
    f = open("Election_results.txt", "w")
    
    f.write('Election Results' + '\n')
    f.write('-------------------------------'+ '\n')
    f.write("Total Votes: "+ str(votes)+ '\n')
    f.write("-------------------------------"+ '\n')
    for key, val in vote_percent.items():
         f.write((key + ": " + val)+ '\n')
    f.write("-------------------------------"+ '\n')
    f.write("Winner: "+ str(maxi)+ '\n')
    f.write("-------------------------------"+ '\n')
    
    f.close()