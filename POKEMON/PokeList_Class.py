# Creamos una clase lista de nodos de Huffman (con peso)
# Tiene algunos métodos para simplificar el tratamiento que necesitamos.

class PokeList(list):
    def __init__(self, list) -> None:
        super().__init__(list)

    def __str__(self) -> str:
        str_to_show = "Pokemons [" + str(len(self)) + "]"
        for idx, pokeData in enumerate(self):
            str_to_show += "\n" + pokeData.__str__()

        if str_to_show == "":
            str_to_show = "Ningún Pokemon ..."

        return str_to_show

    def showQuatity(self) -> str:
        str_to_show = "Pokemons [" + str(len(self)) + "]"
        return str_to_show

    def showName(self) -> str:
        str_to_show = "Pokemons [" + str(len(self)) + "]\n"
        for idx, pokeData in enumerate(self):
            str_to_show += pokeData.nombre + ", "

        if str_to_show == "":
            str_to_show = "Ningún Pokemon ..."

        return str_to_show

    def sortByName(self):
        super().sort(key=lambda pokeData: pokeData.nombre)

        return self