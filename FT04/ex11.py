# Escreve um programa que calcule a soma e o produto dos N primeiros números naturais. O valor de N é introduzido pelo utilizador.

n = int(input("Introduza um número: "))
soma = 0
produto = 1

while n > 0:
    soma += n
    produto *= n
    n -= 1
    
print(f"Soma: {soma}")