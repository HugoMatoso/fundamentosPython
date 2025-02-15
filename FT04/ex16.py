# Escreva um programa que peça ao utilizador números entre 0-10. Se o utilizador inserir um número fora desse intervalo o programa deverá finalizar com uma mensagem personalizada.

while True:
    n = int(input("Introduza um número entre 0 e 10: "))
    if n < 0 or n > 10:
        print("Número fora do intervalo.")
        break
    print(n)