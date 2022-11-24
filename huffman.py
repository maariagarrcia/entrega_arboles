# Vamos a hacer un programa que codifique y decodifique un mensaje
# Aqui  vamos a ejecutar el algoritmo de Huffman y DESPUES YA
# HAREMOS EL LANZADOR YLODE SIEMPRE
# cREAREMOS UNA LISTA DE NODOS Y EL ARBOL DE HUFFMAN
from HuffmanTree_Class import *


# Crear una lista de nodos
lista_nodos = HuffmanNodeList(
    [HuffmanNode("A", 0.20), HuffmanNode("F", 0.17), HuffmanNode("1", 0.13), HuffmanNode("3", 0.21), HuffmanNode("O", 0.05), HuffmanNode("M", 0.09), HuffmanNode("T", 0.15)])

print("\n" + "> CLAVES Y FRECUENCIAS")
print(lista_nodos)

# Crear una arbol de Huffman
ht = HuffmanTree(lista_nodos)
print("> ARBOL DE HUFFMAN")
print(ht)

print("> CLAVE PARA CODIFICAR")
print(" ", ht.codeKeys)
print()

print("> CODFICANDO (solo se pueden usar las claves del arbol)")
mensaje = "AFAF3331TMT"
print("  Mensaje en claro [" + mensaje + "]")
print("  Mensaje codificado [" + ht.encoding(mensaje)+"]")
print()

print("> DECODIFICANDO")
mensaje = "00111001110101011001101011110"
print("  Mensaje codificado [" + mensaje + "]")
print("  Mensaje en claro ["+ht.decoding(mensaje)+"]")
