# Projeto-PabloManzanares

![portada](https://upload.wikimedia.org/wikipedia/commons/thumb/9/99/Las_Meninas_01.jpg/245px-Las_Meninas_01.jpg)



# Objetivo.

🎨 El objetivo del trabajo es el análisis de un csv con información de alguno de los mejores pintores de la historia. De este modo, se pretende estudiar distintos puntos:

1️⃣ Obtención de los lugares de nacimiento de los distintos artistas a través de la información de Wikipedia, realizando un web scraping de cada uno de los links de Wikipedia según el artista y un posterior folium para la obtención de un mapa.

2️⃣ Comprobar si los artistas han vivido alguna revolución relevante, con el objetivo de comprobar si los movimientos sociales influyen en el crecimiento cultural y en el nacimiento de artistas de renombre.

3️⃣ Un análisis de las obras, observando de manera gráfica cual es la media de obras por artista y a qué géneros pertenecen mayoritariamente.

❕ Todo ello, mediante un csv que contiene el nombre del artista, sus años de vida, el movimiento artístico al que perteneció, la nacionalidad, una pequeña descripción, el enlace de su Wikipedia y el número de obras que pintó. De este modo, es necesario un primer paso de limpieza del mismo.



# Obtención resultados.

**Regex:** permite la limpieza del csv, eliminando los datos innecesarios y obteniendo a partir de otros algunos más específicos de interés como, por ejemplo, la fecha de nacimiento y de fallecimiento.

**Web scraping:** este método fue empleado para la obtención de las ciudades y países de nacimiento de cada uno de los artistas, así como las revoluciones más importantes y sus fechas.

🏡🌍 Ciudades y países. Una vez obtenidos estos datos, mediante el empleo de geopy se logró la localización de la ciudad, es decir, su latitud y longitud. Posteriormente, folium nos permite localizar estas ciudades en el mapa observando los lugares de nacimiento de cada uno de los artistas. 

📅 Revoluciones y fechas. En este caso, se analizó las revoluciones vividas por cada uno de los artistas, comprobando si a lo largo de su vida vivieron alguna. Para ello, se realizó un rango con el año de nacimiento y muerte y, posteriormente, se añadió al dataframe con la información del artista la revolución que coincidiese en estos años de vida. Así, podemos comprobar la revolción vivida por cada uno de los artistas. 

**Gráficas:** fueron empleadas para realizar un análisis de las obras de los distintos artistas, comprobando proncipalmente dos situaciones:

1️⃣ Mayoritariamente cuantas obras pintaron los autores, es decir, cual es, por lo general, el número de obras pintadas por los autores. 

2️⃣ Género con mayor número de obras pintadas.



# Estructura del proyecto.

1️⃣ **notebook:** contiene los jupyter de trabajo.

*Análisis obras autores:* gráficas descriptivas de las obras.

*Exploración datos csv:* exploración y limpieza del csv.

*Fechas revoluciones:* obtención dataframe revoluciones más destacadas y sus respectivas fechas.
    
*Localización ciudades nacimiento autores:* dataframe con la geolocalización de la ciudad natal de cada autor y situación en el mapa mundial. 

*Revoluciones vividas por los autores:* dataframe con la revolución vivida por cada autor.

2️⃣ **src:** funciones y diccionarios empleados.

*diccionarios.py:* diccionario con las revoluciones y fechas de las mismas.

*funcionesciudades.py:* funciones empleadas para la obtención de la latitud y longitud de cada ciudad.

*funcionesrevoluciones.py:* funciones usadas para lograr determinar qué revolución vivió cada autor.

3️⃣ **images:** imágenes de las gráficas obtenidas.

4️⃣ **data:** distintos csv empleados en el proyecto.

*art:* csv original sin limpiar.

*artist:* csv original limpio con la fecha de muerte y fallecimiento añadidas.

*artistas_revoluciones:* csv con información de la revolución vivida por cada autor.

*fechas_revoluciones:* csv con las revoluciones y sus respectivas fechas.


# Librerías.

[pandas] (https://pandas.pydata.org/)

[numpy] (https://numpy.org/)

[regex] (https://docs.python.org/3/library/re.html)

[request] (https://docs.python-requests.org/en/latest/)

[bs4] (https://pypi.org/project/beautifulsoup4/)

[sys] (https://docs.python.org/3/library/sys.html)

[folium] (https://python-visualization.github.io/folium/)

[geopy] (https://geopy.readthedocs.io/en/stable/)

[matplotlib] (https://matplotlib.org/)

[seaborn] (https://seaborn.pydata.org/)
