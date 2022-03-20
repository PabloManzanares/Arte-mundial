from geopy.geocoders import Nominatim
import numpy as np


def sacar_coord(x):
    '''
    Esta función va a obtener la geolocalización de una ciudad a través de un string. Probará si es posible y, 
    en caso contrario por falta de información, nos devolverá que no existe a traves de un string:

        x (str): ciudad.
    
    return:
        dos int, uno con la latitud y otro con la longitud, si es posible.
        un string indicando que no hay información, en caso contrario.
    '''
    try: 
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(x)
        return location.latitude, location.longitude
    except:
        return 'Sin información'


def sacar_latitud(x):
    '''
    Esta función va a obtener la latitud de una ciudad a través de un dataframe que contiene su latitud y longitud. 
    Probará si es posible y, en caso contrario por falta de información, nos devolverá un np.nan:
    
        x (tuple): longitud y latitud.
    
    return:
        int con la latitud, si es posible.
        np.nan, en caso contrario.

    '''
    try:
        return float(x[0])
    except:
        return np.nan


def sacar_longitud(x):
    '''
    Esta función va a obtener la longitud de una ciudad a través de un dataframe que contiene su latitud y longitud. 
    Probará si es posible y, en caso contrario por falta de información, nos devolverá un np.nan:
    
        x (tuple): longitud y latitud.
    
    return:
        int con la longitud, si es posible.
        np.nan, en caso contrario.
    '''
    try:
        return float(x[1])
    except:
        return np.nan