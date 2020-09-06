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
import config
from DISClib.ADT import list as lt
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
assert config

"""
En este archivo definimos los TADs que vamos a usar,
es decir contiene los modelos con los datos en memoria

"""

# -----------------------------------------------------
# API del TAD Catalogo de Libros
# -----------------------------------------------------

def newCatalog():
    catalog={'Movies':None,}
    catalog['Movies'] = lt.newList('ARRAY_LIST', compareMovieIds)
    return catalog



# Funciones para agregar informacion al catalogo

def addMovie (catalog,movie):
    lt.addLast(catalog['Movies'],movie)


# ==============================
# Funciones de consulta
# ==============================

def sizeMovies():
    return lt.size(catalog['Movies'])

def getTitulo(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    titulo=pelicula['original_title']
    return titulo

def getFecha(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    fecha=pelicula['release_date']
    return fecha
    
def getPromedio(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    promedio=pelicula['vote_average']
    return promedio

def getVotos(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    votos=pelicula['vote_count']
    return votos

def getIdioma(catalog,pos):
    pelicula=lt.getElement(catalog['Movies'],pos)
    idioma=pelicula['original_language']
    return idioma

def getFirstandLastElementsNTFPVI(catalog,titulo,fecha,promedio,votos,idioma,tamaño):
    Lf=lt.newList('ARRAY_LIST',compareMovieIds)
    pelicula=lt.getElement(catalog['Movie'],pos)
    if pos==1:
        lt.addLast(Lf,"Número de películas cargadas:"+tamaño)
    else:
        lt.addLast(Lf,"Última película")
    lt.addLast(LF,"Título:"+titulo)
    lt.addLast(LF,"Fecha de estreno:"+fecha)
    lt.addLast(LF,"Promedio de la votación:"+promedio)
    lt.addLast(LF,"Número de votos:"+votos)
    lt.addLast(LF,"Idioma original:"+idioma)
    return LF

# ==============================
# Funciones de Comparacion
# ==============================

def compareMovieIds(id1,id2):
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1

