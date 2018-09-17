# Modules
import os
import csv


# Set path for file
csvpath = os.path.join( "Resources", "election_data.csv")


print("\nElection Results")
print("--------------------------")

recCount = 0
candDict = dict()

def getCurrCandCount(candParam):
    candParam
    cvalue = candDict.get(candParam)
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
        recCount += 1
        candName = row[2]
        currCandCount = getCurrCandCount(candName)
        
        candDict[candName] = currCandCount + 1

    print(f"Total Votes: {recCount}")
    print("-------------------------")

    totalVotes = sum(candDict.values())

    maxCount = 0
    winnnerName = None
    
    for k in candDict:
        candPercent = round((float(candDict[k])/float(totalVotes)) * 100, 3)
        print(f"{k} : {candPercent}%  ({candDict[k]})")
        if(candDict[k] > maxCount ):
            maxCount = candDict[k]
            winnnerName = k

    print("---------------------------")
    print(f"Winner : {winnnerName}")
    print("---------------------------")



