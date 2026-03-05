# Testing Strategy

The testing strategy for the Quick-Calc project follows the principles taught in the software testing lecture. The goal was to ensure that the calculator functions work correctly and that the graphical interface interacts properly with the calculation logic.

The project uses automated testing with the **Pytest framework**. Two types of tests were implemented: **unit tests** and **integration tests**.

---

# What Was Tested

The following components were tested:

- Core calculator functions (add, subtract, multiply, divide)
- Handling of edge cases such as division by zero
- Negative numbers
- Decimal numbers
- Large numbers
- Interaction between the GUI and calculator logic
- The clear function resetting the display

---

# What Was Not Tested

Some aspects were intentionally not tested:

- Visual appearance of the user interface
- Button layout and styling
- Performance testing

These were excluded because the main focus of the assignment is **functional correctness and testing strategy**, not UI design.

---

# Testing Pyramid

The testing pyramid suggests that a project should contain many unit tests, fewer integration tests, and even fewer end-to-end tests.

This project follows the pyramid structure:

- **Unit Tests (8 tests)** – verify individual calculator functions
- **Integration Tests (2 tests)** – verify interaction between GUI and logic

Unit tests form the base of the pyramid because they are fast and isolate individual pieces of functionality.

---

# Black-Box vs White-Box Testing

Both black-box and white-box testing approaches were used in this project.

**White-box testing** was used for the unit tests because the internal functions of the calculator module were directly tested. The test cases were written with knowledge of the implementation.

**Black-box testing** was used in the integration tests where the system was treated like a user would interact with it. The tests simulate entering values and performing operations without focusing on internal implementation details.

---

# Functional vs Non-Functional Testing

This project mainly focuses on **functional testing**.

Functional testing verifies that:

- Arithmetic operations produce the correct result
- Division by zero is handled correctly
- The clear function resets the calculator display

Non-functional aspects such as performance, usability, and security were not tested because they are outside the scope of this assignment.

---

# Regression Testing

Automated tests help detect regressions when new features are added. If a developer changes the calculator logic in the future, running the test suite will immediately reveal whether existing functionality has been broken.

This ensures that previously working features continue to work correctly after updates.

---

# Test Results Summary

| Test Name | Type | Result |
|-----------|------|--------|
| test_add | Unit | Pass |
| test_subtract | Unit | Pass |
| test_multiply | Unit | Pass |
| test_divide | Unit | Pass |
| test_divide_by_zero | Unit | Pass |
| test_negative_numbers | Unit | Pass |
| test_decimal_numbers | Unit | Pass |
| test_large_numbers | Unit | Pass |
| test_full_addition_flow | Integration | Pass |
| test_clear_resets_display | Integration | Pass |