potencia_da_lampada = float(input("qual é a potência da lâmpada? (em watts):"))
largura = float(input("qual é a largura do quarto?:"))
comprimento = float(input("qual é o comprimento do quarto?:"))

área = largura * comprimento
potencia_total = área * 3

quantidade_de_lampadas = potencia_total/potencia_da_lampada

bocais_por_area = área / 3
print(f"serão necessários {bocais_por_area} bocais para iluminar o quarto.")

