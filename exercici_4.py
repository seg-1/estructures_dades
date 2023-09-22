"""
- Exercici 4

Crea un diccionari de la següent forma i respon a les preguntes:
compra = { "Pomes" : {"Qty": 5, "€": 0.42}, "Peres" : {"Qty": 3, "€": 0.66} }

    Afegeix alguna fruita més
    Quant han costat les peres en total?
    Quantes fruites hem comprat en total?
    Quina és la fruita més cara?

"""
quantitat_fruites = 0
compra = {"Pomes": {"Qty": 5, "€": 0.42}, "Peres": {"Qty": 3, "€": 0.66}}
max_preu = 0

# Afegim més fruites al diccionari
compra["Platans"] = {"Qty": 4, "€": 0.50}
compra["Taronjes"] = {"Qty": 2, "€": 0.65}

# calculem el cost total de les peres
total_peres = compra["Peres"]["Qty"] * compra["Peres"]["€"]
print("Les peres han costat en total:", total_peres, "€")

# contem la quantitat total de fruites comprades
for quantitat in compra.values():
    quantitat_fruites = quantitat_fruites + quantitat["Qty"]

print("Hem comprat", quantitat_fruites, "peces de fruita\n")

# Busquem la fruita mes cara
# Recorrem les claus per a poder extreure els valors de cada fruita
# Comparem els preus
for nom_fruita in compra.keys():

    valor_dic_fruita = compra[nom_fruita].values()
    i = 0

    print("El nom de la fruita es:", nom_fruita)

    for preu in valor_dic_fruita:

        if i == 1:
            print("El preu de", nom_fruita, "es de:", preu, "\n")
            if max_preu < preu:
                max_preu = preu
        i = i + 1

print("El preu mes alt es:", max_preu)