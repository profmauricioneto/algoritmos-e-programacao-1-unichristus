# criando a função converter_tempo
def converter_tempo(num_horas, tipo):
    if (tipo.lower() == 'h'):
        return num_horas
    elif (tipo.lower() == 'm'):
        return num_horas * 60
    elif (tipo.lower() == 's'):
        return num_horas * 3600
    else:
        print(f'Erro! tipo {tipo} não suportado pela função!')
        return 0
    
# Função Principal! 
def main():
    num_horas = int(input('Diga o valor em horas: '))
    tipo = input('Digite o tipo de tempo (h/m/s)? ')
    
    valor_convertido = converter_tempo(num_horas, tipo)
    
    if (valor_convertido != 0):
        print(f'Conversão de {num_horas} em {tipo} = {valor_convertido}')
    
main()