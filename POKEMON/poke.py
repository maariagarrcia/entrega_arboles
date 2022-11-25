# Ejemplo de uso de arboles binarios para indexación
# y búsqueda de información en este caso de Pokemons
# Desarrollado por Ma~Ra

from .PokeData_Class import *
from .PokeTree_Class import *
from .PokeNode_Class import *
from .PokeDataSet_Class import *
from .PokeList_Class import *
from colorama import Fore

####  AÑADIR LOS COLORES AL FINAL!!!!!
def pokemon():
    # Cargar datos de pokemons del archivo CSV
    print()
    pokemons = PokeDataSet("pokemon.csv")
    print(Fore.YELLOW+"> CARGANDO POKEMONS DESDE ARCHIVO CSV"+Fore.WHITE)
    print(Fore.RED+ "  ATENCIÓN: CSV con cabeceras"+Fore.WHITE)
    print(Fore.RED+ "  ATENCIÓN: Se han detectado pokemons con números repetidos"+Fore.WHITE)
    pokemons.loadPokemons()
    print("  Se han cargado [" + str(len(pokemons)) + "]")
    print("")

    # Crear una arbol por NOMBRE de Pokemonn
    print(Fore.YELLOW+"> INDEXANDO POKEMOS POR NOMBRE"+Fore.WHITE)
    pokeTree_nombre = PokeTree()
    for pk in pokemons:
        pokeTree_nombre.insert(pk.nombre, pk)
    print("  El índice se ha creado con éxito")
    print()

    # Crear una arbol por NÚMERO de Pokemonn
    print(Fore.YELLOW+"> INDEXANDO POKEMONS POR NÚMERO"+Fore.WHITE)
    pokeTree_numero = PokeTree()
    for pk in pokemons:
        pokeTree_numero.insert(pk.numero, pk)
    print("  El índice se ha creado con éxito")
    print()

    # Crear una arbol por TIPO de Pokemonn
    print(Fore.YELLOW+"> INDEXANDO POKEMONS POR TIPO"+Fore.WHITE)
    pokeTree_tipo = PokeTree()
    for pk in pokemons:
        pokeTree_tipo.insert(pk.tipo1, pk)
    for pk in pokemons:
        pokeTree_tipo.insert(pk.tipo2, pk)
    print("  El índice se ha creado con éxito")
    print()

    # Buscando Pokemons por NÚMERO
    print(Fore.YELLOW+"> BUSCANDO POKEMONS POR NUMERO (incluye duplicados)"+Fore.WHITE)
    print(Fore.CYAN+"* Clave [6]: "+Fore.WHITE, pokeTree_numero.search(3), "\n")
    print(Fore.CYAN+"* Clave [700]: "+Fore.WHITE, pokeTree_numero.search(6), "\n")
    print(Fore.CYAN+"* Clave [6578]: "+Fore.WHITE, pokeTree_numero.search(6578), "\n")

    # Buscando Pokemons por NOMBRE
    print(Fore.YELLOW+"> BUSCANDO POKEMONS POR NOMBRE"+ Fore.WHITE)
    print(Fore.CYAN+"* Clave [Oddish]: "+Fore.WHITE, pokeTree_nombre.search("Oddish"), "\n")
    print(Fore.CYAN+"* Clave [GengarMega Gengar]: "+Fore.WHITE,
        pokeTree_nombre.search("GengarMega Gengar"), "\n")
    print(Fore.CYAN+"* Clave [OMG]: "+Fore.WHITE, pokeTree_nombre.search("OMG"), "\n")

    # Ver todos los TIPOS DE POKEMONS
    print(Fore.YELLOW+"> VER TODOS LOS TIPOS DE POKEMONS"+Fore.WHITE)
    print( pokeTree_tipo.showKeysInPreorder())
    print()

    # Contar Pokemons por tipo
    print(Fore.YELLOW+"> CONTAR POKEMONS POR TIPO"+Fore.WHITE)
    for tipo in pokeTree_tipo.showKeysInPreorder():
        print(Fore.CYAN+"* Clave ["+ tipo + "]:"+Fore.WHITE, (pokeTree_tipo.search(tipo)).showQuatity())
    print()

    # Mostrar todos los pokemons que hay de un TIPO
    print(Fore.YELLOW+"> VER TODOS LOS POKEMONS DE CIERTO TIPO ORDENADOS POR NOMBRE"+Fore.WHITE)
    print(Fore.CYAN+"* Clave [Ice]: "+Fore.WHITE, (pokeTree_tipo.search("Ice")).sortByName().showName(), "\n")

    # Ver todos los TIPOS DE POKEMONS
    print(Fore.YELLOW+"> VER TODOS LOS TIPOS DE POKEMONS ORDENADOS POR NOMBREEE"+Fore.WHITE)
    print( pokeTree_nombre.showKeysInPreorder())
    print()

#pokemon()