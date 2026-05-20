# Expense Tracker

A CLI Expense Tracker to monitor your purchases.

This tool is inspired from [Expense Tracker](https://roadmap.sh/projects/expense-tracker).

## How to run

1. Clone this repository
   ```
   git clone https://github.com/unseen24/Expense-Tracker
   cd Expense-Tracker
   ```

2. Run it using:
   ```
   python app.py [command]
   ```

## Commands

| Command | Arguments | Requirement | Description |
| :--- | :--- | :--- | :--- |
| `add` | `-d` <br> `-a` <br> `-c` | Required <br> Required <br> Optional | Description of the expense <br> Amount of the expense <br> Category of the expense (Miscellaneous by default) |
| `update` | `--id` | Required | ID of the expense to update |
| `delete` | `--id` | Required | ID of the expense to delete |
| `list` | *None* | *None* | List all expenses |
| `summary`| `--month` | Optional | List the summary of expenses in a specific month |
| `budget` | `-b` <br> `-m` | Required <br> Required | The budget limit <br> Set a budget limit for a specific month |
| `export` | *None* | *None* | Export expenses to a CSV file |
| `-h`, `--help` | *None* | *None* | List all commands |
