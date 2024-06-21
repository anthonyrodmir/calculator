# Calculator

A simple calculator class implemented in Python.

## Description

This repository contains a basic `Calc` class that provides simple arithmetic operations including addition, subtraction, multiplication, division, exponentiation, and square root.

## Class Methods

- `add(a, b)`: Add two numbers together
- `sub(a, b)`: Subtract two numbers
- `mul(a, b)`: Multiply two numbers
- `div(a, b)`: Divide two numbers
- `pow(a, b)`: Raise `a` to the power of `b`
- `sqrt(a)`: Return the square root of `a`

## Usage

Here's a simple example of how to use the `Calc` class:

```python
from calc import Calc

calculator = Calc()

# Addition
print(calculator.add(2, 3))  # Output: 5

# Subtraction
print(calculator.sub(5, 2))  # Output: 3

# Multiplication
print(calculator.mul(3, 4))  # Output: 12

# Division
print(calculator.div(10, 2))  # Output: 5.0

# Exponentiation
print(calculator.pow(2, 3))  # Output: 8

# Square Root
print(calculator.sqrt(16))  # Output: 4.0
