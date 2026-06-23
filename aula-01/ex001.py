def soma (n1,n2):
    resultado = n1 + n2
    return resultado 

def principal():
    numero1= int (input ("Digite numero 1:"))
    numero2= int (input ("Digite numero 2:"))
    somatorio = soma (numero1, numero2)
    print (" o somatorio é: " , somatorio)

principal()
