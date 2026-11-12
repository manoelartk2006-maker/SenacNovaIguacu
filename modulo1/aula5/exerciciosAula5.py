

for aluno in range (1, 11):
    print( "qual é a nota do", "aluno3",{aluno})

    nota_1 = float(input("digite sua nota:"))
    nota_2 = float(input("digite sua nota:"))
    nota_3 = float(input("digite sua nota:"))
    nota_4 = float(input("digite sua nota:"))

    media =(nota_1 + nota_2 + nota_3 + nota_4)/4

    if media >= 7:
        print(media, "aprovado")

    elif media <5:
        print(media, "reprovado")

    else:
        print(media, "recuperação")

print("-----------acabou!----------------")