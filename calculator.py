def calculate(operation, x, y):
    ''' 
    operation - takes the string ['add', 'sub', 'mul', 'div']
    x & y - two numbers
    '''
    if operation == 'add':
        return x + y
    elif operation == 'sub':
        return x - y
    elif operation == 'mul':
        return x * y
    elif operation == 'div':
        return x / y  # Ensure y is not zero to avoid ZeroDivisionError
    else:
        raise ValueError("Invalid operation. Use 'add', 'sub', 'mul', or 'div'.")
