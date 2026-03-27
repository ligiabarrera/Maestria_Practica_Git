📊 DataPrepUtils

DataPrepUtils es un paquete de Python orientado a la preparación y limpieza de datos, diseñado para facilitar tareas comunes en proyectos de Ciencia de Datos y Análisis de Datos.

Proporciona funciones simples, reutilizables y eficientes para el preprocesamiento, permitiendo mejorar la calidad de los datos antes de su análisis o modelado.

👥 Integrantes del Grupo

- Ligia Gabriela Barrera Copa
- Griselda Merino Herbas
- Deysi Sanchez
- José Luis Romero -->modificado

## Estructura del proyecto

DATAPREP_PROJECT
│
├── .venv/                 # Entorno virtual
├── datapreputils/         # Paquete de utilitarios
│   ├── __pycache__/
│   ├── __init__.py
│   ├── cleaning.py
│   ├── normalization.py
│   └── statistics.py
├── main.py                # Archivo principal
├── README.md              # Documentación
└── requirements.txt       # Dependencias del proyecto


⚙️ Funcionalidades

🧹 Módulo cleaning.py 

Funciones para la limpieza y tratamiento de datos:

Eliminación de valores nulos (None, NaN)
Imputación de valores faltantes
Preparación de datos para análisis posteriores

📏 Módulo normalization.py

Funciones para escalar y transformar datos:

Normalización Min-Max
Escala los datos a un rango entre 0 y 1
Estandarización Z-score
Centra los datos con media 0 y desviación estándar 1
Binarización de datos
Convierte los valores en 0 o 1 en función de un umbral definido:
Valores mayores al umbral → 1
Valores menores o iguales → 0
Útil en modelos de clasificación y machine learning

📈 Módulo statistics.py

Funciones estadísticas básicas:

Media aritmética
Moda
Media armónica
Media geométrica

## Ejecución

1. Ubicarse en la carpeta del proyecto.
2. Ejecutar el archivo principal:

python main.py
