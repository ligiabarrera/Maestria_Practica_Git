"""Módulo de estadísticas para el proyecto de Data Preprocessing.
Contiene funciones para calcular la moda, media armónica, media geométrica, media aritm"""
# Cambio de Jose Luis Romero

import math
import statistics

# Función para calcular la moda
def get_mode(data):
    frecuencia = {}
    
    for num in data:
        if num in frecuencia:
            frecuencia[num] += 1
        else:
            frecuencia[num] = 1

    mode = max(frecuencia, key=frecuencia.get)
    return mode


# Función para calcular la media armónica
def get_harmonic_mean(data):
    if not data:
        raise ValueError("Error, La lista esta vacía")
    
    if any(x == 0 for x in data):
        raise ValueError("Error, La lista contiene un valor cero")
    
    lenght = len(data)
    suma_reciprocos = sum(1 / x for x in data)
    return lenght / suma_reciprocos
    
    
def get_geometric_mean(data):
    
    if not data:
        raise ValueError("La lista de datos no puede estar vacía.")
    if any(x <= 0 for x in data):
        raise ValueError("La media geométrica solo se define para números positivos.")

    # Opción 1: Utilizando la librería estándar (Recomendado por eficiencia)
    media_geo = statistics.geometric_mean(data)
    
    return media_geo

def mean(data):
    return sum(data) / len(data)


def std_dev(data):
    m = mean(data)
    variance= sum((x-m)**2 for x in data)/len(data)
    return math.sqrt(variance)