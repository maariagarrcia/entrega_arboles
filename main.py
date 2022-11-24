from HUFFMAN import huffmann

from colorama import Fore
from menu import *
from helpers import *

def mostrar_resultado(descripcion, resultado):
    print(Fore.WHITE + "> " + descripcion + Fore.YELLOW,resultado, Fore.WHITE)

def Huffman():
    mostrar_resultado("Ejercicio1 ",huffmann())


def inicio_programa():
    helpers.clear()  # Limpia la terminal
    menu = Menu("EJERCICIOS ARBOLES / GRAFOS")
    menu.addOption("Ejercicio1", Huffman)
    menu.start()

inicio_programa()