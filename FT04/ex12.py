# Escreve um programa que calcule e escreva o resultado do fatorial de um número inteiro positivo Nsabendo que: n!=1*2*3*…*n. O valor de N é introduzido pelo utilizador.

n = int(input("Introduza um número: "))
fatorial = 1

while n > 0:
    fatorial *= n
    n -= 1
print(fatorial)