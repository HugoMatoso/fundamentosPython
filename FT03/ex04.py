# Escreve um programa que receba dois números reais e indique qual o maior dos dois números. Considera a possibilidade de o utilizador indicar dois números iguais

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if num1 > num2:
    print(f"O maior número é {num1}")
elif num2 > num1:
    print(f"O maior número é {num2}")
else:
    print("Os numeros digitados foram iguais")