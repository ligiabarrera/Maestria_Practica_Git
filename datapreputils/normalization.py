def  min_max(data):
    """Normalización Min-Max → escala los valores al rango [0, 1]"""
    min_val = min(data)
    max_val = max(data)
    
    if max_val == min_val:
        return [0.0] * len(data)  # evita división por cero
    
    return [(x - min_val) / (max_val - min_val) for x in data]


def z_score(data, me, std):
    """Normalización Z-Score → (x - media) / desviación estándar"""
    if std == 0:
        return [0.0] * len(data)  # evita división por cero
    
    return [(x - me) / std for x in data]
def binarize(data, umbral):
    """
    Convierte valores en 0 o 1 según un umbral.
    Si el valor es mayor o igual al umbral → 1 (sí)
    Si el valor es menor al umbral → 0 (no)
    Ejemplo: umbral=25, [10,30] → [0,1]
    """
    return [1 if x >= umbral else 0 for x in data]