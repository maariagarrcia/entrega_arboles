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







