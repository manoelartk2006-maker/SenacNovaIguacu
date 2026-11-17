 
# 2. Quantidade de Caixas de Azulejos: 
# Escreva um programa para ler as dimensões de uma cozinha retangular (comprimento, 
# largura e altura), calcular e escrever a quantidade de caixas de azulejos para se colocar em 
# todas as suas paredes (considere que não será descontada a área ocupada por portas e 
# janelas). Cada caixa de azulejos possui 1,5 m²

comprimento = float(input("qual é o comprimento da cozinha?:"))
largura = float(input("qual é a largura da cozinha?:"))
altura = float(input("qual é a altura da cozinha?:"))

área_das_paredes = 2 * (comprimento + largura) * altura
quantidade_de_caixas = área_das_paredes / 1.5

print(f"serão necessarias {quantidade_de_caixas} caixas de azulejos para revestir as paredes da cozinha.")