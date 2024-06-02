#Calculator
#Design a simple calculator with basic arithmetic operations.Prompt the user to input two numbers and an operation choice.Perform the calculation and display the result.

def calculate(num1, num2, operator):
  """
  Performs basic arithmetic operations based on the given operator.

  Args:
      num1: The first number.
      num2: The second number.
      operator: The operation symbol (+, -, *, /).

  Returns:
      The result of the calculation.
  """

  if operator == "+":
    return num1 + num2
  elif operator == "-":
    return num1 - num2
  elif operator == "*":
    return num1 * num2
  elif operator == "/":
    if num2 == 0:
      return "Error: Division by zero"
    else:
      return num1 / num2
  else:
    return "Invalid operator"

while True:

  num1 = float(input("Enter the first number: "))
  num2 = float(input("Enter the second number: "))
  operator = input("Choose an operation (+, -, *, /): ")

  result = calculate(num1, num2, operator)

  print(f"{num1} {operator} {num2} = {result}")

  choice = input("Do you want to continue (yes/no)?")
  if choice != "yes":
    break

print("Calculator closed.")
