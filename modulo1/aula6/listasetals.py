## listas
            #   1         2       3
compras = ["arroz", "feijão","sabão","açucar","pão"]


compras2 =  ["amaciante", "papel toalha", "farinha", "maçã","pão"]



# print(compras2 [2])

# print(compras2[2:3])

# print(compras2[0:4:2])

# print(len(compras2))
# print(compras2[0:8:2])

compras_final = compras + compras2

# print(compras_final)

compras3 = [
    "laranja",
    "maçã",
    "hamburguer",
    "sal"
]

compras_final = compras_final  + compras3



# compras_final += compras3

compras_final += ["café"]

# print(compras_final)

# compras.append("café")
#adicionando algo na lista usando o comando "apend" ele vai para o final da lista


compras_final.insert(2,"café")
##modificar a lista e sua ordem


compras_final.pop
##se o append adiciona, o pop retira do final, porém é necessario por o indice a ser retirado


compras_final.remove("maçã")
##ele remove a primeira ocorrencia

compras_dezembro= compras_final.copy()

compras_final.count("maçã")
compras_final.clear()

# print(compras_final)
# print(compras_dezembro)


#TUPLASSS

# tupla_compras = tuple(compras_dezembro)
# ##sequencia imutavel

# # print(tupla_compras)
# # tuplas_compras.append("saleiro")

# add_tupla = ("leite")



# filmesFinalSemana = {
#     "o menino e a garça",
#     "as branquelas",
#     "premunição",
#      "avenges",
#     "diarios de uma paixão",
#     }

# print(filmesFinalSemana)

##dicionarios

# filmes = {
#     "titanic": 1996,
#     "como treinar seu dragão": 2010,
#     "Shrek": 2001
#     "star wars IV": 1997
    
# }

# print(filmes["titanic"][1])
# eu posso ter uma lista dentro de uma lista


nomes_filmes = ["titanic","shrek"]
ano_lançamento_filmes = [1997, 2001]
genero_filmes = ["drama/romance", "comedia/animação"]
indicacoes_oscar = ["sim","sim"]

