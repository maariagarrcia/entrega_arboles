# Vamos a hacer un programa que codifique y decodifique un mensaje
# Aqui  vamos a ejecutar el algoritmo de Huffman y DESPUES YA
# HAREMOS EL LANZADOR YLODE SIEMPRE
# cREAREMOS UNA LISTA DE NODOS Y EL ARBOL DE HUFFMAN
from .HuffmanTree_Class import *
from colorama import Fore

def huffmann():
    # Crear una lista de nodos
    lista_nodos = HuffmanNodeList(
        [HuffmanNode("A", 0.20), HuffmanNode("F", 0.17), HuffmanNode("1", 0.13), HuffmanNode("3", 0.21), HuffmanNode("O", 0.05), HuffmanNode("M", 0.09), HuffmanNode("T", 0.15)])

    print("\n" +Fore.YELLOW+ "> CLAVES Y FRECUENCIAS"+ Fore.WHITE)
    print(lista_nodos)

    # Crear una arbol de Huffman
    ht = HuffmanTree(lista_nodos)
    print(Fore.YELLOW+"> ARBOL DE HUFFMAN"+ Fore.WHITE)
    print(ht)

    print(Fore.YELLOW+"> CLAVE PARA CODIFICAR"+ Fore.WHITE)
    print(" ", ht.codeKeys)
    print()

    print(Fore.YELLOW+"> CODIFICANDO "+Fore.RED+"(solo se pueden usar las claves del arbol)"+ Fore.WHITE)
    mensaje = "AFAF3331TMT"
    print(Fore.YELLOW+"  Mensaje en claro" + Fore.WHITE + "[" + mensaje + "]")
    print(Fore.YELLOW+"  Mensaje codificado "+ Fore.WHITE + "[" + ht.encoding(mensaje)+"]")
    print()

    print(Fore.YELLOW+"> DECODIFICANDO")
    mensaje = "00111001110101011001101011110"
    print(Fore.YELLOW+"  Mensaje codificado "+ Fore.WHITE + "["+ mensaje + "]")
    print(Fore.YELLOW+"  Mensaje en claro "+ Fore.WHITE + "["+ ht.decoding(mensaje)+"]")

