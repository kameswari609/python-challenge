import csv 
import os
poll_csv_path =os.path.join('election_data.csv')
file_to_output = os.path.join('electionanalysis.txt')

candidate =[]
county =[]

voterid = []
khantotal =0
litotal =0
correytotal =0
otooleytotal =0






with open(poll_csv_path) as csvfile:

    csvreader = csv.reader(csvfile , delimiter =",")
  

    header = next(csvreader)
    for row in csvreader:
        candidate.append(str(row[2]))  #candidate array is appended
        county.append(str(row[1]))    #county array is created
        voterid.append(row[0])        #voterid array is created
        id1="Khan"
        id2="Li"
        id3 = "Correy"
        id4 = "O'Tooley"
        if row[2] == id1:
            khantotal+= 1   #khan votes are calculated
        elif row[2]== id2:  
            litotal+=1       #li total is calculated
        elif row[2] == id3:
            correytotal+=1   #correy total is calculated
        elif row[2]== id4:
             otooleytotal+=1  #otooley total is calculated


        


totalvotes=len(voterid)

khanpercentage = round((khantotal/totalvotes) * 100 )
lipercentage = round((litotal/totalvotes) * 100)           # percentage of each candidate from total is here
correypercentage = round((correytotal/totalvotes)*100)
otooleypercentage = round((otooleytotal/totalvotes)*100)

result = (
f"Election Results\n"
f"-----------------------------------\n"
f"Total votes: {len(voterid)}\n"
f"khan : {khanpercentage} %({khantotal})\n"
f"correy : {correypercentage} %({correytotal})\n"
f"Li :{lipercentage} %({litotal})\n "
f"O'Tooley: {otooleypercentage} %({otooleytotal})\n"
f"------------------------\n"
f"Winner: Khan\n"
f"-------------------------"


)
print(result, end="")
        

    #print the results and export the data to a text file 
with open(file_to_output,"w") as txt_file:
    
    #save the final analysis to txt file
    txt_file.writelines(result)
    

   
    
    

           
