import sqlite3

# Create a connection to the database file
conn = sqlite3.connect('expenses.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

# Execute SQL queries to create tables and define schema
cursor.execute('CREATE TABLE IF NOT EXISTS expenses (id INTEGER PRIMARY KEY, amount REAL, category TEXT)')

# Function to add an expense
def add_expense():
    try:
        amount = float(input("Enter the amount: "))
        category = input("Enter the category: ")
        cursor.execute('INSERT INTO expenses (amount, category) VALUES (?, ?)', (amount, category))
        conn.commit()
        print("Expense added successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Function to view all expenses
def view_expenses():
    cursor.execute('SELECT * FROM expenses')
    expenses = cursor.fetchall()
    for expense in expenses:
        print(f"ID: {expense[0]}, Amount: {expense[1]}, Category: {expense[2]}")

# Function to delete an expense
def delete_expense():
    try:
        expense_id = int(input("Enter the ID of the expense to delete: "))
        cursor.execute('DELETE FROM expenses WHERE id = ?', (expense_id,))
        conn.commit()
        print("Expense deleted successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")

# User interface
while True:
    print("\n1. Add expense")
    print("2. View expenses")
    print("3. Delete expense")
    print("4. Quit")
    choice = input("Enter your choice: ")
    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        delete_expense()
    elif choice == '4':
        break
    else:
        print("Invalid choice. Please try again.")

# Close the connection
conn.close()