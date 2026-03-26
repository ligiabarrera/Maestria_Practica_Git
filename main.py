from datapreputils import remove_null, fill_missing
# std_dev, mean, get_mode, get_harmonic_mean, get_geometric_mean, min_max, z_score


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

print("Normalizacion Min-", min_max(filled_data))
print("Normalizacion Z-Score", z_score(filled_data, me, std))
print("Eliminar valores nulos:", clean_data)
print("Reemplazar valores faltantes:", filled_data)
print("Calculo de Moda:", m)
print("Calculo de Media Armonica", med)
print("Calculo de Media Geometrica:", geo)
