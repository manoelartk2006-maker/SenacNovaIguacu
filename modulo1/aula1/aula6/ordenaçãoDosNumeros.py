
n1 = int(input("qual é o primeiro numero?"))
n2 = int(input("qual é o segundo numero?"))
n3 = int4(input("qual é o terceiro numero?"))


if n1 > n2:
    n1, n2 = n2, n1

elif n1 > n3:
    n1, n3 = n3, n1

elif n2 > n3:
    n2, n3 = n3, n2


print("a Ordem crescente dos numeros é: ", n1, n2, n3)