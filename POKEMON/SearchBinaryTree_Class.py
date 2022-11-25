# Implementación básica de un arbol binario de búsqueda, este NO es de the algorithms, usar este que no tiene
# los futures (annotations)

# Clase Nodo
class Node:
    def __init__(self, accessKey, data=[], left=None, right=None):
        self.accessKey = accessKey
        self.left = left
        self.right = right

        if isinstance(data, list):
            self.data = data
        else:
            self.data = []
            self.data.append(data)

    def setLeft(self, node):
        self.left = node

    def setRight(self, node):
        self.right = node

    def setData(self, data):
        # Atención data puede ser de cualquier tipo incluso
        # puede ser un objeto de la clase "PokeData"... ;-)
        self.data = data

# Clase arbol binario de busqueda
class SearchBinaryTree():
    def __init__(self):
        self.tree = None
        self.allowDuplicateAccessKey = True

    def setAllowDuplicateAccesskey(self, allow: bool):
        self.allowDuplicateAccessKey = allow

    def insert(self, node) -> bool:
        # Se permiten claves de acceso repetidas
        if self.tree == None:
            self.tree = node
            return True  # =======================>

        parent = self.tree
        while (parent != None):
            if node.accessKey == parent.accessKey:
                if (self.allowDuplicateAccessKey):
                    # Añadir los datos al nodo existente
                    parent.data = parent.data + node.data
                    return True   # ============>
                else:
                    raise ValueError(
                        '¡En este arbol no se permiten claves duplicadas!')

            if (node.accessKey < parent.accessKey):
                if (parent.left == None):
                    # Hemos llegado al final de la rama izquierda
                    #       => Insertar a la izquierda
                    parent.left = node
                    return True  # ================>
                parent = parent.left
            else:
                if (parent.right == None):
                    # Insertar a la derecha
                    parent.right = node
                    return True  # ================>
                parent = parent.right

        return True

    def search(self, accessKey) -> Node:
        # Partimos de la base de que este arbol es
        # del tipo binario de búsqueda (preorden)
        if accessKey == None:
            raise ValueError(
                'Clave de búsqueda no especificada! (None)')

        parent = self.tree
        while (parent != None):
            if(type(accessKey) != type(parent.accessKey)):
                print(type(accessKey))
                print(type(parent.accessKey))
                raise ValueError(
                    'Tipo incorrecto de la clave de búsqueda!' +
                    '\n  Se esperaba ' + str(type(parent.accessKey)) +
                    '\n  Se ha recibido un ' + str(type(accessKey)))

            if accessKey == parent.accessKey:
                # Lo hemos encontrado
                return parent   # ===============>

            elif (accessKey < parent.accessKey):
                parent = parent.left
            else:
                parent = parent.right

        return None

    def showKeysInPreorder(self, node=None) -> list:
        if node == None:
            node = self.tree

        return self.skp(node)

    def skp(self, node: Node) -> list:
        if node == None:
            return []

        return self.skp(node.left) + [node.accessKey] + self.skp(node.right)

        # Recorrido en preorden a partir de un nodo
        # Devuelve una lista "ordenada" de los nodos
        # Contar nodos de una rama
