###PyBank###
#-------------------------------------------------------------------------------------------------------#
#Dependencies - Import the os module so you can create file paths across operating systems/
############# - Import the csv module so the code can read the csv file
#-------------------------------------------------------------------------------------------------------#
import os
import csv

#Outline the path to the csv file you're going to use in the code
#-------------------------------------------------------------------------------------------------------#
csvpath = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'Resources', 'budget_data.csv')

file_output = "raw_data/results.txt"

#Establish Variables and Lists
total_months = 0
total_profloss = 0
prev_profloss = 0
month_change = []
profloss_change_list = []
greatest_decrease = ['', 99999999999]
greatest_increase = ['', 0]


#Read Data into Dictionaries and Calculate 
with open(csvpath,newline="") as csvfile:  
    reader = csv.DictReader(csvfile)
    for row in reader:
        #Calculate total number of months included in the dataset
        total_months += 1
        #Calculate the net total amount of "Profit/Losses" over the entire period
        total_profloss += int(row['Profit/Losses'])

        #Calulate the average of the changes in "Profit/Losses" over the entire period
        profloss_change = int(row["Profit/Losses"])- prev_profloss
        prev_profloss = int(row["Profit/Losses"])
        profloss_change_list = profloss_change_list + [profloss_change]
        month_change = month_change + [row["Date"]]
        #The greatest increase in profits (date and amount) over the entire period
        if profloss_change>greatest_increase[1]:
            greatest_increase[1]= profloss_change
            greatest_increase[0] = row['Date']
        #The greatest decrease in losses (date and amount) over the entire period
        if profloss_change<greatest_decrease[1]:
            greatest_decrease[1]= profloss_change
            greatest_decrease[0] = row['Date']


#print(profloss_change_list)
profloss_avg = sum(profloss_change_list)/len(profloss_change_list)


print('Average Change in Profit/Losses: $ ' + str(profloss_avg))
print("Total Months: " + str(total_months))
print("Total Profit/Losses: $ " + str(total_profloss))
print(greatest_increase)
print(greatest_decrease)



with open(file_output, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("---------------------\n")
    file.write("Total Months: %d\n" % total_months)
    file.write("Total: $%d\n" % total_profloss)
    file.write("Average Change $%d\n" % profloss_avg)
    file.write("Greatest Increase in Profits: %s ($%s)\n" % (greatest_increase[0], greatest_increase[1]))
    file.write("Greatest Decrease in Profits: %s ($%s)\n" % (greatest_decrease[0], greatest_decrease[1]))