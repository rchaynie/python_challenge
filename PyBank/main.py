import csv
import os
import statistics

path=os.path.join("Resources","budget_data.csv")

profit_loss=[]
unique_months=[]
total_months = 0
total_prof = 0

change_by_month=[]




# finding total months
with open (path, "r") as file:
    dict_reader=csv.DictReader(file)
    
    for row in dict_reader:
        if row['Date'] not in unique_months:
                unique_months.append(row['Date'])
           
    for e in unique_months:
        total_months+=1
    
    
        
# finding total profit 
with open (path, "r") as file:
    dict_reader=csv.DictReader(file)
          

    for row in dict_reader:
        profit_loss.append(int(row['Profit/Losses']))

    total_prof=sum(profit_loss)           

            
    for e in range(1, len(profit_loss)):
        change_by_month.append(profit_loss[e]-profit_loss[e-1])
        

avg_change=statistics.mean(change_by_month)
max_change=max(change_by_month)
min_change=min(change_by_month)

best_month=unique_months[change_by_month.index(max_change)+1]
worst_month=unique_months[change_by_month.index(min_change)+1]

    
print(f"Total Months: {total_months}")      
print(f"Total: ${total_prof}")
print(f"Average change: ${avg_change:0.2f}")
print(f"Greatest Increase in Profits: {best_month} (${max_change:0.2f})")
print(f"Greatest Decrease in Profits: {worst_month} (${min_change:0.2f})")


        

results=(f"Total Months: {total_months} \n"      
f"Total: ${total_prof}\n"
f"Average change: ${avg_change:0.2f}\n"
f"Greatest Increase in Profits: {best_month} (${max_change:0.2f})\n"
f"Greatest Decrease in Profits: {worst_month} (${min_change:0.2f})\n")

file_to_output="analysis/profit_results.txt"
        
     
    
    
    
with open(file_to_output, "w") as txt_file:
    txt_file.write(results)


