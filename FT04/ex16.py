# Escreva um programa que peça ao utilizador números entre 0-10. Se o utilizador inserir um número fora desse intervalo o programa deverá finalizar com uma mensagem personalizada.

Number = int(input("Insira um número entre 0-10: "))
if number < 0 or number > 10:
    print("Número fora do intervalo permitido.")
    exit()
else:
    print("Número dentro do intervalo permitido.")