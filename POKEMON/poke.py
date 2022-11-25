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
print("> CARGANDO POKEMONS DESDE ARCHIVO CSV")
print("  ATENCIÓN: CSV con cabeceras")
print("  ATENCIÓN: Se han detectado pokemons con números repetidos")
pokemons.loadPokemons()
print("  Se han cargado [" + str(len(pokemons)) + "]")
print("")

# Crear una arbol por NOMBRE de Pokemonn
print("> INDEXANDO POKEMOS POR NOMBRE")
pokeTree_nombre = PokeTree()
for pk in pokemons:
    pokeTree_nombre.insert(pk.nombre, pk)
print("  El índice se ha creado con éxito")
print()

# Crear una arbol por NÚMERO de Pokemonn
print("> INDEXANDO POKEMONS POR NÚMERO")
pokeTree_numero = PokeTree()
for pk in pokemons:
    pokeTree_numero.insert(pk.numero, pk)
print("  El índice se ha creado con éxito")
print()

# Crear una arbol por TIPO de Pokemonn
print("> INDEXANDO POKEMONS POR TIPO")
pokeTree_tipo = PokeTree()
for pk in pokemons:
    pokeTree_tipo.insert(pk.tipo1, pk)
for pk in pokemons:
    pokeTree_tipo.insert(pk.tipo2, pk)
print("  El índice se ha creado con éxito")
print()

# Buscando Pokemons por NÚMERO
print("> BUSCANDO POKEMONS POR NUMERO (incluye duplicados)")
print("* Clave [6]: ", pokeTree_numero.search(3), "\n")
print("* Clave [700]: ", pokeTree_numero.search(6), "\n")
print("* Clave [6578]: ", pokeTree_numero.search(6578), "\n")

# Buscando Pokemons por NOMBRE
print("> BUSCANDO POKEMONS POR NOMBRE")
print("* Clave [Oddish]: ", pokeTree_nombre.search("Oddish"), "\n")
print("* Clave [GengarMega Gengar]: ",
      pokeTree_nombre.search("GengarMega Gengar"), "\n")
print("* Clave [OMG]: ", pokeTree_nombre.search("OMG"), "\n")

# Ver todos los TIPOS DE POKEMONS
print("> VER TODOS LOS TIPOS DE POKEMONS")
print( pokeTree_tipo.showKeysInPreorder())
print()

# Contar Pokemons por tipo
print("> CONTAR POKEMONS POR TIPO")
for tipo in pokeTree_tipo.showKeysInPreorder():
    print("* Clave ["+ tipo + "]:", (pokeTree_tipo.search(tipo)).showQuatity())
print()

# Mostrar todos los pokemons que hay de un TIPO
print("> VER TODOS LOS POKEMONS DE CIERTO TIPO ORDENADOS POR NOMBRE")
print("* Clave [Ice]: ", (pokeTree_tipo.search("Ice")).sortByName().showName(), "\n")

# Ver todos los TIPOS DE POKEMONS
print("> VER TODOS LOS TIPOS DE POKEMONS ORDENADOS POR NOMBREEE")
print( pokeTree_nombre.showKeysInPreorder())
print()