#O Índice de Massa Corporal (IMC) é utilizado para medir o peso ideal de uma pessoa. Escreve um programa que peça o nome, a idade, o peso e a altura do utilizado e que, de seguida, calcule e mostre o resultado do seu IMC e classifique esse resultado

nome = input("Digite o seu nome: ")
idade = int(input("Digite a sua idade: "))
peso = float(input("Digite o seu peso (em kg): "))
altura = float(input("Digite a sua altura (em metros): "))
imc = peso / (altura ** 2)

print(f"O IMC de {nome} é {imc:.2f}.")
if imc < 18.5:
    print(f"{nome} está abaixo do peso.")
elif 18.5 <= imc < 25:
    print(f"{nome} está com o peso ideal.")
elif 25 <= imc < 30:
    print(f"{nome} está acima do peso.")
elif 30 <= imc < 40:
    print(f"{nome} está com obesidade.")
elif imc >= 40:
    print(f"{nome} está com obesidade mórbida.")