matriz = [[1,25,8,3,50],[4,8,50,100,21]]
diferencia_total = 0
for numeros in matriz:
    print(numeros)
# con esto pasamos por cada item de la lista que tengo pensada crea.
    position = -1
    comparador = 0
    for numero in numeros:
        position += 1
        
        if numero <= numeros[position]:
            comparador += 1
            
            if comparador == len(numeros):
                diferencia_total -= numero
        else:
            continue
            
print(diferencia_total)        