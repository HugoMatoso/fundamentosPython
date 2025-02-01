# Escreve um programa que solicite um número inteiro ao utilizador e verifique se o mesmo é par ou ímpar

num = int(input("Digite um número: "))

if num % 2 == 0:
    print(f"O número {num} é par")
else:
    print(f"O número {num} é ímpar")