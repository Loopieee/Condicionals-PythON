numeros = []
con = 1
while con <= 10:
    numeros = int(input("Introduce los numeros:"))
    con-=1

pares = []
impares = []
for numero in numeros:
    if(numero%2==0):
        pares.append(numero)
    else:
        impares.append(numero)


