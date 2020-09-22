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
    catalog={'Movies':None,
             'Producers':None,
             'generos':None}
    catalog['Movies'] = lt.newList('ARRAY_LIST', compareMovieIds)
    catalog['Producers']=mp.newMap(1,maptype='CHAINING',loadfactor=2,comparefunction=CompareProducersByName)
    catalog['generos']=mp.newMap(1,maptype='CHAINING',loadfactor=2,comparefunction=CompareProducersByName)
    return catalog

def newProducer(nom_movies,tot_movies,prom_movies): 
    producer={'Peliculas':None,
              'Total películas':None,
              'Promedio':None}
    producer['Peliculas']=nom_movies
    producer['Total películas']=tot_movies
    producer['Promedio']=prom_movies
    return producer


# Funciones para agregar informacion al catalogo

def addGenero (catalog, genero):
    l_peliculas = []
    contador = 0
    valoracion = 0
    tamaño = sizeMovies(catalog)
    for n in range(1,tamaño+1):
        pelicula = lt.getElement(catalog['Movies'], n)
        if genero.lower()==pelicula["genres"].lower() or genero.lower() in pelicula["genres"].lower():
            l_peliculas.append(pelicula["title"])
            contador += 1
            valoracion += float(pelicula["vote_average"])
    promedio = valoracion/contador
    nuevo_genero = newProducer(l_peliculas,contador, promedio)
    mp.put(catalog['generos'], genero, nuevo_genero)
    return mp.get(catalog['generos'], genero)


# ==============================
# Funciones de consulta
# ==============================



# ==============================
# Funciones de Comparacion
# ==============================


