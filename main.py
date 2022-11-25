from HUFFMAN import huffmann
from POKEMON import pokemon
from MARAVILLAS import explicacion_7_maravillas

from colorama import Fore
from menu import *
from helpers import *

def mostrar_resultado(descripcion, resultado):
    print(Fore.WHITE + "> " + descripcion + Fore.YELLOW,resultado, Fore.WHITE)

def Huffman():
    mostrar_resultado("ejercicio 1",huffmann())

def Pokemon():
    mostrar_resultado("ejercicio 2",pokemon())

def Maravillas():
    mostrar_resultado("ejercicio 3", explicacion_7_maravillas())

def inicio_programa():
    helpers.clear()  # Limpia la terminal
    menu = Menu("EJERCICIOS ARBOLES / GRAFOS")
    menu.addOption("CODIFICACION DE HUFFMANN", Huffman)
    menu.addOption("POKEMON", Pokemon)
    menu.addOption("MARAVILLAS DEL MUNDO", Maravillas)

    menu.start()

inicio_programa() 