#!/usr/bin/env python
# coding: utf-8

# # Déjame escuchar la música

# # Contenido <a id='back'></a>
# 
# * [Introducción](#intro)
# * [Etapa 1. Descripción de los datos](#data_review)
#     * [Conclusiones](#data_review_conclusions)
# * [Etapa 2. Preprocesamiento de datos](#data_preprocessing)
#     * [2.1 Estilo del encabezado](#header_style)
#     * [2.2 Valores ausentes](#missing_values)
#     * [2.3 Duplicados](#duplicates)
#     * [2.4 Conclusiones](#data_preprocessing_conclusions)
# * [Etapa 3. Prueba de hipótesis](#hypothesis)
#     * [3.1 Hipótesis 1: actividad de los usuarios y las usuarias en las dos ciudades](#activity)
# * [Conclusiones](#end)

# ## Introducción <a id='intro'></a>
# Como analista de datos, tu trabajo consiste en analizar datos para extraer información valiosa y tomar decisiones basadas en ellos. Esto implica diferentes etapas, como la descripción general de los datos, el preprocesamiento y la prueba de hipótesis.
# 
# Siempre que investigamos, necesitamos formular hipótesis que después podamos probar. A veces aceptamos estas hipótesis; otras veces, las rechazamos. Para tomar las decisiones correctas, una empresa debe ser capaz de entender si está haciendo las suposiciones correctas.
# 
# En este proyecto, compararás las preferencias musicales de las ciudades de Springfield y Shelbyville. Estudiarás datos reales de transmisión de música online para probar la hipótesis a continuación y comparar el comportamiento de los usuarios y las usuarias de estas dos ciudades.
# 
# ### Objetivo:
# Prueba la hipótesis:
# 1. La actividad de los usuarios y las usuarias difiere según el día de la semana y dependiendo de la ciudad.
# 
# 
# ### Etapas
# Los datos del comportamiento del usuario se almacenan en el archivo `/datasets/music_project_en.csv`. No hay ninguna información sobre la calidad de los datos, así que necesitarás examinarlos antes de probar la hipótesis.
# 
# Primero, evaluarás la calidad de los datos y verás si los problemas son significativos. Entonces, durante el preprocesamiento de datos, tomarás en cuenta los problemas más críticos.
# 
# Tu proyecto consistirá en tres etapas:
#  1. Descripción de los datos.
#  2. Preprocesamiento de datos.
#  3. Prueba de hipótesis.
# 
# 
# 
# 
# 
# 
# 

# [Volver a Contenidos](#back)

# ## Etapa 1. Descripción de los datos <a id='data_review'></a>
# 
# Abre los datos y examínalos.

# Necesitarás `pandas`, así que impórtalo.

# In[ ]:


# Importar pandas
import pandas as pd


# Lee el archivo `music_project_en.csv` de la carpeta `/datasets/` y guárdalo en la variable `df`:

# In[ ]:


# Leer el archivo y almacenarlo en df
df=pd.read_csv('/datasets/music_project_en.csv')


# Muestra las 10 primeras filas de la tabla:

# In[ ]:


# Obtener las 10 primeras filas de la tabla df
print(df.head(10))


# Obtén la información general sobre la tabla con un comando. Conoces el método que muestra la información general que necesitamos.

# In[ ]:


# Obtener la información general sobre nuestros datos
df.info


# Estas son nuestras observaciones sobre la tabla. Contiene siete columnas. Almacenan los mismos tipos de datos: `object`.
# 
# Según la documentación:
# - `' userID'`: identificador del usuario o la usuaria;
# - `'Track'`: título de la canción;
# - `'artist'`: nombre del artista;
# - `'genre'`: género de la pista;
# - `'City'`: ciudad del usuario o la usuaria;
# - `'time'`: la hora exacta en la que se reprodujo la canción;
# - `'Day'`: día de la semana.
# 
# Podemos ver tres problemas con el estilo en los encabezados de la tabla:
# 1. Algunos encabezados están en mayúsculas, otros en minúsculas.
# 2. Hay espacios en algunos encabezados.
# 3. `Detecta el tercer problema por tu cuenta y descríbelo aquí`.R/ Existen celdas con valores ausentes "NaN" por lo que puedes llegar a ser necesario replazar esa ausencia de valor para evitar errores durante el analisis de la información
# 
# 
# 

