#Python Program to Find the Square of Number Taken from User as Input
User_Input = float(input())

result = User_Input * User_Input
formatted_Result = "{:.4f}".format(result)

print("The Result of Square of Given Number is : ", formatted_Result)