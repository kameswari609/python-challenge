import csv
import os



#set the path to csv file adnt txt file
bank_csv_path =os.path.join('budget_data.csv')
file_to_output = os.path.join('profitlossanalysis.txt')

with open(bank_csv_path) as csvfile:


    total =0
    date =[]
    profitloss =[]
    rev_change = []

    csvreader = csv.reader(csvfile , delimiter =",")
    
    csvheader = next(csvreader)

    #print("Financial Analysis")
    #print("----------------------------")
    

    
    for row in csvreader:
            profitloss.append(float(row[1])) #append the array with row 1
            date.append(row[0]) #append the array with row 0
        
    
    for i in range(1, len(profitloss)):
                rev_change.append(profitloss[i] - profitloss[i-1])   #append the rev-change array with value differences of profitloss column per date
        
    avg_rev_change = sum(rev_change)/len(rev_change)   #find average change in profit/loss change
max_rev_change = max(rev_change)  #find highest change in profilloss
min_rev_change = min(rev_change)  #find lowest  change in profitloss
max_rev_change_date = str(date[rev_change.index(max(rev_change))]) #find date for the highest profitloss change 
min_rev_change_date = str(date[rev_change.index(min(rev_change))])


results = (

f"Financial Analysis\n"
f"------------------------\n"
f"the total_months : {len(date)}\n"
f"total is :{str(sum(profitloss))}\n"
f"Avereage  Change: ${str(round(avg_rev_change,2))}\n"
f"Greatest Increase in Profits: {max_rev_change_date} $ {str(max_rev_change)}\n"
f"Greatest Decrease in Profits: {min_rev_change_date} $ {str(min_rev_change)}\n")


print(results, end="")
        

    #print the results and export the data to a text file 
with open(file_to_output,"w") as txt_file:
    
    #save the final analysis to txt file
    txt_file.writelines(results)
    



            
    
        




