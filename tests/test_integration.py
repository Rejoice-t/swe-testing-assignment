from quick_calc.calculator import add, clear


class FakeApp:
    def __init__(self):
        self.current_value = 0
        self.operation = None
        self.display = "0"

    def insert(self, value):
        self.display = value

    def get(self):
        return self.display

    def reset(self):
        self.display = str(clear())


def test_full_addition_flow():
    app = FakeApp()

    # simulate entering 5 + 3
    app.insert("5")
    app.current_value = float(app.get())
    app.operation = "+"

    app.insert("3")
    result = add(app.current_value, float(app.get()))

    assert result == 8


def test_clear_resets_display():
    app = FakeApp()

    app.insert("123")
    app.reset()

    assert app.get() == "0"