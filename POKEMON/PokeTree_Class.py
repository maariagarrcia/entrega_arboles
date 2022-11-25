# Adaptación arbol binario para trabajar con PokeNodes

from SearchBinaryTree_Class import *
from PokeData_Class import *
from PokeNode_Class import *
from PokeList_Class import *


class PokeTree(SearchBinaryTree):
    def insert(self, accessKey, pokeData: PokeData) -> bool:
        # Validar que hemos recibido un PokeData
        if not isinstance(pokeData, PokeData):
            raise ValueError('Esperaba un PokeData (data)')
        pass

        if (accessKey==None):
            return False

        if isinstance(accessKey, str):
            if accessKey=="":
                return False

        pokeNode = PokeNode(accessKey, pokeData)
        return super().insert(pokeNode)

    def search(self, accessKey) -> PokeList:
        # Devolvemos un PokeData en lugar de un nodo
        node = super().search(accessKey)
        if node==None:
            return PokeList([]) # =======================>

        return PokeList(node.data)
