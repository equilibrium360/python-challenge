# Modules
import os
import csv


# Set path for file
csvpath = os.path.join( "Resources", "election_data.csv")


print("\nElection Results")
print("--------------------------")

rec_count = 0
cand_dic = dict()

def getCurrCandCount(cand_param):
    cand_param
    cvalue = cand_dic.get(cand_param)
    if(cvalue == None):
        return 0
    else:
        return cvalue

# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    # Loop through data
    for row in csvreader:
        rec_count += 1
        candName = row[2]
        currCandCount = getCurrCandCount(candName)
        
        cand_dic[candName] = currCandCount + 1

    print(f"Total Votes: {rec_count}")
    print("-------------------------")
    
    for k in cand_dic:
        print(f"{k} : {cand_dic[k]}")



