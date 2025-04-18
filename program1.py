class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()

    def calculate(self):
        if self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'divide':
            if self.b == 0:
                return "Error: Division by zero"
            return self.a / self.b
        else:
            return "Error: Unsupported operation"

# Taking input from the user
try:
    a = float(input("Enter first number (a): "))
    b = float(input("Enter second number (b): "))
    operation = input("Enter operation (add, subtract, multiply, divide): ")

    calc = Calculator(a, b, operation)
    result = calc.calculate()
    print("Result:", result)
except ValueError:
    print("Invalid input. Please enter numeric values for a and b.")
