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
             'Producers':None}
    catalog['Movies'] = lt.newList('ARRAY_LIST', compareMovieIds)
    catalog['Producers']=mp.newMap(1,maptype='PROBING',loadfactor=0.5,comparefunction=CompareProducersByName)
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

def addMovie (catalog,movie):
    lt.addLast(catalog['Movies'],movie)
    

def addProducer (catalog, producer):
    tamaño=sizeMovies(catalog)
    acum=0
    titulo=[]
    tupla=()
    for i in range(1,tamaño+1):
        pelicula=lt.getElement(catalog['Movies'],i)
        if pelicula['production_companies'].lower()==producer.lower():
            productora=pelicula['production_companies']
            titulo.append(getTitulo(catalog,i))
            acum=acum+float(getPromedio(catalog,i))
    tamaño_peliculas=len(titulo)
    promedio=acum/tamaño_peliculas
    nuevos_productores=newProducer(titulo,tamaño_peliculas,promedio)
    mp.put(catalog['Producers'],productora,nuevos_productores)
    return mp.get(catalog['Producers'],productora)
    


# ==============================
# Funciones de consulta
# ==============================

def sizeMovies(catalog):
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

def getFirstandLastElementsNTFPVI(catalog,titulo,fecha,promedio,votos,idioma,tamaño,pos):
    Lf=lt.newList('ARRAY_LIST',compareMovieIds)
    pelicula=lt.getElement(catalog['Movies'],pos)
    if pos==1:
        lt.addLast(Lf,"Primera película")
        lt.addLast(Lf,"Número de películas cargadas:"+str(tamaño))
    else:
        lt.addLast(Lf,"Última película")
        lt.addLast(Lf,"Número de películas cargadas:"+str(tamaño))
    lt.addLast(Lf,"Título:"+titulo)
    lt.addLast(Lf,"Fecha de estreno:"+fecha)
    lt.addLast(Lf,"Promedio de la votación:"+promedio)
    lt.addLast(Lf,"Número de votos:"+votos)
    lt.addLast(Lf,"Idioma original:"+idioma)
    return Lf['elements']

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

def CompareProducersByName(name, Producers):
    producerentry = me.getKey(Producers)
    if (name == producerentry):
        return 0
    elif (name > producerentry):
        return 1
    else:
        return -1
