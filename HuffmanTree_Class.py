# AQUI SE CREARA LA CLASE DE ARBOL DE HUFFMAN
from HuffmanNode_Class import *
from HuffmanNodeList_Class import *
from binarytree import get_parent


class HuffmanTree():
    def __init__(self, huffmanNodeList):
        # Hay que pasarle una lista con almenos un nodo
        # La lista debe ser de tipo HuffmanNodeList
        # Los nodos debe ser de tipo HuffmanNode
        # Ahora mismo no comprobamos estos prerequisitos...

        self.tree = None
        self.createTree(huffmanNodeList)

        self.codeKeys = {}  # Diccionario para codificar
        self.createCodeKeys()

    # Permite imprimir el arboll
    def __str__(self) -> str:
        return(self.tree.__str__())

    def createTree(self, huffmanNodeList):
        # Hago una copia para no modificar la lista original 
        hnl = huffmanNodeList.copy()

        # Por precaución: Ordeno el alfabeto de menor a mayor frecuencia
        hnl.sort()

        while len(hnl) > 1:
            # Creo un nuevo nodo que apunta a los dos nodos con
            # frecuéncias más bajas en la lista
            new_internal_node = HuffmanNode("~", 0.0, hnl[0], hnl[1])

            # Elimino de la lista los dos nodos con frecuéncias
            # más bajas, es decir, los dos primeros de la lsita.
            # OJO!!! NO elimino los nodos, solo los
            # desasocio de la lista pero siguen existiendo.
            hnl.pop(0)
            hnl.pop(0)
            hnl.append(new_internal_node)

        self.tree = hnl[0]
    # Devuelve una lista con todos los nodos hoja del arbol
    def leaves(self):
        return self.tree.leaves

    # Devuelve el nodo padre de un nodo 
    def getParent(self, node):
        return get_parent(self.tree, node)

    def createCodeKeys(self):
        # Todas las claves o "letras del alfabeto",
        # usados en nuestros mensajes son nodos hoja del arbol

        # Recorrer todas las hojas del arbol calculando su código
        for node in self.leaves():
            child = node
            parent = self.getParent(child)
            codeKey = ""
            while parent != None:
                if parent.left == child:
                    codeKey = "0" + codeKey
                else:
                    codeKey = "1" + codeKey
                child = self.getParent(child)
                parent = self.getParent(child)

            self.codeKeys[node.label] = codeKey

    def showParents(self):
        # Recorrer todas las hojas del arbol
        for node in self.leaves():
            child = node
            print("> Nodo hoja actual", child.val)
            # Recorrer todos los padres del nodo hasta la raiz
            while self.getParent(child) != None:
                # Mostrar los datos de un nodo padre
                print("   ", "Padre", self.getParent(child).val)
                child = self.getParent(child)
            print("    Root")
            
    # Devuelve el mensaje codificado
    def encoding(self, message):
        # Simplemente para cada clave (letra) el mensaje
        # buscamos su valor codificado y lo añadimos al
        # mensaje codificado
        codifiedMessage = ""
        for key in message:
            codifiedMessage += self.codeKeys[key]

        return codifiedMessage

    # Devuelve el mensaje decodificado
    def decoding(self, codifiedMessage):
        message = ""
        parent = self.tree
        child = None
        for binaryDigit in codifiedMessage:
            if binaryDigit == "0":
                child = parent.left
            else:
                child = parent.right

            if (child.left == None) and (child.right == None):
                message += child.label
                parent = self.tree
            else:
                parent = child

        return message
