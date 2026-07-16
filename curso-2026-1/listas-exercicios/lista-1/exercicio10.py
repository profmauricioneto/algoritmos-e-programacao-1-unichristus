valor_total = float(input("Digite o valor total da venda: "))

print(f"total a pagar com desconto: {valor_total * 0.9}")
print(f"valor da parcela em 3x sem juros: {valor_total/3}")
print(f"comissão do vendedor por venda a vista: {(valor_total * 0.9)*0.05}")
print(f"comissão do vendedor por venda parcelada: {valor_total * 0.05}")