import random
##By: spiderckz
##Gay: nerox
print("| CC GENERATOR |")
print("| BY SPIDERCKZ |")
print('versão 1.0')
print ("telegram: t.me/spiderckz")
print('--------------------------------------------------------')
y = True
Y = True
N = False
n = False
list = [2021, 2022, 2023, 2024, 2025, 2026, 2027, 2028]
nume = random.randrange(1, 9999999999999999)
cvv = random.randint(3, 999)
data1 = random.randrange(1, 31)
data2 = random.randrange(1, 12)
data3 = random.choice(list)
cpf = random.randrange(1, 99799989999)

bi = str(input('Gerar várias ccs? y/n?: '))

if bi == 'y':
    nume2 = random.randrange(1, 9999999999)
    bin = int(input('Bin de 6 números: '))
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    nume2 = random.randrange(1, 9999999999)
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    nume2 = random.randrange(1, 9999999999)
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    nume2 = random.randrange(1, 9999999999)
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    nume2 = random.randrange(1, 9999999999)
    print('CC:', bin, nume2)
    print('Cvv:',cvv)
    print('Vencimento:', data1, data2, data3)
    print('CPF:', cpf)
    print('--------------------------------------------------------')
    
else:
    nume2 = random.randrange(1, 9999999999)
    print('💳CC:', nume2)
    print('🔐Cvv:', cvv)
    print('📆Vencimento:', data1, data2, data3)
    print('📃CPF:', cpf)
    print('--------------------------------------------------------')
  
