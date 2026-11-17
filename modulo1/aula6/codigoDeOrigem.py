# 4. Código de Origem do Produto: 
# Escreva um programa que leia o código de origem de um produto e imprima na tela a região 
# de sua procedência, conforme a tabela abaixo: 
 
# Observação: caso o código não seja nenhum dos especificados, o produto deve ser 
# encarado como “Importado”





codigo = int(input("digite o codigo de origem:"))

match codigo:
    case 1:
        print("produto proveniente do sul")
    case 2:
        print("produto proveniente do norte")
    case 3:
        print("produto proveniente do leste")
    case 4:
        print("produto proveniente do Oeste")
    case 5| 6:
        print("produto proveniente do nordeste")
    case 7| 8 | 9:
        print("produto proveniente do sudeste")
    case 10:
        print("produto proveniente do centro oeste")
    case 11:
        print("produto proveniente do Noroeste")
    case _:
        print("produto importado")


