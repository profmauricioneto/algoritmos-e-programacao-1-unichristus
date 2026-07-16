# Construa uma função que receba uma string como parâmetro e devolva outra string com os caracteres embaralhados. Por exemplo: se a função receber a palavra python, pode retornar npthyo, ophtyn ou qualquer outra combinação possível, de forma aleatória. Padronize em sua função que todos os caracteres serão devolvidos em caixa alta ou caixa baixa, independentemente de como foram digitados.

import random

def embaralhar_palavra(palavra):
    palavra_capitalizada = palavra.upper()
    print(palavra_capitalizada)
    palavra_aleatoria = []
    for i in range(0, len(palavra_capitalizada)):
        palavra_aleatoria.append(palavra_capitalizada[random.randint(0, len(palavra_capitalizada)-1)])
    return palavra_aleatoria
    
print(embaralhar_palavra('teste'))