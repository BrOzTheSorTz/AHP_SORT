import numpy as np
import pandas as pd


class Reader():
    def __init__(self,  name="DEFAULT"):


        self.name = name

    def read(self,path_xlsx):
        df = pd.read_excel(path_xlsx)

        # Supongamos que la estructura es:
        # Criterios en la primera columna y clases ('ALTO', 'MEDIO', 'BAJO') en las otras columnas.

        # Extraer criterios y clases
        criterios = df.iloc[:, 0].tolist()  # Primera columna como lista
        clases = df.columns[1:].tolist()  # Encabezados de las columnas desde la segunda

        # Extraer solo los números como matriz
        matriz = np.array(df.iloc[:, 1:].values)  # Todas las filas, columnas desde la segunda

        # Ahora tienes:
        # criterios -> ['Crímenes', 'Robo', 'Relacionado con...', 'Orden Público', 'Drogas']
        # clases -> ['ALTO', 'MEDIO', 'BAJO']
        # matriz -> [[20, 100, 160], [5000, 95000, 180000], ...]
        df = pd.DataFrame(matriz,index=criterios,columns=clases)
        #print(criterios, clases, matriz)
        return matriz,df

    def read_all(self,path):
        df = pd.read_excel(path)

        # Supongamos que la estructura es:
        # Criterios en la primera columna y clases ('ALTO', 'MEDIO', 'BAJO') en las otras columnas.

        # Extraer criterios y clases
        filas_nombre = df.iloc[:, 0].tolist()  # Primera columna como lista
        columnas_nombre = df.columns[1:].tolist()  # Encabezados de las columnas desde la segunda

        # Extraer solo los números como matriz
        matriz = np.array(df.iloc[:, 1:].values)  # Todas las filas, columnas desde la segunda


        # print(criterios, clases, matriz)
        return filas_nombre,columnas_nombre,matriz