# Stack Based Calculator

A calculator written in Python that evaluates mathematical expressions using stacks.

This project started as a simple calculator and was gradually improved by adding validation, error handling, support for brackets, decimal numbers, unary minus, nested expressions, and persistent calculation history using SQLite.

## Features

* Multi-digit number support
* Decimal number support
* BODMAS/operator precedence
* Bracket support
* Nested bracket support
* Unary minus support (e.g. -5, 2+-3)
* Division by zero handling
* Invalid input detection
* Consecutive operator detection
* Parentheses validation
* Persistent calculation history using SQLite
* Timestamp for every saved calculation
* View complete calculation history
* View last N calculations (history 5, history 10, etc.)
* Clear calculation history

## Example

Input:

((24+43)*5)

Output:

335

## Available Commands

Normal calculation:

2+3

View complete history:

history

View last 5 calculations:

history 5

Clear saved history:

clear history

## What I Learned

While building this project I learned:

* How stacks work
* How mathematical expressions are evaluated
* How operator precedence is implemented
* How to debug larger programs
* How to find and fix edge cases
* How to test a program using unusual inputs
* How to connect Python with SQLite databases
* How to work with multiple Python files in the same project
* How to import and use functions from another file
* How timestamps can be generated using Python's datetime module
* The difference between indexing and slicing while working with data

## Project Structure

CODE/

* calculator.py
* history.py
* history.db

DESCRIPTION/

* README.md
* JOURNEY.md
* AI_NOTES.md

TESTING/

* testing.md
* test screenshots

## Future Improvements

* GUI version using Tkinter
* Multiple user profiles
* Scientific calculator functions
* Search and filter history
* Better expression formatting

## Project Status

Currently working and supports arithmetic expressions involving +, -, *, /, decimals, unary minus, and nested parentheses. Calculation history is stored permanently using SQLite and can be viewed or cleared through commands.
