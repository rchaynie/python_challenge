import csv
import os

path=os.path.join("Resources","budget_data.csv")

unique_months=[]
total_months = 0
total_prof = 0

change_by_month=[]
avg_change=0
max_change=0



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
        total_prof+= int(row['Profit/Losses'])

            
    for row in dict_reader:
        print(row)
        break
            
            
# Average change by month         
    for i in dict_reader:
        change_by_month.append(dict_reader[i]-dict_reader[i-1])

print(change_by_month)
    
        
print(f"Total Months: {total_months}")      
print(f"Total: ${total_prof}")


        




