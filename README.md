# Personal Financial Tracker made with an SQL Database
Very basic financial tracker made with DBBrowser, Python and SQLite3

"initiation.py" creates "finrec_.db" when run; there is no need to install both at once.

"fintrackApp.ipynb" contains both background functions to interact with the database and a function to make it easier for users to interface with the database.

IMPT: As made for personal usage, data validation is very lax.

## Specifications & Features
- "initiation.py" to create the database "finrec_.db" and relevant tables for storing financial records
- "fintrackApp.ipynb" to interface with the database
  - "app_run()" which utilises helper functions to adjust record details in the database
  - Helper functions
    - Insertion function
    - Deletion function
    - Update function
    - Display all records for a given MM/YY
    - Display the largest recorded purchases for a given MM/YY
    - Display current total for given MM/YY
    - Getter functions for record ID and vendor ID
