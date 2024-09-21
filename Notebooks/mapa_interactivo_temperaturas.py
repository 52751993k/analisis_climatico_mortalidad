#!/usr/bin/env python
# coding: utf-8

# Mapa interactivo que muestra información climática y de mortalidad atribuible por provincia en España. Los usuarios pueden seleccionar el año y mes que desean visualizar utilizando widgets interactivos.

# In[ ]:


import pandas as pd
import geopandas as gpd
import folium
import ipywidgets as widgets
from IPython.display import display


# **1. Cargar los DataFrames necesarios**

# Cargar los datos de resultados ajustados y valores gatillo desde archivos CSV.
# Asegúrate de que estos archivos estén en el mismo directorio que este script o cuaderno.
df_resultados_ajustados = pd.read_csv("resultados_ajustados.csv")
df_valores_gatillo = pd.read_csv("nuevos_valores_gatillo.csv")

# Cargar el archivo shapefile de las provincias españolas.
# Asegúrate de tener todos los archivos asociados al shapefile en el mismo directorio.
gdf_provincias = gpd.read_file("georef-spain-provincia-millesime.shp")

# **2. Preparar y unificar los DataFrames**

# Asegurar que las columnas de provincia tienen el mismo nombre en todos los DataFrames.
# En 'gdf_provincias', renombramos la columna 'prov_name' a 'provincia'.
gdf_provincias.rename(columns={'prov_name': 'provincia'}, inplace=True)

# Normalizar los nombres de las provincias para evitar discrepancias al unir los DataFrames.
df_resultados_ajustados['provincia'] = df_resultados_ajustados['provincia'].str.upper().str.strip()
df_valores_gatillo['provincia'] = df_valores_gatillo['provincia'].str.upper().str.strip()
gdf_provincias['provincia'] = gdf_provincias['provincia'].str.upper().str.strip()

# Unir los resultados ajustados con los valores gatillo en base a la provincia.
df_combined = pd.merge(df_resultados_ajustados, df_valores_gatillo, on='provincia', how='inner')

# Eliminar posibles columnas duplicadas después del merge.
df_combined = df_combined.loc[:, ~df_combined.columns.duplicated()]

# **3. Unir con el GeoDataFrame para preparación del mapa**

# Unir el DataFrame combinado con el GeoDataFrame de las provincias.
gdf_combined = gdf_provincias.merge(df_combined, on='provincia', how='left')

# **4. Preparar los widgets para la interacción**

# Obtener el último año y mes disponibles en los datos para establecer valores por defecto.
ultimo_anio = df_combined['año'].max()
ultimo_mes = df_combined[df_combined['año'] == ultimo_anio]['mes_num'].max()

# Crear widgets de selección para el año y el mes.
anio_widget = widgets.Dropdown(
    options=sorted(df_combined['año'].unique(), reverse=True),
    value=ultimo_anio,
    description='Año:',
    disabled=False,
)

mes_widget = widgets.Dropdown(
    options=sorted(df_combined['mes_num'].unique()),
    value=ultimo_mes,
    description='Mes:',
    disabled=False
)

# **5. Definir la función para actualizar el mapa**

