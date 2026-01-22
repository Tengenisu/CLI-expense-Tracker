# Expense Tracker

**Version:** 1.0  
**Author:** Aryan  
**License:** MIT License

A simple command-line expense tracking application built with Python. This project was created to learn about Python lists and tuples and demonstrates their use to manage personal expenses efficiently.

## Features

- **View All Expenses**: Display all recorded expenses with their details
- **Add Expenses**: Record new expenses with amount, category, date, and optional notes
- **Remove Expenses**: Delete expenses using flexible search criteria (by date, amount, and/or category)
- **Edit Expenses**: Modify existing expense details including date, amount, category, and notes

## Requirements

- Python 3.x
- No external dependencies (uses only Python standard library)

## Installation

1. Clone or download this repository
2. Navigate to the `list_tuples` directory
3. No additional installation required - the script uses only Python standard library modules

## Usage

Run the expense tracker from the command line:

```bash
python expense_tracker.py
```

### Menu Options

When you run the program, you'll see a menu with the following options:

1. **View all the expenses** - Displays all recorded expenses
2. **Add an expense** - Add a new expense to your tracker
3. **Remove a expense** - Delete an expense from your list
4. **Edit an expense** - Modify an existing expense

### Adding an Expense

When adding an expense, you'll be prompted for:
- **Amount**: Enter the expense amount (must be a number)
- **Category**: Enter the expense category (e.g., "Food", "Transport", "Entertainment")
- **Note** (optional): You can add a note by typing 'y' when prompted, then enter your note and press `CTRL-D` (Linux/Mac) or `CTRL-Z` (Windows) to save

The expense will automatically be assigned:
- A unique ID
- The current date (in DD-Month-YYYY format)

### Removing an Expense

When removing an expense, you can search by:
- Date only
- Date and amount
- Date, amount, and category

The program will show matching expenses and let you select which one to delete.

### Editing an Expense

You can edit any field of an expense:
1. **Date**: Change the transaction date
2. **Amount**: Modify the expense amount
3. **Category**: Update the expense category
4. **Note**: Edit or add a note to the expense

Similar to removal, you can search for expenses using date, amount, and/or category.

## Project Structure

```
list_tuples/
├── expense_tracker.py    # Main application file
├── README.md             # This file
└── exepnse tracker flowchart.png  # Flowchart diagram
```

## How It Works

### Data Structure

Expenses are stored as tuples in a list (`all_expenses`). Each expense tuple contains:
- `(ID, Date, Amount, Category, Note)`

Example:
```python
(1, "15-January-2024", 50, "Food", "Lunch at restaurant")
```

### Key Functions

- `menu_option()`: Displays the main menu
- `add_expense()`: Adds a new expense to the list
- `view_all_expense()`: Displays all expenses
- `remove_expense()`: Removes an expense based on search criteria
- `edit_expense()`: Modifies an existing expense
- `partial_match()`: Helper function for finding expenses based on partial criteria
- `main()`: Main program loop that handles user input and calls appropriate functions

### Date Format

Dates are stored in the format: `DD-Month-YYYY` (e.g., "15-January-2024")

## Notes

- The expense tracker stores data in memory - expenses are not persisted to a file
- Each expense is assigned a unique ID automatically
- The program includes input validation to handle errors gracefully
- Notes can be multi-line - use `CTRL-D` (Linux/Mac) or `CTRL-Z` (Windows) to finish entering a note
- This is a solo project created for learning purposes

## Known Issues

The following issues have been identified in the current version:

1. **Global Variable Issue**: The `counter_for_id` variable is modified inside functions without using the `global` keyword, which will cause an `UnboundLocalError` when trying to increment the counter.

2. **Logic Bug in `add_expense()`**: When a note is `None`, the function creates an expense tuple but then continues to execute and creates another expense with the note parameter, potentially causing duplicate entries.

3. **Index Error in Note Editing**: When editing a note, the code checks `expense_to_edit[3]` (category) instead of `expense_to_edit[4]` (note) to determine if a note can be added.

4. **Single Execution**: The program only runs once per execution. After completing an action, the program exits instead of returning to the menu for continuous use.

5. **Unused Import**: The `time` module is imported but never used in the code.

6. **Empty List Handling**: No validation for empty expense lists when viewing, removing, or editing expenses - may cause confusing output or errors.

7. **Typographical Errors**: Several typos in user-facing messages:
   - "pelase" instead of "please" (multiple locations)
   - "emter" instead of "enter"
   - "didgits" instead of "digits"
   - "entere" instead of "enter"
   - "waht" instead of "what"
   - "fate" instead of "date"
   - "catergory" instead of "category"

8. **Formatting Inconsistency**: Some print statements use commas instead of colons in the output format (lines 119, 143).

9. **Note Logic Issue**: The requirement to have a category before adding a note (line 283) may be unintentional or needs clarification.

## Example Usage

```
Welcome to your own personal expense tracker
Please choose one of the following options

1. View all the expenses
2. Add an expense
3. Remove a expense
4. Edit an expense

Enter your choice: 2
enter the amount you want to add: 25
enter your category: Coffee
Do you want to enter a note : (y/n): n
expense added successfully
```

## Future Enhancements

Planned improvements for future versions:

- **Data Persistence**: Save expenses to a JSON file to persist data between program sessions
  - Implement automatic saving when expenses are added, edited, or removed
  - Load existing expenses from JSON file on program startup
  - Add error handling for file operations
- Add expense filtering and search functionality
- Generate expense reports and statistics (total spending, category breakdowns, monthly summaries)
- Add budget tracking features with alerts
- Export expenses to different formats (CSV, Excel)
- Implement a continuous menu loop so users can perform multiple operations without restarting
- Add data validation improvements
- Fix known issues listed above
- Add unit tests for better code reliability

## License

MIT License

Copyright (c) 2024 Aryan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
