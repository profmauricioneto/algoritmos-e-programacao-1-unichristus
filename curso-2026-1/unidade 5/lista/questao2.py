def converter_tempo(horas, tipo):
    if (tipo == 'h'):
        return horas
    elif (tipo == 'm'):
        return horas*60
    elif (tipo == 's'):
        return horas*60*60
    else:
        print(f'Tipo Inválido!')
        return 0
    
def main():
    horas = float(input('Digite a quantidade de horas: '))
    tipo = input('Digite o tipo de hora (h = horas, m = minutos e s = segundos): ')
    
    resultado = converter_tempo(horas, tipo)
    
    print(f'Conversão de {horas}h para {tipo} = {resultado}')

main()