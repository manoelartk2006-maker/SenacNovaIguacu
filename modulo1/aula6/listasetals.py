

compras2 = [
    "amaciante", "papel toalha", "farinha", "maçã","pão de forma"
]

compras_final = compras + compras2
print(compras_final)

compras3 = [
    "laranja",
    "maçã",
    "hamburguer",
    "sal"
]
 
compras_final += compras3
print(compras_final)

# compras_final += ["café"]
# compras_final.append("café")
compras_final.insert(2,"café")
# print(compras_final)
compras_final.pop(3)
compras_final.remove("maçã")
compras_final.pop()
compras_dezembro=compras_final.copy()
print(compras_dezembro)

compras_final.count("maçã")
compras_final.clear()

print(compras_final)
print(compras_dezembro)

#############################
