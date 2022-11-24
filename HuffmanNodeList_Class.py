# Creamos una clase lista de nodos.
# Tiene algunos métodos para simplificar el tratamiento que necesitamos.
# Vamos a usar esta clase para crear una lista de nodos de Huffman.

# CREAMOS LO NECESARIO y lo qye vamos a usar simplemente
class HuffmanNodeList(list):
    def __init__(self, list) -> None:
        super().__init__(list)
        self.sort()

    # Muestra la lista de nodos
    def __str__(self) -> str:
        str_to_show = ""
        for idx, node in enumerate(self):
            str_to_show += str(idx) + "  " + node.val + "\n"

        return str_to_show

    # Permite ordenar el alfabeto de forma ascendente según frecuencia
    def sort(self):
        super().sort(key=lambda nodo: nodo.weight)


    # Al añadir un elemento a la lista la mantiene ordenada
    def append(self, node):
        super().append(node)
        self.sort()

    # Clona la lista
    def copy(self):
        return(HuffmanNodeList(self))

