
# Ejemplos de lista
ejemplo_lista = ["pineapple","orange","blueberry","orange"]
print ("Lista: ")
print (ejemplo_lista)
print ("Listas - Indice 2: " + ejemplo_lista[2])
print ("Listas - Indice 0: " + ejemplo_lista[0])

# Ejemplos de diccionario
dictionary = {
  1: "Lunes",
  2: "Martes",
  3: "Miercoles",
  4: "Jueves",
  5: "Viernes",
  6: "Sábado",
  7: "Domingo",
}

print ("Dictionary - Dia 3: " + dictionary.get(3))

dictionary2 = {
    "name" : "Arlyn",
    "last_name" : "Chavarría",
    "gender" : "female",
    "has_job" : 1
}

print ("Dictionary - Nombre completo: " + dictionary2.get("name") + " " + dictionary2.get("last_name"))

# Ejemplos de tuplas
ejemplo_tuple = ("pineapple","orange","tomato","blueberry","tomato")
print ("Tupla:")
print (ejemplo_tuple)
print ("Tuplas - Indice 1: " + ejemplo_tuple[1])
print ("Tuplas - Indice 3: " + ejemplo_tuple[3])


# Ejemplos de Conjuntos
ejemplo_set = {"Hola", "este", "es", "un", "conjunto","conjunto"}
print("Conjunto: ")
print(ejemplo_set)
