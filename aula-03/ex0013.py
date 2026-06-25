salario = float(input("R$ Salario atual: "))
aumento = salario * 15 /100
novo_salario = salario + aumento
print(f"\nSalario anterior: R${aumento:.2f}")
print(f" aumento (15%):  R${aumento:.2f}")
print(f"novo salario: R${novo_salario:.2f}")
