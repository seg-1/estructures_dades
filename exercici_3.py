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

# contem la quantitat de numeros que hi ha en la llista
contador_numeros = len(numeros)
print('En la llista hi ha:', contador_numeros, 'numeros')

# Veiem cuantes vegades apareix el numero 3
numero_3 = numeros.count(3)
print('El numero 3 apareix: ', numero_3, 'vegades en la llista')

# Veiem cuantes vegades apareix el numero 3 i 4
numero_3 = numeros.count(3), numeros.count(4)
print('Els numeros 3 i 4 apareixen:', numero_3, 'vegades en la llista')

# Busquem el numero més gran
max_numeros = max(numeros)
print('El numero més gran es el: ', max_numeros)

# Busquem els 3 numeros mes petits
num_ordenats = sorted(numeros)
print('Els tres numeros més petits son:', num_ordenats[0:3])

# Calculem el rang q de la llista
min_numeros = min(numeros)
print('El rang de la llista es:', max_numeros - min_numeros)
