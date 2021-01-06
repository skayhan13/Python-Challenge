#HW 3- Python Challenge
import os #import the python modules you would like to use
import csv #module for reading csv files 

file_path='../Resources/PyBankData.csv'
file_path=os.path.join('..', 'Resources', 'PyBankData.csv')
csvfile= open(file_path)
csvreader=csv.reader(csvfile)
csvreader= csv.reader(csvfile, delimiter=',') #since this file is a csv the delimiter is a comma
#print(csvreader) #this will tell us what kind of object the file is: input-output objects
csvheader=next(csvreader)  #moves you to the next item of the iterable (i.e. the list)
#print(csvheader) #this will list the headers of the csv file in terminal

#Your task is to create a Python script that analyzes the records to calculate each of the following:
#1. The total number of months included in the dataset
#2. The net total amount of "Profit/Losses" over the entire period
#3. Calculate the changes in "Profit/Losses" over the entire period, then find the average of those changes
#4. The greatest increase in profits (date and amount) over the entire period
#5. The greatest decrease in losses (date and amount) over the entire period

#Begin- identify the variables I would like to use
month= [] #create data types to store your variables; empty brackets denote lists 
profit= []

index=1 #create a counter outside the loop so it will reset after each iteration 
#f=open("Analysis.txt","w") #this will create a text file in the specified file path in line 5, w is used to write a file, r for read, a to add to an existing file
f=open("C:/Users/sarak/OneDrive/Documents/DU Data Analytics Bootcamp/HW #3/Python-Challenge/PyBank/Analysis/PyBank_Analysis.txt", "w") #this is the absolute path of where I would like the txt file to be generated in
for row in csvreader: 
	#print (index)- print statement to test if we are in the correct index 
	month.append(row[0]) #append global method will tell us the length of a list; python begins with 0 therefore first column is row 0 
	profit.append(row[1]) 
	index+=1 #+= is the same thing as index= index+ 1
index=1
sum_of_avg=0 #sum of average 
maxp=0 #maximum profit
minp=0 #minimum profit
sum_of_profit=int(profit[0])
#print (profit[0]) -test if this captures the first cell of profit column in csv file
#print (profit[0:87])
for r in range(len(month)-1):  #-1 to handle the end of csv where there are no values (come up one)	
	#print(month[index],profit[index])
	#print(month[index],profit[index-1])
	sum_of_profit=sum_of_profit+int(profit[index])
	pr=int(profit[index])-int(profit[index-1])
	if abs(pr)>abs(minp):  #abs to denote absolute value #print (max(profit[0:10])) #tried to utilize the max function, however max function treats list as a string not value
		minp=pr	
		date_value_for_min=month[index]
		loc_index=index
	if (maxp)<(pr):
		maxp=pr	
		date_value_for_max=month[index]
		loc_index2=index
	sum_of_avg=sum_of_avg+pr
	#f.write(str(index) +"," + str(profit[index]) + "," + str(sum_of_profit) + "\n")
	#print ("\n",pr)
	index+=1
#print(sum_of_profit)
avg=sum_of_avg/(len(month)-1) #-1 to allot for the blank rows at the bottom of csv file
avg= round(avg,2) #round function,2 will round value to 2 decimal places

#Print results to text file:
f.write("----------------------------------------------------------"+ "\n")#what you what to put inside the text file
f.write("Financial Analysis" + "\n") #\n will put a new line at the end of your f.write statement 
f.write("----------------------------------------------------------" + "\n")
f.write("Total Months:" + str(len(month)) + "\n")
f.write("Total profit: $" + str(sum_of_profit) + "\n")
f.write("Average Change: $" + str(avg)+ "\n")
f.write("Greatest Increase in Profits:" + str((date_value_for_max) +" " +"$"+ str(maxp) + "\n"))
f.write("Greatest Decrease in Profits:"+ str((date_value_for_min)+ " "+ "$"+ str(minp)+ "\n"))
f.close() #always good practice to end f open method with f.close

#Print results to the terminal:
print("----------------------------------------------------------")
print("Financial Analysis")
print("----------------------------------------------------------")
print(f'Total Months: {len(month)}')
print(f'Total profit: $ {sum_of_profit}')
print(f'Average Change: $ {avg}')
print(f'Greatest Increase in Profits: {date_value_for_max} ${(maxp)}')
print(f'Greatest Decrease in Profits: {date_value_for_min} ${(minp)}')
