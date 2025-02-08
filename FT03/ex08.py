#Escreve um programa para classificar um triângulo de acordo com o comprimento dos seus lados. Considere as seguintes informações:

print("Introduza o comprimento dos lados do triângulo:")
l1 = float(input("Lado 1: "))
l2 = float(input("Lado 2: "))
l3 = float(input("Lado 3: "))

if l1 == l2 == l3:
    print("O triângulo é equilátero.")
elif l1 == l2 or l2 == l3 or l3 == l1:
    print("O triângulo é isósceles.")
else:
    print("O triângulo é escaleno.")