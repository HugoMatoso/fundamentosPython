# Escreve um programa que solicite ao utilizador um número e escreva em simultâneo a sequência crescente e decrescente entre 1 e esse número.

n = int(input("Introduza um número: "))
while n > 0:
    for i in range(1, n+1):
        print(i, end="  ")
        print(n, end="  ")
        n -= 1
        print()