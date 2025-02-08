#Fazer um programa para ler números inteiros e positivos, calcular e devolver a sua média aritmética.

numeros = []
soma = 0
quantidade = 0
while True:
    num = int(input("Digite um número inteiro e positivo: "))
    if num > 0:
        soma += num
        quantidade += 1
        numeros.append(num)
    else:
        