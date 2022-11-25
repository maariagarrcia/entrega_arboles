from .maravillas_arquitectonico import *
from colorama import Fore
def explicacion_7_maravillas():
    print("7 MARAVILLAS DEL MUNDO ARQUITECTOÓONICAS")

    # crear  un grafo de 7 maravillas
    grafo = Grafo()
    
    # crear 7 maravillas
    maravilla1 = Maravilla("Chichen Itza", "México")
    maravilla2 = Maravilla("Petra", "Jordania")
    maravilla3 = Maravilla("Coloso de Rodas", "Grecia")
    maravilla4 = Maravilla("Mausoleo de Halicarnaso", "Turquía")
    maravilla5 = Maravilla("Templo de Artemisa", "Turquía")
    maravilla6 = Maravilla("Estátua de Zeus", "Grecia")
    maravilla7 = Maravilla("Jardines colgantes de Babilonia", "Irak")

    # añadir maravillas al grafo
    grafo.add_maravilla(maravilla1)
    grafo.add_maravilla(maravilla2)
    grafo.add_maravilla(maravilla3)
    grafo.add_maravilla(maravilla4)
    grafo.add_maravilla(maravilla5)
    grafo.add_maravilla(maravilla6)
    grafo.add_maravilla(maravilla7)

    # crear conexiones entre maravillas
    grafo.add_conexion(maravilla1, maravilla2)
    grafo.add_conexion(maravilla1, maravilla3)
    grafo.add_conexion(maravilla1, maravilla4)
    grafo.add_conexion(maravilla1, maravilla5)
    grafo.add_conexion(maravilla1, maravilla6)
    grafo.add_conexion(maravilla1, maravilla7)
    grafo.add_conexion(maravilla2, maravilla3)
    grafo.add_conexion(maravilla2, maravilla4)
    grafo.add_conexion(maravilla2, maravilla5)
    grafo.add_conexion(maravilla2, maravilla6)
    grafo.add_conexion(maravilla2, maravilla7)
    grafo.add_conexion(maravilla3, maravilla4)
    grafo.add_conexion(maravilla3, maravilla5)
    grafo.add_conexion(maravilla3, maravilla6)
    grafo.add_conexion(maravilla3, maravilla7)
    grafo.add_conexion(maravilla4, maravilla5)
    grafo.add_conexion(maravilla4, maravilla6)
    grafo.add_conexion(maravilla4, maravilla7)
    grafo.add_conexion(maravilla5, maravilla6)
    grafo.add_conexion(maravilla5, maravilla7)
    grafo.add_conexion(maravilla6, maravilla7)

 
    # mostrar maravillas
    print(Fore.YELLOW+"Las 7 maravillas del mundo son: "+Fore.WHITE)
    grafo.print_maravillas()

    print()

    # mostrar conexiones
    print(Fore.YELLOW+"Las conexiones entre las maravillas son: "+Fore.WHITE)
    grafo.print_conexiones()

 
    print()
    #maravillas_pais
    print(Fore.YELLOW+"Paises que tienen mas de una maravilla son: "+Fore.WHITE)
    grafo.maravillas_pais()

# ejecutar programa
#explicacion_7_maravillas()
