"""
- Exercici 3

Crea una llista amb nombres desordenats i respon a les següents preguntes:

    Quants números hi ha?
    Quantes vegades apareix el número 3.
    Quantes vegades apareixen els nombres 3 i 4?
    Quin és el número més gran?
    Quins són els 3 números més petits?
    Quin és el rang d’aquesta llista?
"""

numeros = [5, 9, 10, 4, 44, 23, 70, 4]

contador_numeros = len(numeros)
print('En la llista hi ha:', contador_numeros, 'numeros')

numero_3 = numeros.count(3)
print('El numero 3 apareix: ', numero_3, 'vegades en la llista')

numero_3 = numeros.count(3), numeros.count(4)
print('Els numeros 3 i 4 apareixen:', numero_3, 'vegades en la llista')

max_numeros = max(numeros)
print('El numero més gran es el: ', max_numeros)

min_numeros = min(numeros)

print('El rang de la llista es:', max_numeros - min_numeros)
