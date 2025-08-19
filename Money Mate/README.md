# Money Mate


#### Description:
This project is a **terminal-based Finance Tracker** implemented in Python. It is an interactive financial management tool that allows users to track transactions and set budget limits. The application features a menu-driven interface where users can add transactions (income or expenses) with categories, view transaction history in an aligned table, and set budget limits for specific categories, with data stored in CSV files.

### How The Application Works:
When the program starts, the user is prompted to choose from a menu with four options: add a transaction, view transactions, set a budget, or exit.
- **Add Transaction**: Users input the date (DD-MM-YYYY), type (income/expense), category (e.g., food, salary), and amount. The data is saved to `transactions.csv`.
- **View Transactions**: Displays all recorded transactions in a formatted table, readable with aligned columns.
- **Set Budget**: Allows users to set a budget limit for a category, stored in `budgets.csv`.
- **Exit**: Terminates the application with a goodbye message.

The application continues until the user chooses to exit, with input validation ensuring valid data entries.

### Special Features:
- **Category Support**: Transactions include categories, enabling future budget tracking features.
- **Aligned Table Display**: Transactions are shown in a neatly formatted table with fixed column widths.
- **Data Persistence**: Uses CSV files (`transactions.csv` and `budgets.csv`) for storing data between sessions.

### Design Decisions & File Overview:

**`project.py`**

This is the main file containing all the code for the budget tracker, divided into several key functions:

- `main()`: The main game loop that manages the menu-driven interface and directs to other functions.
- `add_transaction()`: Handles adding a new transaction with date, type, category, and amount to `transactions.csv`.
- `view_transaction()`: Displays all transactions in a formatted table from `transactions.csv`.
- `set_budget()`: Sets a budget limit for a category in `budgets.csv`.

These functions are defined at the same indentation level as `main()` for modularity and readability, allowing easy future enhancements.

**`test_project.py`**

This file contains minimal unit tests for the three custom functions using `pytest`:
- `test_add_transaction()`: Verifies that a valid transaction is added and the success message is displayed.
- `test_view_transaction()`: Checks that transactions are displayed correctly in the aligned table format.
- `test_set_budget()`: Ensures a valid budget is set and the success message is shown.
These tests use `monkeypatch` to simulate inputs and `capsys` to capture output, meeting CS50P requirements with basic functionality checks.

### Design Decisions:
- **Command-Line Interface**: Chosen for simplicity and no external dependencies, making it portable across systems with Python.
- **CSV Storage**: Utilized for easy data persistence using Python's `csv` module, suitable for small-scale tracking.
- **Table Alignment**: Implemented fixed-width formatting in `view_transaction()` to improve readability.
- **Input Validation**: Ensures users enter valid data (e.g., positive amounts, correct date formats).
- **No External Dependencies**: Relies solely on Python's standard library, enhancing accessibility.

### Requirements:
- Python 3.x
- Terminal or command-line interface

To run the application, navigate to the project directory and execute:

```bash
python project.py
