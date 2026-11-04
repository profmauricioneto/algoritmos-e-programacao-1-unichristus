peso_pacote = int(input('Peso do Pacote: '))
destino = input('Destino [N/NE/CO/SE/S]: ').upper()
valor_pedido = float(input('Valor do Pedido: '))

VALOR_EXTRA = 3.5
frete = 0
total = 0

if (peso_pacote <= 0 or peso_pacote > 30):
    print('Não é possível enviar o pacote pelos correios!')
elif ((destino == 'NE' or destino == 'SE') and valor_pedido >= 299):
    print('Isenção de frete!')
    total = (peso_pacote - 1)*VALOR_EXTRA + valor_pedido + frete
else:
    if (destino == 'N'):
        frete = 32
        total = (peso_pacote - 1)*VALOR_EXTRA + valor_pedido + frete
    elif (destino == 'NE'): 
        frete = 24
        total = (peso_pacote - 1)*VALOR_EXTRA + valor_pedido + frete
    elif (destino == 'CO'):
        frete = 28
        total = (peso_pacote - 1)*VALOR_EXTRA + valor_pedido + frete
    elif (destino == 'SE'):
        frete = 20
        total = (peso_pacote - 1)*VALOR_EXTRA + valor_pedido + frete  
    else:
        frete = 22
        total = (peso_pacote - 1)*VALOR_EXTRA + valor_pedido + frete

print(f'frete = {frete}')
print(f'total = {total: .2f}')