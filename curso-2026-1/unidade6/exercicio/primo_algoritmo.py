def verificar_primo(num):
    eh_primo = True
    for j in range(2, num):
        if (num % j == 0):
            eh_primo = False
    return eh_primo

def main():
    valores = [0]*9
    for i in range(0, 9):
        valores[i] = int(input('Digite um valor inteiro: '))
    # print(valores)

    for i in range(0, 9):
        eh_primo = verificar_primo(valores[i])             
        if eh_primo:
            print(f"O valor {valores[i]} é primo")
        else: 
            print(f"O valor {valores[i]} NAO é primo")
            
main()