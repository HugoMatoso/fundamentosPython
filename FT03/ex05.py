# Escreva um programa que verifique se um determinado número introduzido pelo utilizador é nulo, positivo ou negativo

num = int(input("Introduza um número: "))

if num == 0:
    print(f"O número {num} é nulo")
elif num > 0:
    print(f"O número {num} é positivo")
else:
    print(f"O número {num} é negativo")