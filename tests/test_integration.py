from quick_calc.calculator import add
from quick_calc.app import CalculatorApp
import tkinter as tk


def test_full_addition_flow():
    root = tk.Tk()
    app = CalculatorApp(root)

    app.entry.insert(0, "5")
    app.current_value = 5
    app.operation = "+"
    app.entry.delete(0, tk.END)
    app.entry.insert(0, "3")

    result = add(app.current_value, float(app.entry.get()))
    assert result == 8

    root.destroy()


def test_clear_resets_display():
    root = tk.Tk()
    app = CalculatorApp(root)

    app.entry.insert(0, "123")
    app.clear()

    assert app.entry.get() == "0"

    root.destroy()