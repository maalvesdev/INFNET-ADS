# User Input and Basic Text Analysis - **Date:** 05/03/2026

### Topics Covered

- User interaction with `input()`
- Type conversion using `int()`
- Formatted output using f-strings
- String length calculation with `len()`
- Counting characters in a string using `count()`

---

### Example: Converting Seconds to Minutes

This exercise converts a number of seconds into minutes and seconds using integer division and modulo.

```python
seconds = int(input("Enter the number of seconds: "))
print(f"{seconds//60} Minutes and {seconds%60} Seconds")
