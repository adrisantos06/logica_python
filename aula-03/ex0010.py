cotacao_usd = 5.15 # cotação referência
real = float(input('R$ Quanto você tem na carteira?)'))
dolar = real / cotacao_usd
print(f"Com R$ {real:.2f} você pode comprar " f"US$ {dolar:.2f}")
      