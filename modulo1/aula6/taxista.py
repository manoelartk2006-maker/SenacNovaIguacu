# 3. Rendimento do Taxista: 
# Um motorista de táxi deseja calcular o rendimento de seu carro na praça. Sabendo-se que o 
# preço do combustível é de R$ 6,15, escreva um programa para ler: a marcação do 
# odômetro (km) no início do dia, a marcação (km) no final do dia, o número de litros de 
# combustível gasto e o valor total (R$) recebido dos passageiros. Calcular e escrever: a 
# média do consumo em km/L e o lucro (líquido) do dia

preco_combustivel = 6.15

odometro_inicio = float(input("digite a marcação do odometro no início do dia (em km): "))
odometro_fim = float(input("digite a marcação do odometro no fim do dia (em km): "))
litros_de_gazolina_gasta = float(input("digite o número de litros de combustível gasto: "))
total_recebido_dos_passageiros = float(input("digite o total recebido dos passageiros"))

media = (odometro_fim - odometro_inicio) / litros_de_gazolina_gasta
lucro = total_recebido_dos_passageiros - (litros_de_gazolina_gasta * preco_combustivel)

print(f"a média do consumo em km/L é: {media:.2f}")
print(f"o lucro líquido do dia é: R$ {lucro:.2f}")
