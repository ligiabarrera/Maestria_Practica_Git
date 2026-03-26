"""Módulo de limpieza para el proyecto de Data Preprocessing.
Contiene funciones para eliminar valores nulos y reemplazar valores faltantes en un conjunto de datos"""
import math

# Función para eliminar valores nulos
def remove_null(data_array):
    return [x for x in data_array if x is not None and not (isinstance(x, float) and math.isnan(x))]

# Función para reemplazar valores faltantes
def fill_missing(data_array, value):
    return [
        value if x is None or (isinstance(x,float) and math.isnan(x))
        else x
        for x in data_array
    ]