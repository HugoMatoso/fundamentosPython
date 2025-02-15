#Fazer um programa para ler números inteiros e positivos, calcular e devolver a sua média aritmética. O programa deve terminar quando for introduzido um número negativo.

n = 0
soma = 0
while True:
    num = int(input("Introduza um número: "))
    if num < 0:
        break
    soma += num
    n += 1
if n == 0:
    print("Não introduziu números positivos.")
else:
    print("Média aritmética:", soma / n)