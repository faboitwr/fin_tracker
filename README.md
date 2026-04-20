# Personal Financial Tracker made with an SQL Database
Very basic financial tracker made with DBBrowser, Python and SQLite3

## Introduction
A simple, Python-based application for me to store personal financial records privately/locally on my PC.

## Systems Overview
"initiation.py" generates a fresh, empty instance of "finrec_.db" on a user's PC.

"fintrackFunc.py" contains background functions that allow a user to interact with the database through a Python-based system; whereas "fintrackApp.py" calls these functions through a simple menu system to allow for users to easily interface with the database through a Python app.

## Specifications & Features
- "initiation.py" to create the database "finrec_.db" and relevant tables for storing financial records
- "fintrackApp.py" to interface with the database
  - "app_run()" which utilises helper functions to adjust record details in the database
  - Helper functions
    - Insertion function
    - Deletion function
    - Update function
    - Display all records for a given MM/YY
    - Display the largest recorded purchases for a given MM/YY
    - Display current total for given MM/YY
    - Getter functions for record ID, vendor ID and all IDs in a month
