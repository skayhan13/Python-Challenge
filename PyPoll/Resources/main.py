# PyPoll
# In this challenge, you are tasked with helping a small, rural town modernize its vote counting process.
# You will be give a set of poll data called election_data.csv. The dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote.

import os #import the python modules you would like to use aka dependencies
import csv #module for reading csv files 

file_path='../Resources/Election_Data.csv' #file name 
file_path=os.path.join('..', 'Resources', 'Election_Data.csv')
csvfile= open(file_path)
csvreader=csv.reader(csvfile)
csvreader= csv.reader(csvfile, delimiter=',') #since this file is a csv the delimiter is a comma
#print(csvreader) #this will tell us what kind of object the file is: input-output objects
csvheader=next(csvreader)  #moves you to the next item of the iterable (i.e. the list)
#print(csvreader)
#print(csvheader) #this will list the headers of the csv file in terminal

#Begin- identify the variables I would like to use
#Define variables
votes= [] #will be using voter id to find total number of votes; aka row 0
candidates= []
for row in csvreader: 
	#print(row)
	votes.append(row[0]) #append global method will tell us the length of a list 
	candidates.append(row[2])
#print(len(votes))
#print(candidates) - test to see if i am in the right location
total_votes = (len(votes))

#Count each number of candidates in the candidates list: 
Khan = int(candidates.count("Khan"))
Correy = int(candidates.count("Correy"))
Li = int(candidates.count("Li"))
O_Tooley = int(candidates.count("O'Tooley"))

#Find the percentage of votes:
Khan_percentage = round((Khan/total_votes) * 100) #round function will round to nearest whole number
Correy_percentage = round((Correy/total_votes) * 100)
Li_percentage = round((Li/total_votes) * 100)
O_Tooley_percentage = round((O_Tooley/total_votes) * 100)
   
#Print each candidate's name, vote percentage, and number of votes recieved:
# print(f"Khan: {Khan_percentage}% ({Khan})")
# print(f"Correy: {Correy_percentage}% ({Correy})")
# print(f"Li: {Li_percentage}% ({Li})")
# print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})")

#Compare votes and pick winner with the most votes- may be able to accomplish this with a dictionary, but unsure how to do so
if Khan > Correy :
	Winner = "Khan"
elif Correy > Khan: 
	Winner = "Correy"
elif Li > Khan :
	Winner = "Li"
elif O_Tooley > Khan :
	Winner = "O'Tooley"
#print(f"Winner: {Winner}")


#Print results to the terminal:
print("Election Results")
print("----------------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("----------------------------------------------------------")
print(f"Khan: {Khan_percentage}% ({Khan})")
print(f"Correy: {Correy_percentage}% ({Correy})")
print(f"Li: {Li_percentage}% ({Li})")
print(f"O'Tooley: {O_Tooley_percentage}% ({O_Tooley})")
print("----------------------------------------------------------")
print(f"Winner: {Winner}")

#Print results to text file:
f=open("C:/Users/sarak/OneDrive/Documents/DU Data Analytics Bootcamp/HW #3/Python-Challenge/PyPoll/Analysis/PyPoll_Analysis.txt", "w") #this is the absolute path of where I would like the txt file to be generated in
f.write("Election Results" + "\n") #\n will put a new line at the end of your f.write statement 
f.write("----------------------------------------------------------" + "\n")
f.write("Total Votes:" + str(total_votes) +"\n")
f.write("----------------------------------------------------------" + "\n")
f.write("Khan:" + str(Khan_percentage) +"%" +" " + str(Khan)+ "\n") #+ " " puts once space in file
f.write("Correy:" + str(Correy_percentage) +"%" +" " + str(Correy)+ "\n")
f.write("Li:" + str(Li_percentage) +"%" +" " + str(Li)+ "\n")
f.write("O'Tooley:" + str(O_Tooley_percentage) +"%" + " " + str(O_Tooley)+ "\n")
f.write("----------------------------------------------------------" + "\n")
f.write("Winner:" + str(Winner) + "\n")
f.close() #always good practice to end f open method with f.close