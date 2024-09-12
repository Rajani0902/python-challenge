# python-challenge

Overview:
This repository contains 2 python scripts that analyse data sets PyBank and PyPoll where the data is stored in csv files in Resources folder.

PyBank: 
The task is to analyse the financial records fo the company  with Financial Data set Budge_data.csv file which has two columns Date and Profit/loss


Created a Python script that analyses the records to calculate each of the following values:

. The total number of months included in the dataset
. The net total amount of "Profit/Losses" over the entire period
. The changes in "Profit/Losses" over the entire period, and then the average of those changes
. The greatest increase in profits (date and amount) over the entire period
. The greatest decrease in profits (date and amount) over the entire period


Python code:

The code is stored in main.py file. to run the code type in git bash the folowing command
python main.py

Output:
Tha analysis results are printed to the terminal and exported as a text file financial_analysis.txt.


PyPoll

Pypoll data is in  election_data.csv file stored in Resources folder. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". The task is to create a Python script that analyzes the votes and calculates each of the following values:

. The total number of votes cast
. A complete list of candidates who received votes
. The percentage of votes each candidate won
. The total number of votes each candidate won
. The winner of the election based on popular vote

Run the script in git bash
python pypoll.py

The Results will be printed to the terminal and saved to the Analysis_election_results.txt

