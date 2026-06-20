# Testing Documentation

This document contains the major test cases used during the development of the Stack Based Calculator.

## Version 1 - Basic Arithmetic

Goal:
Verify that the calculator can correctly evaluate simple arithmetic expressions.

Tested:

* Addition
* Subtraction
* Multiplication
* Division
* Multi-digit numbers

Examples:

* 2+3
* 10-4
* 5*6
* 20/5

Screenshot:
v1-basic.png

---

## Version 2 - Operator Precedence

Goal:
Verify that operator precedence (BODMAS) works correctly.

Tested:

* Multiplication before addition
* Division before subtraction
* Multiple operators in a single expression

Examples:

* 2+3*4
* 10-2*3
* 20/5+2
* 2*3+4*5

Screenshot:
v2-precedence.png

---

## Version 3 - Parentheses Support

Goal:
Verify that expressions containing parentheses are evaluated correctly.

Tested:

* Single parentheses
* Nested parentheses
* Parentheses combined with operator precedence

Examples:

* (2+3)*4
* 2*(3+4)
* ((2+3)*4)
* 24+43*(111-90)

Screenshot:
v3-parentheses.png

---

## Version 4 - Negative Numbers

Goal:
Verify correct handling of unary minus and negative values.

Tested:

* Standalone negative numbers
* Negative numbers inside parentheses
* Negative values in expressions
* Consecutive minus signs

Examples:

* -5
* (-5)
* 2--3
* 2/-3
* (-5)(3)

Screenshot:
v4-negative.png

---

## Version 5 - Error Handling

Goal:
Detect invalid expressions and provide meaningful error messages.

Tested:

* Two operators in a row
* Expression ending with an operator
* Expression starting with an invalid operator
* Empty parentheses
* Invalid parenthesis placement
* Parenthesis mismatch

Examples:

* 2++3
* 2+*3
* 2+
* +2
* ()
* (()))
* )((

Screenshot:
v5-errors.png

---

## Final Validation

Goal:
Test all major features together.

Tested:

* Operator precedence
* Parentheses
* Negative numbers
* Unary minus
* Error detection

Examples:

* 24+43*(111-90)
* (2+3)(4+5)
* (-5)(3)
* 2--3
* 2++3

Screenshot:
final-tests.png

---

Testing was performed manually during development. New test cases were added whenever a bug or edge case was discovered.
***Note:
The screenshots in this document were captured after the final version of the calculator was completed. However, the corresponding tests were performed manually throughout the development process as new features and bug fixes were added.