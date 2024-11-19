import os
import csv

# Directorio donde se encuentran los archivos CSV
input_directory = "./dir_csv"
output_file = "file.csv"

# Lista para almacenar todas las filas de datos
all_data = []
header = None

# Leer todos los archivos en el directorio
for filename in os.listdir(input_directory):
    if filename.endswith(".csv"):
        filepath = os.path.join(input_directory, filename)
        with open(filepath, mode='r', encoding='utf-16-le') as csvfile:
            reader = csv.reader(csvfile)
            file_header = next(reader)  # Leer la cabecera del archivo
            
            # Guardar la cabecera si aún no se ha guardado
            if header is None:
                header = file_header
            
            # Asegurarse de que la cabecera es consistente
            elif header != file_header:
                raise ValueError(f"Cabeceras inconsistentes en el archivo: {filename}")
            
            # Leer el resto de las filas y almacenarlas
            for row in reader:
                all_data.append(row)

# Escribir el archivo unificado
with open(output_file, mode='w', encoding='utf-8', newline='') as csvfile:
    writer = csv.writer(csvfile)
    if header:
        writer.writerow(header)  # Escribir la cabecera
    writer.writerows(all_data)  # Escribir todos los datos

print(f"Archivos combinados en {output_file}")
