# Ejemplo de uso de arboles binarios para indexación
# y búsqueda de información en este caso de Pokemons
# Desarrollado por Ma~Ra

from PokeData_Class import *
from PokeTree_Class import *
from PokeNode_Class import *
from PokeDataSet_Class import *
from PokeList_Class import *

####  AÑADIR LOS COLORES AL FINAL!!!!!

# Cargar datos de pokemons del archivo CSV
print()
pokemons = PokeDataSet("pokemon.csv")
print("> Cargando Pokemons desde archivo CSV")
print("  ATENCIÓN: CSV con cabeceras")
print("  ATENCIÓN: Se han detectado pokemons con números repetidos")
pokemons.loadPokemons()
print("  Se han cargado [" + str(len(pokemons)) + "]")
print("")

# Crear una arbol por NOMBRE de Pokemonn
print("> Creando arbol de Pokemons indexado por NOMBRE")
pokeTree_nombre = PokeTree()
for pk in pokemons:
    pokeTree_nombre.insert(pk.nombre, pk)


# Crear una arbol por NÚMERO de Pokemonn
print("> Creando arbol de Pokemons indexado por NÚMERO")
pokeTree_numero = PokeTree()
for pk in pokemons:
    pokeTree_numero.insert(pk.numero, pk)

# Crear una arbol por TIPO de Pokemonn
print("> Creando arbol de Pokemons indexado por TIPO")
pokeTree_tipo = PokeTree()
for pk in pokemons:
    pokeTree_tipo.insert(pk.tipo1, pk)
for pk in pokemons:
    pokeTree_tipo.insert(pk.tipo2, pk)
print()


# Buscando Pokemons por NÚMERO
print("> Clave [3]:", pokeTree_numero.search(3), "\n")
print("> Clave [5]:",pokeTree_numero.search(6), "\n")
print("> Clave [1]:",pokeTree_numero.search(1), "\n")
print("> Clave [10]:", pokeTree_numero.search(10),"\n")
# print("> Clave [3]:", pt.search(None))
# print("> Clave [3]:", pt.search("Pepe"))


# Buscando Pokemons por NOMBRE


# Buscando Pokemons por TIPO
