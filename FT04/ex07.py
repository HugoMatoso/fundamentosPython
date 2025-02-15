#Elabora um programa para calcula a soma dos N primeiros números naturais (1+2+3+...+N) em que N é um número introduzido pelo utilizador (NOTA: este programa poderia ser feito utilizando a fórmula da progressão aritmética, S = (1+N) * N/2, mas faz de conta que não sabíamos a fórmula).

n = int(input("Introduza um número: "))
soma = 0

while n > 0:
    soma += n
    n -= 1
print(f"A soma dos {n} primeiros numeros naturaus é: {soma}")