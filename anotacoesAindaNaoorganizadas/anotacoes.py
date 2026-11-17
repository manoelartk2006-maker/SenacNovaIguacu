####conceito de função!!!!!!!!!!

##TODAS AS FIRULAS QUE O PYTHON DISPOE


print("*"*40) #multiplica '*' 40 vzs
print("ATENDIMENTO")
print("*"*40)
print("para iniciarmos seu atendimento, por favor digite seu nome e cpf")
nome_user = input("nome:")
id_user = input("CPF:")


def menu_inicial( nome_user, id_user): #tudo que a dentro da função so aontece quando ela é invocada.
    
    print("*"*40) #multiplica '*' 40 vzs
    print("ATENDIMENTO")
    print("*"*40)
    print("para iniciarmos seu atendimento, por favor digite seu nome e cpf")
    # nome_user = input("nome:")
    # id_user = input("CPF:")
    print(f"olá, {nome_user}! Seu indentificador informado é {id_user}.")




#####novos elementos
    
# menu_inicial()  ###### posso usar esse comando para chama a função
    
##3 podemos invocar a função dessa forma tmb
    
inicio_do_sistema = menu_inicial(nome_user, id_user)

# menu_inicial
    
##novos nomes para variaves ""argumento ou paramento



