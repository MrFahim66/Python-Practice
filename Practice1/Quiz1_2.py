def FunctionWithParameter(number1, number2, number3):
    result = number1 + number2 + number3
    return result

def Function_WithInitializeValue(A=10, B=5):
    C = A-B
    return C

def Function_WithoutParameters():
    print("This is The Function Which Does Not Contain Any Parameters!")

print("Calling Function With 3 Parameters:")
print(FunctionWithParameter(50, 75, 100))
print("\nCalling Function With Initialized Parameters:")
print(Function_WithInitializeValue())
print("\nCalling Function With No Parameters:")
Function_WithoutParameters()