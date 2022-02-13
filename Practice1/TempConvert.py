print("Choose Preferred Action : \n1. Fahrenheit to Celcius    2. Celcius to Fahrenheit")
userInput = int(input())

if(userInput == 1):
    print("Enter Temparature in Fahrenheit :")
    fahrenheit = float(input())
    print(fahrenheit,"In Celcius is :",'%.4f' %(5/9 * (fahrenheit-32)))
elif(userInput == 2):
    print("Enter Temparature in Celcius :")
    celcius = float(input())
    print(celcius,"In Fahrenheit is :",'%.4f'%((celcius * 9/5)+32))