#Programa que mostre todas as tabuadas

i = 1
while i <= 10:
    print(f'Tabuada do {i}:')
    j = 1
    while j <= 10:
        print(f'{i} x {j} = {i * j}')
        j += 1
    i += 1    