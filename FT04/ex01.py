#Faz um programa que escreva o nome do mês que é introduzido, pelo utilizador, na forma numérica.

mes = input("Introduza o nome do mês: ")
match mes:
    case "Janeiro":
        print("1")
    case "Fevereiro":
        print("2")
    case "Março":
        print("3")
    case "Abril":
        print("4")
    case "Maio":
        print("5")
    case "Junho":
        print("6")
    case "Julho":
        print("7")
    case "Agosto":
        print("8")
    case "Setembro":
        print("9")
    case "Outubro":
        print("10")
    case "Novembro":
        print("11")
    case "Dezembro":
        print("12")
    case _:
        print("Mês não encontrado")