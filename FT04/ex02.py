#Implemente um programa que, dada uma letra (S, C ou V), indique o estado civil de uma pessoa.
resposta = "S"
while resposta.upper() == "S":
    estadoCivil = input("Digite a letra correspondente ao estado civil (S, C ou V): ")
    match estadoCivil.upper():
        case "S":
            print("Solteiro")
        case "C":
            print("Casado")
        case "V":
            print("Viúvo")
        case _:
            print("Estado civil inválido")
    resposta = input("Deseja continuar? (S/N): ")