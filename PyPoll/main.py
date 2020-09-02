import csv
import os

path=os.path.join("Resources","election_data.csv")


vote_total=0
khan_list=[]
khan_vote=0
correy_list=[]
correy_vote=0
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
            
    
for row in correy_list:
    correy_vote+=1

for row in khan_list:
    khan_vote+=1
    
for row in li_list:
    li_vote+=1
    
for row in otooley_list:
    otooley_vote+=1
    
# variables for win percentage by candidate

khan_per=format((khan_vote/vote_total)*100,".3f")
correy_per=format((correy_vote/vote_total)*100,".3f")
li_per=format((li_vote/vote_total)*100,".3f")
otooley_per=format((otooley_vote/vote_total)*100,".3f")

# who is the winning candidate

winner_var= {
    khan_vote:"Khan",
    correy_vote:"Correy",
    li_vote:"Li",
    otooley_vote: "O'tooley"
}

winner=winner_var.get(max(winner_var))


print("Election Results \n--------------------------")
print(f"Total Votes: {vote_total}")
print("--------------------------")
print(f"Khan: {khan_per}% ({khan_vote})")    
print(f"Correy: {correy_per}% ({correy_vote})")
print(f"Li: {li_per}% ({li_vote})")
print(f"O'Tooley: {otooley_per}% ({otooley_vote})")
print("--------------------------")
print(f"Winner: {winner}")
    
results=("Election Results \n--------------------------\n"
f"Total Votes: {vote_total}\n"
f"--------------------------\n"
f"Khan: {khan_per}% ({khan_vote})\n"  
f"Correy: {correy_per}% ({correy_vote})\n"
f"Li: {li_per}% ({li_vote})\n"
f"O'Tooley: {otooley_per}% ({otooley_vote})\n"
f"--------------------------\n"
f"Winner: {winner}")
    
    
file_to_output="analysis/voting_results.txt"
        
     
    
    
    
with open(file_to_output, "w") as txt_file:
    txt_file.write(results)