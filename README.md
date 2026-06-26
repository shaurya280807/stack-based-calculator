# 🧮 Stack-Based Calculator

A command-line calculator built in **Python** that evaluates mathematical expressions using the **Stack** data structure. The project supports complex arithmetic expressions with operator precedence, nested parentheses, unary minus, decimal numbers, robust input validation, and persistent calculation history using **SQLite**.

---

## 🚀 Key Features

* Stack-based expression evaluation
* Multi-digit and decimal number support
* BODMAS / operator precedence
* Nested parentheses support
* Unary minus handling (`-5`, `2+-3`)
* Input validation and syntax checking
* Consecutive operator detection
* Parentheses balancing
* Division by zero handling
* Persistent calculation history using SQLite
* Timestamped calculations
* View complete or last **N** calculations
* Clear saved history

---

## 🛠 Technologies Used

* Python 3
* SQLite3
* datetime module

---

## 📚 Concepts Demonstrated

* Stack Data Structure
* Expression Parsing
* Operator Precedence (BODMAS)
* Parentheses Matching
* Error Handling
* Input Validation
* Modular Programming
* SQLite Database Integration

---

## 💻 Example

**Input**

```text
((24+43)*5)
```

**Output**

```text
335
```

---

## 📋 Commands

| Command         | Description              |
| --------------- | ------------------------ |
| `2+3*5`         | Evaluate an expression   |
| `history`       | Show complete history    |
| `history 5`     | Show last 5 calculations |
| `clear history` | Delete saved history     |

---

## 📂 Project Structure

```
CODE/
├── calculator.py
├── history.py
└── history.db

DESCRIPTION/
├── README.md
├── JOURNEY.md
└── AI_NOTES.md

TESTING/
├── testing.md
└── test screenshots/
```

---

## 🎯 Skills Demonstrated

* Stack implementation
* Expression evaluation algorithms
* SQLite database integration
* Exception handling
* Input validation
* Modular code organization
* Edge-case testing
* Debugging

---

## 🔮 Future Improvements

* GUI using Tkinter
* Scientific calculator functions
* Multiple user profiles
* Search and filter history
* Export history
* Better expression formatting

---

## 📌 Project Status

Completed and fully functional. Supports arithmetic expressions involving `+`, `-`, `*`, `/`, decimal numbers, unary minus, nested parentheses, and persistent SQLite-based history.
