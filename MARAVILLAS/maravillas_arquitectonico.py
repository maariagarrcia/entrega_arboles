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







