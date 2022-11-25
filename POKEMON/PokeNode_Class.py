# Crear un tipo de nodo cuyos datos son datos de  tipo PokeData

from .PokeData_Class import *
from .SearchBinaryTree_Class import *


class PokeNode(Node):
    def __init__(self, accessKey, data: PokeData, left=None, right=None):
        if not isinstance(data, PokeData):
            raise ValueError('Esperaba un PokeData (data)')

        super().__init__(accessKey, data, left, right)

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setData(self, data):
        # Atención data puede se de cualquier tipo incluso
        # puede ser un objeto de la clase "PokeData"... ;-)
        self.data = data
