import csv
from datetime import datetime

EXPENSES_FILE = 'expenses.csv'

def add_expense(category, amount, date=None):
    if date is None:
        date = datetime.today().strftime('%Y-%m-%d')
    with open(EXPENSES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([date, category, amount])
    print(f"Added: {category} - ${amount} on {date}")

def view_expenses():
    try:
        with open(EXPENSES_FILE, 'r') as file:
            reader = csv.reader(file)
            print("\nExpenses:")
            print("Date       | Category      | Amount")
            print("------------------------------------")
            for row in reader:
                print(f"{row[0]:<11} | {row[1]:<13} | ${row[2]}")
    except FileNotFoundError:
        print("No expenses found.")

def total_expenses():
    total = 0.0
    try:
        with open(EXPENSES_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                total += float(row[2])
    except FileNotFoundError:
        return 0.0
    return total