# ### Escribe observaciones de tu parte. Estas son algunas de las preguntas que pueden ser útiles: <a id='data_review_conclusions'></a>
# 
# `1.   ¿Qué tipo de datos tenemos a nuestra disposición en las filas? ¿Y cómo podemos entender lo que almacenan las columnas?`
# 
# `2.   ¿Hay suficientes datos para proporcionar respuestas a nuestra hipótesis o necesitamos más información?`
# 
# `3.   ¿Notaste algún problema en los datos, como valores ausentes, duplicados o tipos de datos incorrectos?`

# [Volver a Contenidos](#back)

# ## Etapa 2. Preprocesamiento de datos <a id='data_preprocessing'></a>
# 
# El objetivo aquí es preparar los datos para que sean analizados.
# El primer paso es resolver cualquier problema con los encabezados. Luego podemos avanzar a los valores ausentes y duplicados. Empecemos.
# 
# Corrige el formato en los encabezados de la tabla.
# 

# ### Estilo del encabezado <a id='header_style'></a>
# Muestra los encabezados de la tabla (los nombres de las columnas):

# In[ ]:


# Muestra los nombres de las columnas
import pandas as pd
df = pd.read_csv('/datasets/music_project_en.csv')
print(df.columns)


# Cambia los encabezados de la tabla de acuerdo con las reglas del buen estilo:
# * Todos los caracteres deben ser minúsculas.
# * Elimina los espacios.
# * Si el nombre tiene varias palabras, utiliza snake_case.

# Anteriormente, aprendiste acerca de la forma automática de cambiar el nombre de las columnas. Vamos a aplicarla ahora. Utiliza el bucle for para iterar sobre los nombres de las columnas y poner todos los caracteres en minúsculas. Cuando hayas terminado, vuelve a mostrar los encabezados de la tabla:

# In[ ]:


# Bucle en los encabezados poniendo todo en minúsculas
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

new_columns = []

for col in df.columns:
    new_columns.append(col.strip().lower())

df.columns = new_columns

print(df.columns)


# Ahora, utilizando el mismo método, elimina los espacios al principio y al final de los nombres de las columnas e imprime los nombres de las columnas nuevamente:

# In[ ]:


# Bucle en los encabezados poniendo todo en minúsculas
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

new_columns = []

for col in df.columns:
    new_columns.append(col.replace(' ', '_'))

df.columns = new_columns

print(df.columns)


# Necesitamos aplicar la regla de snake_case a la columna `userid`. Debe ser `user_id`. Cambia el nombre de esta columna y muestra los nombres de todas las columnas cuando hayas terminado.

# In[ ]:


import pandas as pd

# Cargar el archivo CSV en un DataFrame
df = pd.read_csv('/datasets/music_project_en.csv')

# Crear una lista vacía para almacenar los nuevos nombres de las columnas
new_columns = []

# Iterar sobre los nombres de las columnas y convertirlos a minúsculas
for col in df.columns:
    new_columns.append(col.strip().lower().replace(' ', '_'))  # Limpiar espacios y aplicar snake_case

# Asignar los nuevos nombres al DataFrame
df.columns = new_columns


df = df.rename(columns={'userid': 'user_id'})

print(df.columns)


# Comprueba el resultado. Muestra los encabezados una vez más:

# In[ ]:


# Comprobar el resultado: la lista de encabezados
print(df.columns)


# [Volver a Contenidos](#back)

# ### Valores ausentes <a id='missing_values'></a>
#  Primero, encuentra el número de valores ausentes en la tabla. Debes utilizar dos métodos en una secuencia para obtener el número de valores ausentes.

# In[ ]:


# Calcular el número de valores ausentes
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

missing_values = df.isnull().sum()

print(missing_values)


