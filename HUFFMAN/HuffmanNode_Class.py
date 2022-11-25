# La libreria binarytree la uso para representar por consola los arboles binarios
from binarytree import Node

# Extiendo la clase Node para agregar peso, propiedad necesaria
# en los árboles de Huffman

# También agrego el método calcMyWeight() para establecer
# automáticamente eeel peso en un nuevo nodo o para recalcular
# el peso si es necesario...

class HuffmanNode(Node):
    def __init__(self, value, weight=0.000, left=None, right=None) -> None:
        # Llamo al constructor Node (que es su superclase)
        super().__init__(value, left, right)

        # Nuevos atributos
        self.weight = float(weight)
        self.label = str(value)

        # Recalculamos el valor el nodo para que incluya el peso
        # y sea de tipo string
        self.val = self.calcVal()

        self.calcWeight()

    def calcWeight(self):
        if self.left != None:
            self.weight = self.left.weight

        if self.right != None:
            self.weight += self.right.weight

        self.val = self.calcVal()

    def calcVal(self) -> str:
        return f'{self.label}·{self.weight:.2f}'
        # return f'{self.label}->{self.weight:.2f}'

        # Es demasiado largo para la consola por eso parecia que en el arbol habia algun error y derecha e izquierda
        # parecia que estaban intercambiadas. :(
            
        # return str(self.label) + "->" + str(self.weight)

    def setLeft(self, node):
        self.left = node
        self.calcWeight()

    def setRight(self, node):
        self.right = node
        self.calcWeight()