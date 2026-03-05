import tkinter as tk
from quick_calc.calculator import add, subtract, multiply, divide, clear


class QuickCalc:
    def __init__(self, root):
        self.root = root
        self.root.title("Quick-Calc")

        self.current_value = 0
        self.operation = None

        self.display = tk.Entry(root, width=20, font=("Arial", 16))
        self.display.pack()

        self.create_buttons()

    def create_buttons(self):
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", "C", "=", "+"
        ]

        frame = tk.Frame(self.root)
        frame.pack()

        for button in buttons:
            tk.Button(
                frame,
                text=button,
                width=5,
                height=2,
                command=lambda b=button: self.on_click(b)
            ).pack(side=tk.LEFT)

    def on_click(self, char):
        if char.isdigit():
            self.display.insert(tk.END, char)

        elif char in "+-*/":
            self.current_value = float(self.display.get())
            self.operation = char
            self.display.delete(0, tk.END)

        elif char == "=":
            second_value = float(self.display.get())

            if self.operation == "+":
                result = add(self.current_value, second_value)
            elif self.operation == "-":
                result = subtract(self.current_value, second_value)
            elif self.operation == "*":
                result = multiply(self.current_value, second_value)
            elif self.operation == "/":
                result = divide(self.current_value, second_value)
            else:
                result = "Error"

            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))

        elif char == "C":
            self.display.delete(0, tk.END)
            self.display.insert(0, str(clear()))


if __name__ == "__main__":
    root = tk.Tk()
    app = QuickCalc(root)
    root.mainloop()