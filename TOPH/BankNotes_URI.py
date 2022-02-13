from math import *
initial_value = input()

value = float(initial_value)

note100 = floor(value / 100)
value = value-(note100*100)

note50 = floor(value / 50)
value = value - (note50*50)

note20 = floor(value / 20)
value = value - (note20*20)

note10 = floor(value / 10)
value = value - (note10*10)

note5 = floor(value / 5)
value = value - (note5*5)

note2 = floor(value / 2)
value = value - (note2*2)

coin1 = floor(value / 1)
value = value - (coin1*1)

coin0_50 = floor(value / 0.50)
value = value - (coin0_50*0.50)

coin0_25 = floor(value / 0.25)
value = value - (coin0_25*0.25)

coin0_10 = floor(value / 0.10)
value = value - (coin0_10*0.10)

coin0_05 = floor(value / 0.05)
value = value - (coin0_05*0.05)

coin0_01 = floor(value / 0.01)
value = value - (coin0_01*0.01)

print('NOTAS:')
print(note100, "nota(s) de R$ 100.00")
print(note50, "nota(s) de R$ 50.00")
print(note20, "nota(s) de R$ 20.00")
print(note10, "nota(s) de R$ 10.00")
print(note5, "nota(s) de R$ 5.00")
print(note2, "nota(s) de R$ 2.00")
print('MOEDAS:')
print(coin1, "moeda(s) de R$ 1.00")
print(coin0_50, "moeda(s) de R$ 0.50")
print(coin0_25, "moeda(s) de R$ 0.25")
print(coin0_10, "moeda(s) de R$ 0.10")
print(coin0_05, "moeda(s) de R$ 0.05")
print(coin0_01, "moeda(s) de R$ 0.01")