# Desarrollado por mi (M.R.G.), no es de the algorithms

# Objeto de datos para la información de los Pokemons
# Cada objeto de datos contiene la información de un Pokemon que se nos pide

class PokeData():
    def __init__(self, numero, nombre, tipo1, tipo2, total, hp, ataque, defensa,
                 sp_ataque, sp_defensa, velocidad, generacion, legendario) -> None:

        # Nuevos atributos
        self.numero         = numero
        self.nombre         = nombre
        self.tipo1          = tipo1
        self.tipo2          = tipo2
        self.total          = total
        self.hp             = hp
        self.ataque         = ataque
        self.defensa        = defensa
        self.sp_ataque      = sp_ataque
        self.sp_defensa     = sp_defensa
        self.velocidad      = velocidad
        self.generacion     = generacion
        self.legendario     = legendario

    def __str__(self) -> str:
        pd = "<"+str(self.numero) + "-" + self.nombre + ">\n" + \
            "   Tipo1: " + self.tipo1 + \
            " · Tipo2: " + self.tipo2 + "\n" +\
            "   Total: " + str(self.total) + \
            " · HP: " + str(self.hp) + "\n" + \
            "   Ataque: " + str(self.ataque) + \
            " · Defensa: " + str(self.defensa) + "\n" + \
            "   SP Ataque: " + str(self.sp_ataque) + \
            " · SP Defensa: " + str(self.sp_defensa) + "\n" + \
            "   Velocidad: " + str(self.velocidad) + \
            " · Generación: " + self.generacion + "\n"+\
            "   Es legendario? " + self.legendario.__str__()
        return pd
