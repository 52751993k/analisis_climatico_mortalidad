Análisis del impacto del calor extremo en la mortalidad en España

Este proyecto analiza la relación entre variables climáticas y la mortalidad en las provincias de España, incluyendo la generación de mapas interactivos y cálculos de valores gatillo para variables climáticas.

Estructura del Proyecto
bash
Copiar código
tu_proyecto/
│
├── data/                   # Carpeta para los archivos de datos
│   ├── dataset_modificado.csv
│   ├── resultados_ajustados.csv
│   ├── nuevos_valores_gatillo.csv
│   └── georef-spain-provincia-millesime.shp
│       (y los demás archivos asociados al shapefile)
│
├── scripts/                # Carpeta para los scripts en Jupyter Notebooks
│   ├── calcular_valores_gatillo.ipynb
│   ├── ajustar_valores_gatillo.ipynb
│   ├── verificar_versiones.ipynb
│   └── (otros scripts de procesamiento)
│
├── notebooks/              # Carpeta para los notebooks de Jupyter 
│   ├── mapa_interactivo_gatillos.ipynb
│   ├── mapa_interactivo_temperaturas.ipynb
│   └── (otros notebooks)
│
├── requirements.txt        # Archivo con las dependencias y versiones
│
└── README.md               # Documentación del proyecto
Descripción del Proyecto
Este proyecto tiene como objetivo analizar cómo las variables climáticas, como temperaturas extremas y humedad, afectan la mortalidad en las diferentes provincias de España. Incluye:

Cálculo de valores gatillo para variables climáticas.
Ajuste y validación de valores gatillo.
Generación de mapas interactivos que muestran información climática y de mortalidad.
Visualización de valores gatillo por provincia.

Requisitos Previos
Python 3.9 o superior.
Anaconda o Conda (recomendado para manejar dependencias geoespaciales).

Instalación
Usando Conda (Recomendado)

Clonar el repositorio:
git clone https://github.com/tu_usuario/tu_proyecto.git

Navegar al directorio del proyecto:
cd Análisis del impacto del calor extremo en la mortalidad en España

Crear un entorno virtual:
conda create -n mi_entorno python=3.9

Activar el entorno:
conda activate mi_entorno

Instalar las dependencias principales con Conda:
conda install pandas==2.1.4 numpy==1.26.4 geopandas==1.0.1 folium==0.17.0 ipywidgets==8.1.5 ipython==8.14.0 requests==2.31.0

Instalar las dependencias adicionales con pip:
pip install fiona==1.10.1 shapely==2.0.5 pyproj==3.6.1 rtree==1.0.1 branca==0.7.2

Nota: Algunas librerías geoespaciales requieren dependencias del sistema que Conda maneja automáticamente.


Uso del Proyecto
Procesamiento de Datos

1. Calcular Valores Gatillo
Ejecuta el script calcular_valores_gatillo.py para calcular los valores gatillo de las variables climáticas.

python scripts/calcular_valores_gatillo.py
Entrada: dataset_modificado.csv
Salida: gatillos_provincia_promedio_ultimos_2_anos.


2. Ajustar Valores Gatillo
Ejecuta el script ajustar_valores_gatillo.py para ajustar y validar los valores gatillo calculados.

python scripts/ajustar_valores_gatillo.py
Entrada: gatillos_provincia_promedio_ultimos_2_anos.csv
Salida: nuevos_valores_gatillo.csv


Visualizaciones Interactivas
Los mapas interactivos se encuentran en la carpeta notebooks/ y requieren Jupyter Notebook o JupyterLab.

1. Iniciar Jupyter Notebook
jupyter notebook

2. Abrir los Notebooks de Interés

Mapa Interactivo de Valores Gatillo:
Abre mapa_interactivo_gatillos.ipynb para visualizar los valores gatillo por provincia.


Mapa Interactivo de Temperaturas Extremas:
Abre mapa_interactivo_temperaturas.ipynb para visualizar las temperaturas extremas y la mortalidad atribuible.

Nota: Asegúrate de que los archivos de datos están en la carpeta data/ y que las rutas relativas en los notebooks son correctas.

Verificación de Versiones de Librerías
Para asegurarte de que tienes instaladas las versiones correctas de las librerías, ejecuta el siguiente script:

python scripts/verificar_versiones.py
Este script mostrará las versiones de las librerías utilizadas en el proyecto. Deberías comparar estas versiones con las especificadas en requirements.txt para confirmar que coinciden.


Estructura de Carpetas y Archivos

data/: Contiene los datasets y archivos geoespaciales necesarios.

scripts/: Scripts de procesamiento y utilidades.

calcular_valores_gatillo.py: Calcula los valores gatillo.

ajustar_valores_gatillo.py: Ajusta y valida los valores gatillo.

verificar_versiones.py: Verifica las versiones de las librerías instaladas.


notebooks/: Notebooks de Jupyter para visualizaciones interactivas.

mapa_interactivo_gatillos.ipynb: Visualización de valores gatillo.

mapa_interactivo_temperaturas.ipynb: Visualización de temperaturas extremas y mortalidad.

requirements.txt: Lista de dependencias y sus versiones específicas.

README.md: Documentación del proyecto (este archivo).

Notas Adicionales

Dependencias del Sistema:

Algunas librerías geoespaciales como GDAL y PROJ son necesarias para geopandas, fiona y pyproj.
Usar Conda facilita la instalación de estas dependencias.
Uso de Entornos Virtuales:

Se recomienda encarecidamente utilizar un entorno virtual para evitar conflictos con otras instalaciones de Python en tu sistema.
Rutas Relativas:

Los scripts y notebooks utilizan rutas relativas para acceder a los datos, lo que mejora la portabilidad del proyecto.
Manejo de Errores:

Los scripts incluyen manejo de excepciones para gestionar posibles errores durante la ejecución.
Contacto
Autor: [Antonio Cantos Cuevas]
Email: [heloan@hotmail.es]

Licencia
Este proyecto está bajo la [Licencia MIT ] - ve el archivo LICENSE para más detalles.


¡Gracias por utilizar este proyecto! Si tienes alguna pregunta o sugerencia, no dudes en contactarme.