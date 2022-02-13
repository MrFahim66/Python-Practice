salary = float(input())

if(salary<= 400.00):
    percent = 15
    increase = (salary/100)*percent
    new_salary = salary + increase
elif(salary>= 400.01 and salary <= 800.00):
    percent = 12
    increase = (salary/100)*percent
    new_salary = salary + increase
elif(salary>= 800.01 and salary <= 1200.00):
    percent = 10
    increase = (salary/100)*percent
    new_salary = salary + increase
elif(salary>= 1200.01 and salary <= 2000.00):
    percent = 7
    increase = (salary/100)*percent
    new_salary = salary + increase
elif(salary> 2000.00):
    percent = 4
    increase = (salary/100)*percent
    new_salary = salary + increase

print("Novo salario: %0.2f"%new_salary)
print("Reajuste ganho: %0.2f"%increase)
print("Em percentual:",percent,"%")