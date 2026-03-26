import math

def remove_null(data):
    return [x for x in data if x is not None and not (isinstance(x, float) and math.isnan(x))]

def fill_missing(data, fill_value):
    return [fill_value if (x is None or (isinstance(x, float) and math.isnan(x))) else x for x in data]
