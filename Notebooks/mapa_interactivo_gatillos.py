#!/usr/bin/env python
# coding: utf-8

# Visualización de los valores climáticos gatillo por provincia en España para ultimos años

# In[ ]:


import pandas as pd
import geopandas as gpd
import folium
from IPython.display import display

# **1. Cargar los DataFrames necesarios**

# Cargar los valores gatillo desde un archivo CSV.
# Asegúrate de que el archivo 'nuevos_valores_gatillo.csv' esté en la misma carpeta que este script o cuaderno.
df_gatillo = pd.read_csv("nuevos_valores_gatillo.csv")

# Cargar el shapefile de las provincias de España.
# Asegúrate de que los archivos del shapefile estén en la misma carpeta o en una subcarpeta adecuada.
gdf_provincias = gpd.read_file("georef-spain-provincia-millesime.shp")

# **2. Preparar y unir los DataFrames**

# Renombrar la columna de provincia en 'gdf_provincias' para que coincida con 'df_gatillo'.
gdf_provincias.rename(columns={'prov_name': 'provincia'}, inplace=True)

# Normalizar los nombres de las provincias para evitar discrepancias al unir los DataFrames.
df_gatillo['provincia'] = df_gatillo['provincia'].str.upper().str.strip()
gdf_provincias['provincia'] = gdf_provincias['provincia'].str.upper().str.strip()

# Unir el DataFrame de valores gatillo con el GeoDataFrame de provincias.
gdf_filtrado = gdf_provincias.merge(df_gatillo, on='provincia', how='left')

# **3. Crear y personalizar el mapa**

# Crear un mapa centrado en España.
mapa = folium.Map(location=[40.4165, -3.7026], zoom_start=6)

# Añadir un mapa coroplético que colorea las provincias según la temperatura máxima gatillo.
folium.Choropleth(
    geo_data=gdf_filtrado,
    name='choropleth',
    data=gdf_filtrado,
    columns=['provincia', 'gatillo_temp_max_max'],
    key_on='feature.properties.provincia',
    fill_color='YlOrRd',
    fill_opacity=0.7,
    line_opacity=0.2,
    legend_name='Temperatura Máxima Gatillo (°C)'
).add_to(mapa)

# Añadir las fronteras de las provincias y tooltips personalizados.
folium.GeoJson(
    gdf_filtrado,
    style_function=lambda x: {'fillColor': '#ffffff00', 'color': 'black', 'weight': 1},
    tooltip=folium.GeoJsonTooltip(
        fields=['provincia', 'gatillo_temp_max_max', 'gatillo_humedad_max'],
        aliases=['Provincia', 'Temp. Máx. Gatillo (°C)', 'Humedad Máx. Gatillo (%)'],
        localize=True,
        sticky=False,
        labels=True,
        toLocaleString=True,
        template="""
            <div style="font-size: 14px;">
                <b>{provincia}</b><br>
                Temp. Máx. Gatillo: {gatillo_temp_max_max:.2f}°C<br>
                Humedad Máx. Gatillo: {gatillo_humedad_max:.2f}%<br>
            </div>
        """
    )
).add_to(mapa)

# **4. Mostrar el mapa interactivo**

# Visualizar el mapa generado.
display(mapa)

