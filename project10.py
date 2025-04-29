 def calculator(a, b, operation):
    if operation == '+':
        return a + b
    elif operation == '-':
        return a - b
    elif operation == '*':
        return a * b
    elif operation == '/':
        return a / b
    else:
        return "Invalid operation"

print(calculator(5, 3, '+'))  
print(calculator(10, 4, '-'))  
print(calculator(7, 2, '*'))  
print(calculator(8, 2, '/'))  
    
 