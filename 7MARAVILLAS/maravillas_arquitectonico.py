# crear clase Grafo
# lo que queremos es crear una clase grafo con 7 maravillas
# y que cada maravilla tenga una lista de conexiones
# y que cada conexion tenga un peso
# En esta clase estaran los metodos para añadir maravillas, añadir conexiones, mostrar maravillas, mostrar conexiones
# y todos los atrtibutos que necesitemos
# Claramente desarrollaremos un algoritmo para que se nos muestre el grafo

# crearemos una clase maravilla que tendrá nombre y país

# 
class Grafo:
    def __init__(self) -> None:
        self.maravillas = []
        self.conexiones = []

    def add_maravilla(self, maravilla):
        self.maravillas.append(maravilla)

    def add_conexion(self, maravilla1, maravilla2):
        self.conexiones.append((maravilla1, maravilla2))

   # printear las maravillas
    def print_maravillas(self):
        for maravilla in self.maravillas:
            print(maravilla)

    # uso grafo no dirigido
    def print_conexiones(self):
        for conexion in self.conexiones:
            print(conexion[0],"-->", conexion[1])
            print()
    
    # metodo para mostrar el grafo
    def mostrar_grafo(self):
        for maravilla in self.maravillas:
            print(maravilla)
            for conexion in self.conexiones:
                if conexion[0] == maravilla:
                    print("  ", conexion[1])
                if conexion[1] == maravilla:
                    print("  ", conexion[0])



        


    def __repr__(self) -> str:
        return f"Grafo({self.maravillas}, {self.conexiones})"

    
 

  

# crear clase Maravilla
class Maravilla:
    def __init__(self, nombre, pais) -> None:
        self.nombre = nombre
        self.pais = pais

    def __str__(self) -> str:
        return self.nombre + " (" + self.pais + ")"







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
    print("Las 7 maravillas del mundo son:")
    grafo.print_maravillas()


    # mostrar conexiones
    print("Las conexiones entre las maravillas son:")
    grafo.print_conexiones()

    # mostrar grafo
    print("El grafo es:")
    grafo.mostrar_grafo()


# ejecutar programa
explicacion_7_maravillas()
