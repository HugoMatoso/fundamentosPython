import math

#Pedir ao usuário para digitar um número inteiro e devolver a sua raiz quadrada

numero = int(input("Digite um número inteiro: "))
raizquadrada = math.sqrt(numero)

print("A raiz quadrada do número:",numero,"é igual a", round(raizquadrada,2))

#formatação posicional %d para inteiro %s string e %f para decimal
print("A raiz quadrada do número: %d é igual a %f"%(numero,round(raizquadrada,2)))

#usando format
print("A raíz quadrada do número: {} é igual a {}".format(numero,round(raizquadrada,2)))

#mais atual e mais eficiente
print(f"A raíz quadrada do número: {numero} é igual a {round(raizquadrada,2)}")