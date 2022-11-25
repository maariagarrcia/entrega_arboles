from .maravillas_arquitectonico import *
from colorama import Fore
def explicacion_7_maravillas():
    print("7 MARAVILLAS DEL MUNDO ARQUITECTOÓONICAS")
    print()

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

    print(Fore.YELLOW+ "** COMO LO HARIA **"+Fore.WHITE)
    print(" Lo primero de todo es crear las clases necesarias,  en principio crearia la clase Grafo y maravillas aunque no es necesario  crear la clase maravilla, pero yo la creo para tener un mejor control de los datos.")
    print()
    print(" Lo que queremos es crear una clase grafo con 7 maravillasy que cada maravilla tenga una lista de conexiones y que cada conexion tenga un peso.")
    print()
    print(" En la clase Grafo estaran los metodos para añadir maravillas, añadir conexiones, mostrar maravillas, mostrar conexiones y todos los atrtibutos que necesitemos para los demass apartados.")
    print()
    print(" Claramente desarrollaremos un algoritmo para que se nos muestre el grafo y se printee con sus conexiones")
    print()
    print(" Crearemos una clase maravilla que tendrá nombre y país")
 
    # mostrar maravillas
    print(Fore.YELLOW+"Las 7 maravillas del mundo son: "+Fore.WHITE)
    grafo.print_maravillas()

    print()

    # mostrar conexiones
    print(Fore.YELLOW+"Las conexiones entre las maravillas son: "+Fore.WHITE)
    grafo.print_conexiones()

 
    print()
    
 

# ejecutar programa
#explicacion_7_maravillas()
