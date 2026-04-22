senha_correta = '1234'
bloqueado = True
for tentativa in range(1, 4):
    senha = input('Digite a senha: ')
    if (senha == senha_correta):
        print('acesso liberado!')
        bloqueado = False
        break
    else:
        print('senha incorreta!')

if (bloqueado):
    print('Numero de tentativas excedidas!')