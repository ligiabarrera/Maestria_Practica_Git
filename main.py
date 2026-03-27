from datapreputils import remove_null, fill_missing, binarize
from datapreputils.statistics import std_dev, mean, get_mode, get_harmonic_mean, get_geometric_mean
from datapreputils.normalization import min_max, z_score

data_array = [10, None, 20, float('nan'), 30, 10, 20 ,30, 40, 50]
print("=========================================================")
print("                     PROCESOS ESTADISTICOS               ")
print("=========================================================")

print(f"\n{'--- Datos originales':}")
print(f"  Array original       : {data_array}")
clean_data = remove_null(data_array)
print(f"  Sin valores nulos    : {clean_data}")
filled_data = fill_missing(clean_data, 0.1)
print(f"  Valores faltantes    : {filled_data}")
 

m= get_mode(filled_data)
med = get_harmonic_mean(filled_data)
geo= get_geometric_mean(filled_data)
me = mean (filled_data)
std= std_dev(filled_data)
umbral = sum(filled_data) / len(filled_data)

print("\nNormalizacion Min-", min_max(filled_data))
print("Normalizacion Z-Score", [round(x, 2) for x in z_score(filled_data, me, std)])
print("Binarización:", binarize(filled_data, umbral))
print("\nEliminar valores nulos:", clean_data)
print("Reemplazar valores faltantes:", filled_data)
print("\nCalculo de Moda:", m)
print("Calculo de Media Armonica", med)
print("Calculo de Media Geometrica:", geo)