def actualizar_mapa(anio_seleccionado, mes_seleccionado):
    """
    Actualiza el mapa interactivo basado en el año y mes seleccionados por el usuario.
    """
    # Filtrar los datos según el año y mes seleccionados.
    df_filtrado = df_combined[
        (df_combined['año'] == anio_seleccionado) &
        (df_combined['mes_num'] == mes_seleccionado)
    ]

    # Unir los datos filtrados con el GeoDataFrame de las provincias.
    gdf_filtrado = gdf_provincias.merge(df_filtrado, on='provincia', how='left')

    # Crear un mapa centrado en España.
    mapa = folium.Map(location=[40.4165, -3.7026], zoom_start=6)

    # Añadir un mapa coroplético para mostrar la mortalidad atribuible.
    folium.Choropleth(
        geo_data=gdf_filtrado,
        name='choropleth',
        data=gdf_filtrado,
        columns=['provincia', 'mort_atribuible_x'],
        key_on='feature.properties.provincia',
        fill_color='YlOrRd',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='Mortalidad Atribuible (%)'
    ).add_to(mapa)

    # Añadir las fronteras de las provincias y tooltips personalizados.
    folium.GeoJson(
        gdf_filtrado,
        style_function=lambda x: {'fillColor': '#ffffff00', 'color': 'black', 'weight': 1},
        tooltip=folium.GeoJsonTooltip(
            fields=[
                'provincia', 'mortalidad_atribuible', 'temp_min_max', 'temp_max_max', 'humedad_max',
                'dias_consecutivos_tmin_22', 'dias_consecutivos_tmin_25', 'dias_consecutivos_tmin_28',
                'dias_consecutivos_tmax_35', 'dias_consecutivos_tmax_38', 'dias_consecutivos_tmax_41',
                'dias_consecutivos_humedad_70', 'dias_consecutivos_humedad_80', 'dias_consecutivos_humedad_90',
                'mort_atribuible_x', 'dias', 'gatillo_temp_max_max', 'gatillo_humedad_max'
            ],
            aliases=[
                'Provincia', 'Mortalidad %', 'Temp. Mín. Máx.', 'Temp. Máx. Máx.', 'Humedad Máx.',
                'Días T. Mín ≥22°C', 'Días T. Mín ≥25°C', 'Días T. Mín ≥28°C', 'Días T. Máx ≥35°C', 'Días T. Máx ≥38°C',
                'Días T. Máx ≥41°C', 'Días Hum. ≥70%', 'Días Hum. ≥80%', 'Días Hum. ≥90%', 'Muertes Atribuibles',
                'Días Totales', 'Gatillo Temp. Máx. Máx.', 'Gatillo Humedad Máx.'
            ],
            localize=True,
            sticky=False,
            labels=True,
            toLocaleString=True,
            template="""
                <div style="font-size: 14px;">
                    <b>{provincia}</b><br>
                    Mortalidad Atribuible: {mortalidad_atribuible:.2f}%<br>
                    Temp. Mín. Máx.: {temp_min_max:.2f}°C<br>
                    Temp. Máx. Máx.: {temp_max_max:.2f}°C<br>
                    Humedad Máx.: {humedad_max:.2f}%<br>
                    Días T. Mín ≥22°C: {dias_consecutivos_tmin_22}<br>
                    Días T. Mín ≥25°C: {dias_consecutivos_tmin_25}<br>
                    Días T. Mín ≥28°C: {dias_consecutivos_tmin_28}<br>
                    Días T. Máx ≥35°C: {dias_consecutivos_tmax_35}<br>
                    Días T. Máx ≥38°C: {dias_consecutivos_tmax_38}<br>
                    Días T. Máx ≥41°C: {dias_consecutivos_tmax_41}<br>
                    Días Hum. ≥70%: {dias_consecutivos_humedad_70}<br>
                    Días Hum. ≥80%: {dias_consecutivos_humedad_80}<br>
                    Días Hum. ≥90%: {dias_consecutivos_humedad_90}<br>
                    Muertes Atribuibles: {mort_atribuible_x}<br>
                    Días Totales: {dias}<br>
                    Gatillo Temp. Máx. Máx.: {gatillo_temp_max_max:.2f}°C<br>
                    Gatillo Humedad Máx.: {gatillo_humedad_max:.2f}%
                </div>
            """
        )
    ).add_to(mapa)

    # Mostrar el mapa interactivo.
    display(mapa)

# **6. Conectar los widgets con la función para actualizar el mapa**

# Utilizar 'interact' para conectar los widgets y actualizar el mapa según las selecciones del usuario.
widgets.interact(actualizar_mapa, anio_seleccionado=anio_widget, mes_seleccionado=mes_widget)

