from colorama import Style, Fore, Back
import numpy
import os
import msvcrt
import random

###################################
#Crear arreglo
libros = numpy.empty([10,4], object)

###################################
#Funciones de diseño
def printv(texto : str):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def printr(texto : str):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Style.RESET_ALL}{Fore.RESET}")

def limpiarpantalla():
    printv("<<Presione una tecla para continuar>>")
    msvcrt.getch()
    os.system("cls")

###################################
#Funciones de arreglo

#validarcodigo

#guardar

#buscar

#certificadoCriticas

#certificadoDetalle

###################################