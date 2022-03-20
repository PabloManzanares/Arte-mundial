import pandas as pd

def sacar_rango(x, y):
    '''
    Esta función va a obtener el rango de datos entre dos numpy int64, la fecha de nacimiento y de muerte del artista. 
    De esta forma, transformará los numpy en int y nos devolverá un rango con los años de vida del artista:

        x (numpy.int64): fecha nacimiento del artista.
        y (numpy.int64): fecha fallecimiento del artista.

    return:
        range: rango de dos int con los años de vida del artista.
    '''
    return range(int(x), int(y))


def sacar_rev(x, y, rev):
    '''
    Esta función nos permitirá determinar si el artista ha vivido alguna revolución determinando si la fecha en la que se
    produjo se encuentra dentro del rango de vida del mismo, es decir, si en los años de vida del artista vivió alguna
    revolución. 
    De esta forma, si el año de la revolución está en el rango de vida del artista nos añadirá el nombre de la
    misma en una nueva columna del dataframe que contiene la información del artista y, en caso de que no se encuentre en 
    el rango, no añadirá nada:

        x (numpy.int64): fecha nacimiento del artista.
        y (numpy.int64): fecha fallecimiento del artista.
        rev(diccionario): revoluciones y fechas en las que se produjeron. 

    return:
        string: revolución vivida por el artista.
    '''
    for key, values in rev.items():
        if values in sacar_rango(x, y):
            return key

        else:
            continue