# validação de usuario.
username = input('Digite seu username: ')
if (username.lower() == "maumneto"):
    print('Acesso Liberado!')
else: 
    print('Acesso Negado!')

# validação de email
email = input('Digite seu email: ')
valido = ("@" in email and "." in email)
if (valido == True):
    print('Email validado!')
else:
    print('Email não válido!')

# validação basica de CPF
cpf = input('Digite seu CPF: ')
cpf_valido = ("-" not in cpf)
indice_valido = cpf.find('-')
print(indice_valido)
if (cpf_valido == True and indice_valido != 11):
    print('CPF não esta no padrão')
else:
    print('CPF esta no padrão.')