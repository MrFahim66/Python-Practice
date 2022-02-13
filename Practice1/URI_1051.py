salary = float(input())

if(salary and salary <= 2000):
    print("Isento")
elif(salary >= 2000.01 and salary<= 3000.00):
    salary2 = salary -2000
    tax = salary2 * 0.08
    print("R$ %0.2f"%tax)
elif(salary >= 3000.01 and salary<= 4500.00):
    salary2 = salary - 3000
    tax = (salary2*0.18) + (1000*0.08)
    print("R$ %0.2f"%tax)
elif(salary > 4500.00):
    salary2 = salary - 4500
    tax = (salary2*0.28) + (1500*0.18) + (1000*0.08)
    print("R$ %0.2f"%tax)
