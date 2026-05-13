# função de verificação da senha
def verificar_senha(senha):
    if (len(senha) >= 8 and len(senha) <= 12):
        return True
    else:
        return False
    
# Função principal
def main():    
    while(True):
        senha = input('Digite sua senha (entre 8 e 12 caracteres): ')

        eh_valido = verificar_senha(senha)
        
        if (eh_valido):
            print('Senha Válida!')
            break
        else:
            print('Senha Inválida! Forneça outra senha de acordo com o as regras!')
    
    
    # if (eh_valido):
    #     print('Senha válida!')
    # else:
    #     print('Senha Inválida! Forneça outra senha de acordo com o as regras!')

# Chamada da função principal!
main()