# No todos los valores ausentes afectan a la investigación. Por ejemplo, los valores ausentes en `track` y `artist` no son cruciales. Simplemente puedes reemplazarlos con valores predeterminados como el string `'unknown'` (desconocido).
# 
# Pero los valores ausentes en `'genre'` pueden afectar la comparación entre las preferencias musicales de Springfield y Shelbyville. En la vida real, sería útil saber las razones por las cuales hay datos ausentes e intentar recuperarlos. Pero no tenemos esa oportunidad en este proyecto. Así que tendrás que:
# * rellenar estos valores ausentes con un valor predeterminado;
# * evaluar cuánto podrían afectar los valores ausentes a tus cómputos;

# Reemplazar los valores ausentes en las columnas `'track'`, `'artist'` y `'genre'` con el string `'unknown'`. Como mostramos anteriormente en las lecciones, la mejor forma de hacerlo es crear una lista que almacene los nombres de las columnas donde se necesita el reemplazo. Luego, utiliza esta lista e itera sobre las columnas donde se necesita el reemplazo haciendo el propio reemplazo.

# In[ ]:


# Bucle en los encabezados reemplazando los valores ausentes con 'unknown'
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

columns_to_replace = ['track', 'artist', 'genre']

for col in columns_to_replace:
    df[col] = df[col].fillna('unknown')

print(df.isnull().sum())


# Ahora comprueba el resultado para asegurarte de que después del reemplazo no haya valores ausentes en el conjunto de datos. Para hacer esto, cuenta los valores ausentes nuevamente.

# In[ ]:


# Contar valores ausentes
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

columns_to_replace = ['track', 'artist', 'genre']

for col in columns_to_replace:
    df[col] = df[col].fillna('unknown')

missing_values_after = df.isnull().sum()

print(missing_values_after)


# [Volver a Contenidos](#back)

# ### Duplicados <a id='duplicates'></a>
# Encuentra el número de duplicados explícitos en la tabla. Una vez más, debes aplicar dos métodos en una secuencia para obtener la cantidad de duplicados explícitos.

# In[ ]:


# Contar duplicados explícitos
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

duplicados = df.duplicated().sum()

print("Número de duplicados explícitos en la tabla:", duplicados)


# Ahora, elimina todos los duplicados. Para ello, llama al método que hace exactamente esto.

# In[ ]:


# Eliminar duplicados explícitos

import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

df = df.drop_duplicates()

duplicate_count_after = df.duplicated().sum()

print("Número de duplicados después de la eliminación:", duplicate_count_after)


# Comprobemos ahora si eliminamos con éxito todos los duplicados. Cuenta los duplicados explícitos una vez más para asegurarte de haberlos eliminado todos:

# In[ ]:


# Comprobar de nuevo si hay duplicados

import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

df = df.drop_duplicates()

duplicate_count_after = df.duplicated().sum()

print("Número de duplicados después de la eliminación:", duplicate_count_after)


# Ahora queremos deshacernos de los duplicados implícitos en la columna `genre`. Por ejemplo, el nombre de un género se puede escribir de varias formas. Dichos errores también pueden afectar al resultado.

# Para hacerlo, primero mostremos una lista de nombres de género únicos, ordenados en orden alfabético. Para ello:
# * Extrae la columna `genre` del DataFrame.
# * Llama al método que devolverá todos los valores únicos en la columna extraída.
# 

# In[ ]:


# Inspeccionar los nombres de géneros únicos
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

unique_genres = sorted(df['genre'].unique())

print(unique_genres)


# Busca en la lista para encontrar duplicados implícitos del género `hiphop`. Estos pueden ser nombres escritos incorrectamente o nombres alternativos para el mismo género.
# 
# Verás los siguientes duplicados implícitos:
# * `hip`
# * `hop`
# * `hip-hop`
# 
# Para deshacerte de ellos, crea una función llamada `replace_wrong_genres()` con dos parámetros:
# * `wrong_genres=`: esta es una lista que contiene todos los valores que necesitas reemplazar.
# * `correct_genre=`: este es un string que vas a utilizar como reemplazo.
# 
# Como resultado, la función debería corregir los nombres en la columna `'genre'` de la tabla `df`, es decir, remplazar cada valor de la lista `wrong_genres` por el valor en `correct_genre`.
# 
# Dentro del cuerpo de la función, utiliza un bucle `'for'` para iterar sobre la lista de géneros incorrectos, extrae la columna `'genre'` y aplica el método `replace` para hacer correcciones.

