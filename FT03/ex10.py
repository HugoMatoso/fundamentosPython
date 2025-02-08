#Implemente uma calculadora simples com as operações aritméticas básicas. O utilizador deverá especificar a operação desejada (+,-,*,/) e, em seguida, inserir dois valores. Caso, o utilizador escolha divisão e insira como valor do denominar 0 mostra uma mensagem personalizada. Para os restantes casos, mostra no ecrã o resultado da operação desejada.

print ("Calculadora simples")
print ("1 - Soma")
print ("2 - Subtração")
print ("3 - Multiplicação")
print ("4 - Divisão")
op = int(input("Escolha a operação desejada: "))
num1 = float(input("Insira o primeiro valor: "))
num2 = float(input("Insira o segundo valor: "))
if op == 1:
    print("O resultado da soma é: ", num1 + num2)
elif op == 2:
    print("O resultado da subtração é: ", num1 - num2)
elif op == 3:
    print("O resultado da multiplicação é: ", num1 * num2)
elif op == 4:
    print("O resultado da divisão é: ", num1 / num2)