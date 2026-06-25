nome = str(input("digite seu nome completo: ")). strip()

print(f" Em MAIUSCULA: {nome.upper()}")
print(f" Em minisculas: {nome.lower()}")

total_letras = len(nome) - nome.count(" ")
print(f' total de letras (sem espaços): {total_letras}')

partes = nome.split()
primeiro = partes[0]
print(f"Seu primeiro nome é '{primeiro}' e tem {len(primeiro)} letras")

