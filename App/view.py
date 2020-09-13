"""
 * Copyright 2020, Departamento de sistemas y Computación
 * Universidad de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along with this program.  If not, see <http://www.gnu.org/licenses/>.
 """

import sys
import config
from DISClib.ADT import list as lt
from DISClib.DataStructures import listiterator as it
from App import controller
assert config

"""
La vista se encarga de la interacción con el usuario.
Presenta el menu de opciones y por cada seleccion
hace la solicitud al controlador para ejecutar la
operación seleccionada.
"""

# ___________________________________________________
#  Ruta a los archivos
# ___________________________________________________

moviesfile="SmallMoviesDetailsCleaned.csv"


# ___________________________________________________
#  Funciones para imprimir la inforamación de
#  respuesta.  La vista solo interactua con
#  el controlador.
# ___________________________________________________

def printFirstandLast(catalog,titulo,fecha,promedio,votos,idioma,tamaño,pos):
    print(controller.FirstandLastElementsNTFPVI(catalog,titulo,fecha,promedio,votos,idioma,tamaño,pos))


# ___________________________________________________
#  Menu principal
# ___________________________________________________

def printMenu():
    print("Bienvenido")
    print("1 - Inicializar Catalogo")
    print("2 - Cargar informacion en el catalogo")
    print("3 - Imprimir primera y ultima pelicula")
    print("0 - Salir")


while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')

    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        # cont es el controlador que se usará de acá en adelante
        cont = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        controller.loadData(cont, moviesfile)
        print('peliculas cargados: ' + str(controller.movieSize(cont)))

    elif int(inputs[0]) == 3:
        Tamaño = controller.movieSize(cont)
        Titulo1 = controller.Titulo(cont, 1)
        Titulo2 = controller.Titulo(cont, Tamaño)
        Fecha1 = controller.Fecha(cont, 1)
        Fecha2 = controller.Fecha(cont,Tamaño)
        Promedio1 = controller.Promedio(cont, 1)
        Promedio2 = controller.Promedio(cont, Tamaño)
        Votos1 = controller.Votos(cont, 1)
        Votos2 = controller.Votos(cont, Tamaño)
        Idioma1 = controller.Idioma(cont, 1)
        Idioma2 = controller.Idioma(cont, Tamaño)
        printFirstandLast(cont,Titulo1, Fecha1, Promedio1, Votos1, Idioma1,Tamaño,1)
        printFirstandLast(cont,Titulo2, Fecha2, Promedio2, Votos2, Idioma2,Tamaño,Tamaño)   
    else:
        sys.exit(0)
sys.exit(0)