# In[ ]:


# Función para reemplazar duplicados implícitos
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

def replace_wrong_genres(wrong_genres, correct_genre):
    for genre in wrong_genres:
        df['genre'] = df['genre'].replace(genre, correct_genre)

wrong_genres_list = ['hip', 'hop', 'hip-hop']
correct_genre_name = 'hiphop'

replace_wrong_genres(wrong_genres_list, correct_genre_name)

print(sorted(df['genre'].unique()))


# Ahora, llama a `replace_wrong_genres()` y pásale tales argumentos para que retire los duplicados implícitos (`hip`, `hop` y `hip-hop`) y los reemplace por `hiphop`:

# In[ ]:


# Eliminar duplicados implícitos

wrong_genres_list = ['hip', 'hop', 'hip-hop']
correct_genre_name = 'hiphop'

replace_wrong_genres(wrong_genres_list, correct_genre_name)

print(sorted(df['genre'].unique()))


# Asegúrate de que los nombres duplicados han sido eliminados. Muestra la lista de valores únicos de la columna `'genre'` una vez más:

# In[ ]:


# Comprobación de duplicados implícitos
wrong_genres_list = ['hip', 'hop', 'hip-hop']
correct_genre_name = 'hiphop'

replace_wrong_genres(wrong_genres_list, correct_genre_name)

print(sorted(df['genre'].unique()))


# [Volver a Contenidos](#back)
### Tus observaciones <a id='data_preprocessing_conclusions'></a>

`Describe brevemente lo que has notado al analizar duplicados, cómo abordaste sus eliminaciones y qué resultados obtuviste.`

Existian diversos errores en el campo de 'genre' ya que existian datos que representaban la información pero por no tener la misma sintaxis python nol a reconocia como una misma información.

Asi que toco pasar de 3 nombres de genero que significaban hip hop a solamente un grupo que ahora se llama hiphop.
# [Volver a Contenidos](#back)

# ## Etapa 3. Prueba de hipótesis <a id='hypothesis'></a>

# ### Hipótesis: comparar el comportamiento del usuario o la usuaria en las dos ciudades <a id='activity'></a>

# La hipótesis afirma que existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música. Para comprobar esto, usa los datos de tres días de la semana: lunes, miércoles y viernes.
# 
# * Agrupa a los usuarios y las usuarias por ciudad.
# * Compara el número de canciones que cada grupo reprodujo el lunes, el miércoles y el viernes.
# 

# Realiza cada cálculo por separado.
# 
# El primer paso es evaluar la actividad del usuario en cada ciudad. Recuerda las etapas dividir-aplicar-combinar de las que hablamos anteriormente en la lección. Tu objetivo ahora es agrupar los datos por ciudad, aplicar el método apropiado para contar durante la etapa de aplicación y luego encontrar la cantidad de canciones reproducidas en cada grupo especificando la columna para obtener el recuento.
# 
# A continuación se muestra un ejemplo de cómo debería verse el resultado final:
# `df.groupby(by='....')['column'].method()`Realiza cada cálculo por separado.
# 
# Para evaluar la actividad de los usuarios y las usuarias en cada ciudad, agrupa los datos por ciudad y encuentra la cantidad de canciones reproducidas en cada grupo.
# 
# 

# In[ ]:


# Contar las canciones reproducidas en cada ciudad
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

songs_by_city = df.groupby(by='city')['track'].count()

print(songs_by_city)


# `Comenta tus observaciones aquí`

# Ahora agrupemos los datos por día de la semana y encontremos el número de canciones reproducidas el lunes, miércoles y viernes. Utiliza el mismo método que antes, pero ahora necesitamos una agrupación diferente.
# 

