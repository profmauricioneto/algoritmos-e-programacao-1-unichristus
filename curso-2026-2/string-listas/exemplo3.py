continuar = input('Deseja continuar? [s/n] ').upper()
if (continuar.startswith('S')):
    print('Continuar')
    
    
mensagem = 'hello world'
print(mensagem.capitalize())
print(mensagem.title())

temHello = "hello" in mensagem.lower()
print(temHello)