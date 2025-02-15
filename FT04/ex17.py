# Escreva um programa que peça ao utilizador 20 números reais e no final mostre a soma e a médiados números introduzidos.

soma = 0
for i in range(20):
    n = float(input("Introduza um número: "))
    soma += n
print("Soma:", soma)
print("Média:", soma/20)