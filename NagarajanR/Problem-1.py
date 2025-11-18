    def calculate(self, a, b, operation):
        # Normalizing string to lower case for easier matching
        op = operation.lower()
        
        if op == "add" or op == "+":
            return a + b
        elif op == "subtract" or op == "-":
            return a - b
        elif op == "multiply" or op == "*":
            return a * b
        elif op == "divide" or op == "/":
            if b != 0:
                return a / b
            else:
                return "Error: Division by zero"
        else:
            return "Invalid operation"

if __name__ == "__main__":
    # Inputs
    try:
        num_a = float(input("Enter number a: "))
        num_b = float(input("Enter number b: "))
        op_type = input("Enter type of operation (+, -, *, /): ")

        # Object Instantiation
        my_calc = Calculator()
        
        # Method Call
        result = my_calc.calculate(num_a, num_b, op_type)
        print(f"Result: {result}")
        
    except ValueError:
        print("Error: Please enter valid numbers for a and b.")
