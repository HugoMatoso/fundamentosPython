# Elabora um programa que pede ao utilizador para inserir dois números inteiros. O programa deve escrever todos os números inteiros entre os dois limites por ordem crescente. Utiliza o ciclo for.

n1 = int(input("Introduza um número: "))
n2 = int(input("Introduza outro número: "))
if n1 > n2:
    n1, n2 = n2, n1
for i in range(n1, n2+1):
    print(i, end=" ")
print()