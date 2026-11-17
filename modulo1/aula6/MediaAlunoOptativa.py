
nota1 = float(input("Digite a nota da primeira avaliação: "))
nota2 = float(input("Digite a nota da segunda avaliação: "))    
nota_op = input("O aluno fez a avaliação optativa? (s/n): ").lower()




if nota_op.lower() == "s":
    print(float(input("qual a nota da optativa?")))
    
    if nota_op > nota1:
        media = (nota2 + nota_op )/2

    elif nota_op > nota2:
        media = (nota1 + nota_op )/2
    else:
        media = (nota1 + nota2)/2
    

elif nota_op.lower() =="n":
    nota_op = -1


media = ((nota1 + nota2)/2)-1

5
if media >= 6.0:
    print (f"aprovado!!, sua media é : {media}")

elif media < 3.0:
    print(f"reprovado... sua media é :{media}" )

else:
    print(f"quase... recuperação, sua media é {media}")