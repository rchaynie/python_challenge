import csv
import os
from itertools import groupby
import operator

path=os.path.join("Resources","election_data.csv")


vote_total=0
correy_list=[]
correy_vote=0
khan_list=[]
khan_vote=0
li_list=[]
li_vote=0
otooley_list=[]
otooley_vote=0

with open(path, "r") as file:
    dict_reader=csv.DictReader(file)
    for row in dict_reader:
        vote_total+=1
        if row["Candidate"]=="Correy":
            correy_list.append("Candidate")
        if row["Candidate"]=="Khan":
            khan_list.append("Candidate")
        if row["Candidate"]=="Li":
            li_list.append("Candidate")
        if row["Candidate"]=="O'Tooley":
            otooley_list.append("Candidate")
            
    
#     for row in dict_reader:
#         if row["Candidate"]=="Correy":
#             correy_list.append("Candidate")
    
#     for row in dict_reader:
#         if row["Candidate"]=="khan":
#             khan_list.append("Candidate")
            
#     for row in dict_reader:
#         if row["Candidate"]=="li":
#             li_list.append("Candidate")
    
#     for row in dict_reader:
#         if row["Candidate"]=="O'Tooley":
#             otooley_list.append("Candidate")
    
    
    
for row in correy_list:
    correy_vote+=1

for row in khan_list:
    khan_vote+=1
    
for row in li_list:
    li_vote+=1
    
for row in otooley_list:
    otooley_vote+=1
    
print("Election Results \n --------------------------")
print(f"Total Votes: {vote_total}")
print("--------------------------")
print(f"Khan: {(khan_vote/vote_total)*100}% ({khan_vote})")    
print(f"Correy: {(correy_vote/vote_total)*100}% ({correy_vote})")
print(f"Li: {(li_vote/vote_total)*100}% ({li_vote})")
print(f"O'Tooley: {(otooley_vote/vote_total)*100}% ({otooley_vote})")
print("--------------------------")
print(f"Winner: ______")
    
    
        
        
        
        
        
        
        
        
        
       

    
    
#     for row in dict_reader:
#         vote_total+=1
    
# for row in unique_can:
#     print(row)