import os
import csv
import statistics

# Define the path to the CSV file
csvpath = os.path.join('..', 'Resources', 'budget_data.csv')

# Initialize variables
month_count = 0
total_volume = 0
greatest_increase = float('-inf')
best_month = ''
greatest_decrease = float('inf')
worst_month = ''

change = []
month_to_month_change = []

# Open and read the CSV file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    
    # Read the header row
    csv_header = next(csvreader)
    
    # Read the first row to initialize previous_value
    first_row = next(csvreader)
    previous_value = int(first_row[1])
    total_volume += previous_value
    month_count += 1

    # Process each row
    for row in csvreader:
        month_count += 1
        current_value = int(row[1])
        total_volume += current_value
        
        # Calculate monthly change
        monthly_change = current_value - previous_value
        month_to_month_change.append(monthly_change)
        
        # Track greatest increase and decrease
        if monthly_change > greatest_increase:
            greatest_increase = monthly_change
            best_month = row[0]
        if monthly_change < greatest_decrease:
            greatest_decrease = monthly_change
            worst_month = row[0]
        
        # Update previous_value
        previous_value = current_value

# Calculate the average change
average_change = statistics.mean(month_to_month_change) if month_to_month_change else 0

# Print results
output_file = 'financial_analysis.txt'

# Write results to the output file
with open(output_file, 'w') as file:
    file.write("Financial Analysis\n")
    file.write("-------------------------------------------------------\n")
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total: ${total_volume}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {best_month} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {worst_month} (${greatest_decrease})\n")

print(f"Results have been written to {output_file}")
