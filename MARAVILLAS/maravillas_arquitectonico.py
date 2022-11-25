##### COMO LO HARIA ?????
# Lo primero de todo es crear las clases necesarias,  en principio crearia la clase Grafo y maravillas aunques no es necesario 
# crear la clase maravilla, pero yo la creo para tener un mejor control de los datos.

# Lo que queremos es crear una clase grafo con 7 maravillasy que cada maravilla tenga una lista de conexiones
# y que cada conexion tenga un peso.

# En la clase Grafo estaran los metodos para añadir maravillas, añadir conexiones, mostrar maravillas, mostrar conexiones
# y todos los atrtibutos que necesitemospara los demass apartados.
# Claramente desarrollaremos un algoritmo para que se nos muestre el grafo y se printee con sus conexiones

# Crearemos una clase maravilla que tendrá nombre y país


class Grafo:
    def __init__(self) -> None:
        self.maravillas = []
        self.conexiones = []

    def add_maravilla(self, maravilla):
        self.maravillas.append(maravilla)

    def add_conexion(self, maravilla1, maravilla2):
        self.conexiones.append((maravilla1, maravilla2))

    def print_maravillas(self):
        for maravilla in self.maravillas:
            print(maravilla)

    def print_conexiones(self):
        for conexion in self.conexiones:
            print(conexion[0],"-->", conexion[1])
    

    # determinar si algún país tiene más de una maravilla del mismo tipo;
    # si es así, mostrar el nombre de la maravilla y el país

    #def maravillas_pais(self):
    #    for maravilla in self.maravillas:
    #        for conexion in self.conexiones:
    #            if conexion[0] == maravilla:
    #                print("  ", conexion[1])
#
    #            elif conexion[1] == maravilla:
    #                print("  ", conexion[0])
#
    #    


    def __repr__(self) -> str:
        return f"Grafo({self.maravillas}, {self.conexiones})"

    

  

# crear clase Maravilla
class Maravilla:
    def __init__(self, nombre, pais) -> None:
        self.nombre = nombre
        self.pais = pais

    def __str__(self) -> str:
        return self.nombre + " (" + self.pais + ")"







