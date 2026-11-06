 ##Desafio 1: Ordenação de Três Números 

# Recebidos 3 números inteiros, crie um programa que os mostre ordenados em ordem 
# crescente. 
# ●  Dica: Este desafio exige que você use estruturas if aninhadas ou uma série de testes 
# usando operadores de comparação para determinar qual número é o menor, o do 
# meio e o maior. 


# Desafio 2: Cálculo de Média e Status do Estudante 

# Dadas as 4 notas de um estudante, calcule sua média e, com base nela, emita a mensagem 
# de status correspondente: 
# 1.  Aprovado: Média estritamente maior que 7. 
# 2.  Recuperação: Média entre 5 (inclusive) e 7 (inclusive). 
# 3.  Reprovação: Média estritamente abaixo de 5. 
 


nota_1 = 8
nota_2 = 6
nota_3 = 4
nota_4 = 4

media =(nota_1 + nota_2 + nota_3 + nota_4)/4

if media >= 7:
    print(media, "aprovado")

elif media <5:
    print(media, "reprovado")

else:
    print(media, "recuperação")

