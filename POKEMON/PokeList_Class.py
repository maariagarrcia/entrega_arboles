# Creamos una clase lista de nodos de Huffman (con peso)
# Tiene algunos métodos para simplificar el tratamiento que necesitamos.

class PokeList(list):
    def __init__(self, list) -> None:
        super().__init__(list)

    # Muestra la lista de Pokemons
    def __str__(self) -> str:
        str_to_show = ""
        for idx, node in enumerate(self):
            str_to_show += "\n" + node.__str__() 

        return str_to_show
