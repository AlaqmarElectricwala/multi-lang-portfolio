# Simple Budget Tracker application to manage transactions and budgets.
import sys
import csv
import os
from datetime import datetime

# Main Function
def main():
    while True:
        print("--Welcome To MONEY MATE--")
        print("1. Add Transaction")
        print("2. View Transactions")
        print("3. Set Budget")
        print("4. Exit")
        try:
            # Prompt user for option
            option = int(input("Choose an option (1-4): "))
        except ValueError:
            # Handle non integer input
            print("Please enter a valid option.")
            continue
        match option:
            case 1:
                add_transaction()
            case 2:
                view_transaction()
            case 3:
                set_budget()
            case 4:
                print("\n--Thank you for using MONEY MATE. Goodbye!--") # Exit message
                sys.exit()
            case _:
                # Handle invalid option
                print("Invalid option!")

# Function to add a new transaction to the CSV file
def add_transaction():
    CSV_FILE = "transactions.csv"
    # Check if the file exists if not create it
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["date", "type", "amount"])

    type_input = input("Enter Type (income/expense): ").strip().lower()
    # Validate Transaction Type
    while type_input not in ["income", "expense"]:
        type_input = input("Enter Type (income/expense): ").strip().lower()

    category = input("Enter Category: ").strip().lower()
    # Validate Category is not empty
    while not category:
        category = input("Enter Category: ").strip().lower()

    # Loop for amount Validation
    while True:
        try:
            amount = float(input("Enter Amount: "))
            # Ensure amount is positive
            if amount <= 0:
                continue
            break
        except ValueError:
            print("Invalid Amount! Enter a number.")

    date = input("Enter Date (DD-MM-YYYY): ").strip()
    try:
        # Validate Date Format
        datetime.strptime(date, "%d-%m-%Y")
    except ValueError:
        print("Invalid Date Format!")
        return

    # Append new transaction
    with open(CSV_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, type_input, category, amount])
    print("--TRANSACTION ADDED--")

# Function to view transactions
def view_transaction():
    CSV_FILE = "transactions.csv"
    if not os.path.exists(CSV_FILE):
        print("No Transactions Found!")
        return

    print("\nView Transactions")
    print("1. View All")
    try:
        option = int(input("Choose an Option (1): "))
    except ValueError:
        print("Invalid Input!")
        return

    transactions = [] # List to Store Transactions
    with open(CSV_FILE, mode='r', newline='') as file:
        reader = csv.reader(file)
        next(reader) # Skip header row
        for row in reader:
            # Ensure row has correct number of elements
            if len(row) == 4:
                transactions.append(row)

    # Check if transactions exists
    if not transactions:
        print("No transactions!")
        return

    # Print Table Header with aligned columns
    print("\n{:<12} {:<10} {:<15} {:<10}".format("Date", "Type", "Category", "Amount"))
    # Print Separator Line
    print("-" * 47)
    # Display Each Transaction with aligned columns
    for trans in transactions:
        print("{:<12} {:<10} {:<15} {:<10}".format(trans[0], trans[1], trans[2], trans[3]))
    print()

# Function to set a budget limit for a category
def set_budget():
    BUDGET_FILE = "budgets.csv"
    if not os.path.exists(BUDGET_FILE):
        with open(BUDGET_FILE, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["category", "budget"])

    category = input("Enter Category: ").strip().lower()
    # Check if category is empty
    if not category:
        print("Category cannot be empty!")
        return

    # Loop For Budget Validation
    while True:
        try:
            budget = float(input("Enter Budget Amount: "))
            # Ensure Budget is Positive
            if budget <=0:
                continue
            break
        except ValueError:
            print("Invalid Budget! Enter a number.")

    # Append new Budget
    with open(BUDGET_FILE, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([category, budget])
    print("--BUDGET SET--")


if __name__ == "__main__":
    main()
