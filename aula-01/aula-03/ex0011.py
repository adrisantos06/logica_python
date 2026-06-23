largura = float(input("largura da parede (m): "))
altura = float(input("altura da parede (m): "))
area = largura * altura 
tinta = area / 2 
print(f'\nSua parede: {largura} x {altura} m')
print(f'Area total: {area:.3f} m2')
print(f'tinta necessaria: {tinta:.4f} litros')
