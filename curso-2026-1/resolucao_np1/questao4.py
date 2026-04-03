COMISSAO = 4.5
VALOR_KM = 1.2
BONUS = 0.15

quantidade_entregas = int(input("Quantidade de entregas: "))
distancia = float(input("Distancia (km): "))
tempo_medio = int(input("Tempo médio (minutos): "))

valor_total_comissao = quantidade_entregas * COMISSAO
print(f"Valor total das comissões fixas: {valor_total_comissao: .2f}")
valor_total_km = distancia * VALOR_KM
print(f"Valor total por quilometragem: {valor_total_km: .2f}")

tempo_bonus = 0
if (tempo_medio < 25):
    tempo_bonus = tempo_medio * BONUS
print(f"Valor total do bônus por tempo: {tempo_bonus: .2f}")

valor_total_receber = valor_total_comissao + valor_total_km + tempo_bonus
print(f"Valor total a receber (R$): {valor_total_receber: .2f}")