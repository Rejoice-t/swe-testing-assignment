![Tests](https://img.shields.io/badge/tests-10%20passed-brightgreen)
![Version](https://img.shields.io/badge/version-v1.0.0-orange)

# swe-testing-assignment
# Quick-Calc

Quick-Calc is a simple calculator application developed in Python using Tkinter.  
The application supports the four basic arithmetic operations: addition, subtraction, multiplication, and division. It also includes a clear function to reset the display.

The purpose of this project is to demonstrate software testing principles, version control using Git, and automated testing using the Pytest framework.

---

## Features

- Addition
- Subtraction
- Multiplication
- Division
- Clear display
- Graphical user interface using Tkinter
- Automated unit and integration tests using Pytest

---

## Setup Instructions

1. Clone the repository
2. Navigate to the project folder
3. Create a virtual environment
4. Activate the environment
Windows:

5. Install dependencies

## Running the Application

Run the calculator GUI:
## Running the Tests
Run all tests using Pytest:


This command executes both the unit tests and integration tests located in the `tests` folder.

---

# Testing Framework Research

## Pytest vs Unittest

Python provides several frameworks for automated testing. Two of the most common are **Unittest** and **Pytest**.
**Unittest** is the built-in testing framework that comes with Python. It is inspired by Java's JUnit framework and uses a class-based structure. Tests are organised into test cases and require more boilerplate code to define test classes and setup methods.
**Pytest**, on the other hand, is a more modern testing framework that focuses on simplicity and readability. It allows developers to write tests as simple functions without needing to create classes. Pytest also provides powerful features such as fixtures, better error reporting, and automatic test discovery.
One advantage of Pytest is that it requires less code to write tests, making it easier to maintain and read. It also integrates well with continuous integration systems and supports plugins for extended functionality.
For this project, **Pytest was chosen** because it simplifies writing tests and automatically discovers test files, which makes it ideal for small projects like Quick-Calc.
