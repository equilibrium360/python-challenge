# Modules
import os
import csv


# Set path for file
csvpath = os.path.join( "Resources", "budget_data.csv")


print("\nFinancial Analysis")
print("--------------------------")
# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    rec_count = 0
    net_profit_loss = 0
    previous_value = 0 
    change = 0
    change_sum = 0

    great_incr_profits = 0
    great_decr_profits = 0
    gipDate = ""
    gdpDate = ""


    csv_header = next(csvreader)
   # print(f"BudgetData Header: {csv_header}")


    # Loop through data
    for row in csvreader:
        rec_count += 1
        net_profit_loss += int(row[1])
        if(rec_count > 1):
            change = int(row[1]) - previous_value
            if(change > great_incr_profits):
                gipDate = row[0]
                great_incr_profits = change
            if(change < great_decr_profits):
                great_decr_profits = change  
                gdpDate = row[0]              
            change_sum += change
           # print(f"{row[0]}, {row[1]}, {previous_value}, {change_sum}")
        previous_value = int(row[1])
    print(f"Total Months: {rec_count}" )
    print(f"Total: ${net_profit_loss}" )
    #print(f"{change_sum}, {rec_count}")
    print(f"Average Change: ${round(change_sum/(rec_count-1), 2)}" )
    print(f"Greatest Increase in Profits: {gipDate} (${great_incr_profits})")
    print(f"Greatest Decrease in Profits: {gdpDate} (${great_decr_profits})")

resultsFile = open("ResultsFile.txt", "w")
resultsFile.write("\nFinancial Analysis")
resultsFile.write("\n--------------------------")
resultsFile.write(f"\nTotal Months: {rec_count}" )
resultsFile.write(f"\nTotal: ${net_profit_loss}" )

resultsFile.write(f"\nAverage Change: ${round(change_sum/(rec_count-1), 2)}" )
resultsFile.write(f"\nGreatest Increase in Profits: {gipDate} (${great_incr_profits})")
resultsFile.write(f"\nGreatest Decrease in Profits: {gdpDate} (${great_decr_profits})")
resultsFile.close()




