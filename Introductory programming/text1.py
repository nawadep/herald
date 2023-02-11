def divide(a, b):
    
 try:

  result = a / b

 except ZeroDivisionError:

  print("Cannot divide by zero")

 else:

  print(f"Result is: {result}")

 finally:

  print("Exiting the function")

# test the function

divide(10, 2)

divide(10, 0)
