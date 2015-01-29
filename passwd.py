#!/user/bin/python
# -*- coding: utf-8 -*-

fd=open("/etc/passwd", "r")
lineas = fd.readlines();
diccionario={}

for linea in lineas :
    diccionario[linea.split(":")[0]] = linea.split(":")[len(linea.split(":"))-1]

print("El usuario root usa: " + diccionario["root"][:-1])

try:
    print("El usuario imaginario usa: " + diccionario["imaginario"])
except KeyError:
    print("El usuario imaginario no existe en el diccionario")