# In[ ]:


# Calcular las canciones reproducidas en cada uno de los tres días
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

songs_by_day = df.groupby(by='day')['track'].count()

songs_selected_days = songs_by_day.loc[['Monday', 'Wednesday', 'Friday']]

print(songs_selected_days)


# `Comenta tus observaciones aquí`

# Ya sabes cómo contar entradas agrupándolas por ciudad o día. Ahora necesitas escribir una función que pueda contar entradas según ambos criterios simultáneamente.
# 
# Crea la función `number_tracks()` para calcular el número de canciones reproducidas en un determinado día **y** ciudad. La función debe aceptar dos parámetros:
# 
# - `day`: un día de la semana para filtrar. Por ejemplo, `'Monday'` (lunes).
# - `city`: una ciudad para filtrar. Por ejemplo, `'Springfield'`.
# 
# Dentro de la función, aplicarás un filtrado consecutivo con indexación lógica.
# 
# Primero filtra los datos por día y luego filtra la tabla resultante por ciudad.
# 
# Después de filtrar los datos por dos criterios, cuenta el número de valores de la columna 'user_id' en la tabla resultante. Este recuento representa el número de entradas que estás buscando. Guarda el resultado en una nueva variable y devuélvelo desde la función.

# In[ ]:


# Declara la función number_tracks() con dos parámetros: day= y city=.
import pandas as pd

df = pd.read_csv('/datasets/music_project_en.csv')

    # Almacena las filas del DataFrame donde el valor en la columna 'day' es igual al parámetro day=
    
def number_tracks(day, city):
    
    df_filtered_day = df[df['day'] == day
                         
    # Filtra las filas donde el valor en la columna 'city' es igual al parámetro city=
                         
    df_filtered_city = df_filtered_day[df_filtered_day['city'] == city]
                         
    # Extrae la columna 'user_id' de la tabla filtrada y aplica el método count()
                         
    track_count = df_filtered_city['user_id'].count()
                         
    # Devolve el número de valores de la columna 'user_id'
                         
    return track_count


# Llama a `number_tracks()` seis veces, cambiando los valores de los parámetros para que recuperes los datos de ambas ciudades para cada uno de los tres días.

# In[ ]:


# El número de canciones reproducidas en Springfield el lunes
tracks_monday_springfield = number_tracks('Monday', 'Springfield')


# In[ ]:


# El número de canciones reproducidas en Shelbyville el lunes
tracks_monday_shelbyville = number_tracks('Monday', 'Shelbyville')


# In[ ]:


# El número de canciones reproducidas en Springfield el miércoles
tracks_wednesday_springfield = number_tracks('Wednesday', 'Springfield')


# In[ ]:


# El número de canciones reproducidas en Shelbyville el miércoles
tracks_wednesday_shelbyville = number_tracks('Wednesday', 'Shelbyville')


# In[ ]:


# El número de canciones reproducidas en Springfield el viernes
tracks_friday_springfield = number_tracks('Friday', 'Springfield')


# In[ ]:


# El número de canciones reproducidas en Shelbyville el viernes
tracks_friday_shelbyville = number_tracks('Friday', 'Shelbyville')


# [Volver a Contenidos](#back)

# # Conclusiones <a id='end'></a>

# `Resume aquí tus conclusiones sobre la hipótesis.` R/ La hipotesis 'existen diferencias en la forma en que los usuarios y las usuarias de Springfield y Shelbyville consumen música' es correcta, ya que la información arroajda durante los lunes, miercoles y viernes es distinta en ambas ciudades (Springfield y Shelbyville)

# ### Nota
# En proyectos de investigación reales, la prueba de hipótesis estadística es más precisa y cuantitativa. También ten en cuenta que no siempre se pueden sacar conclusiones sobre una ciudad entera a partir de datos de una sola fuente.
# 
# Aprenderás más sobre la prueba de hipótesis en el sprint de análisis estadístico de datos.

# [Volver a Contenidos](#back)
