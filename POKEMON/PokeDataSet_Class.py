# Trata el CSV y permite cargar una lista con los Pokemons

import csv
from .PokeData_Class import *


class PokeDataSet(list):
    def __init__(self, fileName: str) -> None:
        super().__init__()

        self.fileName = fileName

    def loadPokemons(self):
        with open(self.fileName, 'r', encoding='utf-8') as fileHandler:
            # Asumimos que es un CSV con encabezamientos de columnas
            csvReader = csv.DictReader(fileHandler, delimiter=',')

            for row in csvReader:
                pd = PokeData(
                    int(row["#"]),
                    row["Name"],
                    row["Type 1"],
                    row["Type 2"],
                    int(row["Total"]),
                    int(row["HP"]),
                    int(row["Attack"]),
                    int(row["Defense"]),
                    int(row["Sp. Atk"]),
                    int(row["Sp. Def"]),
                    int(row["Speed"]),
                    row["Generation"],
                    row["Legendary"])

                self.append(pd)