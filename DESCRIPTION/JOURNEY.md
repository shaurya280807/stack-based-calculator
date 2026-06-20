# Development Journey

This project started as a simple calculator built to understand how expression evaluation works internally instead of relying on Python's built-in `eval()` for the entire calculation process.

## Version 1 – Basic Calculator

The first version could:

* Read mathematical expressions
* Store numbers and operators separately
* Evaluate expressions using stacks
* Handle operator precedence (`*`, `/` before `+`, `-`)

At this stage, the goal was simply to make the calculator work for valid inputs.

### Challenges

* Understanding how stacks interact during evaluation
* Applying operator precedence correctly
* Managing multi-digit numbers

---

## Version 2 – Better Expression Parsing

After the basic calculator worked, expression parsing was improved.

### Added

* Multi-digit number support
* Cleaner token extraction
* Better separation of operators and operands

### Challenges

A major difficulty was correctly identifying where a number ends and an operator begins.

---

## Version 3 – Parentheses Support

The next goal was supporting expressions like:

(2+3)*4

### Added

* Opening and closing parenthesis handling
* Stack-based bracket evaluation
* Nested expression support

### Challenges

Parentheses introduced several bugs.

Examples:

* Missing closing brackets
* Extra closing brackets
* Incorrect stack states after bracket evaluation

One bug was caused by not removing an opening bracket from the operator stack after processing a closing bracket.

Finding and fixing that issue significantly improved understanding of stack debugging.

---

## Version 4 – Unary Minus and Edge Cases

After parentheses were working, focus shifted to expressions involving negative values.

### Added

* Support for negative numbers
* Handling expressions like:

-5

2+-3

2--3

(-5)

### Challenges

Distinguishing between:

* subtraction operator
* negative sign

was one of the most difficult parts of the project.

The parser had to decide whether `-` represented an operation or was part of a number.

Several parsing rules were added to correctly interpret these cases.

---

## Version 5 – Error Handling and Robustness

The final stage focused on invalid inputs and calculator stability.

### Added

Detection for:

* two operators in a row
* operator at the beginning
* operator at the end
* mismatched parentheses
* incorrect parenthesis order
* empty brackets
* invalid expressions

Examples:

2++
2+
+2
(())
())

### Additional Improvement

The calculator also handles implicit multiplication cases such as:

2(3+4)

(2+3)(4+5)

(-5)(3)

These expressions are automatically interpreted as multiplication.

---

## What I Learned

Through this project I learned:

* Stack-based expression evaluation
* Expression parsing
* Operator precedence handling
* Debugging complex logic bugs
* Edge case testing
* Incremental software development

The most valuable lesson was that writing code is only part of programming. A large amount of time was spent identifying bugs, reproducing them, understanding their cause, and designing fixes.

This project evolved through multiple versions and many small improvements rather than one large rewrite.
*Versions represent development milestones rather than separate preserved code snapshots.