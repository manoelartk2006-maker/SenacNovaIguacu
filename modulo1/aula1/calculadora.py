

#o usuario precisa inserir 2 numeros e o algoritimo vai calcular o resultado desses numeros

n1 = float(input("digite o primeiro numero:"))
n2 = float(input("digite o segundo numero:"))

operacao = input("qual operação você deseja realizar? (soma, subtração, multi, divisão, média):")

if operacao == "soma":
    print("o resultado da soma é:", n1 + n2)
elif operacao == "divisão":
    print("o resultado da divisão é:", n1 / n2)
elif operacao == "multi":
    print("o resultado da multiplicação é:", n1 * n2)
elif operacao == "subtração":
    print("o resultado da subtração é:", n1 - n2)
elif operacao == "média":
    print("a média é:", (n1 + n2) / 2)

if operacao not in ["soma", "subtração", "multiplicação", "divisão", "média"]:
    print("operação inválida, por favor escolha uma das opções válidas.")