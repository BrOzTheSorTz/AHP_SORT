# README: Aplicación para Clasificación de Alternativas con AHP-SORT

## Introducción

Esta aplicación implementa el método **AHP-SORT** para clasificar alternativas en distintas clases basándose en el análisis multicriterio. La aplicación utiliza archivos de datos para definir alternativas, criterios, clases y prioridades, y genera un archivo Excel con los resultados del análisis.

## Requisitos Previos

- **Python 3.8 o superior** instalado.
- Librerías necesarias:
  - `pandas`
  - `numpy`
  - `openpyxl`
  - Cualquier otra librería mencionada en el código.

Puedes instalar las dependencias necesarias con el siguiente comando:

```bash
pip install -r requirements.txt
```

## Estructura de Archivos

La aplicación requiere varios archivos Excel con un formato específico:

1. **Archivo de datos (e.g., `crimenes_spain_2023_norm.xlsx`)**:
   - Contiene las alternativas (filas) y los valores normalizados para cada criterio (columnas).
   - Las columnas deben representar los criterios.
   - Ejemplo:
     ```
     Alternativa    Criterio1    Criterio2    Criterio3
     Madrid         0.5          0.7          0.3
     Barcelona      0.6          0.8          0.2
     ```

2. **Archivo de comparación de criterios (e.g., `Comp_criterios.xlsx`)**:
   - Matriz de comparación pareada de los criterios (AHP).
   - Ejemplo:
     ```
     Criterio1    Criterio2    Criterio3
     1.0          3.0          0.5
     0.33         1.0          0.2
     2.0          5.0          1.0
     ```

3. **Archivo de clases (e.g., `Clases.xlsx`)**:
   - Define las clases y los valores que delimitan las prioridades.
   - Ejemplo:
     ```
     Clase    Criterio1    Criterio2    Criterio3
     1        0.1          0.2          0.3
     2        0.4          0.5          0.6
     3        0.7          0.8          0.9
     ```

4. **Archivos de prioridades para cada criterio (e.g., `PC_Crimenes_Norm.xlsx`)**:
   - Define las prioridades relativas para los rangos de cada criterio.
   - Ejemplo:
     ```
     Valor    Prioridad
     0.1      0.2
     0.5      0.6
     0.9      0.9
     ```

## Cómo Ejecutar

1. **Ubicar los Archivos**:
   - Asegúrate de tener todos los archivos necesarios en las rutas correspondientes:
     - Archivo de datos.
     - Archivo de comparación de criterios.
     - Archivo de clases.
     - Archivos de prioridades.

2. **Configurar el Archivo `main.py`**:
   - Modifica las rutas de los archivos en `main.py` para que correspondan a tus datos:
     ```python
     path_data = './data/crimenes_spain_2023_norm.xlsx'
     path_criterios = './data/Comp_criterios.xlsx'
     path_classes = './data/Clases.xlsx'
     path_prioridades = ['./data/Prioridades/PC_Crimenes_Norm.xlsx',
                         './data/Prioridades/PC_Robos_Norm.xlsx',
                         './data/Prioridades/PC_VEHICULOS_Norm.xlsx',
                         './data/Prioridades/PC_ORDEN_Norm.xlsx',
                         './data/Prioridades/PC_DROGAS_Norm.xlsx',
                         ]
     path_result = './results/ejercicio4.xlsx'
     ```

3. **Ejecutar la Aplicación**:
   - Desde la línea de comandos, ejecuta el archivo `main.py`:
     ```bash
     python main.py
     ```

4. **Verificar los Resultados**:
   - El resultado se generará en el archivo definido en `path_result` (por defecto: `./results/ejercicio4.xlsx`).
   - Este archivo incluirá:
     - Las prioridades globales de las alternativas.
     - La clase asignada a cada alternativa.

## Descripción del Código

### Clase `AHP_SORT`

Esta clase contiene toda la lógica del análisis:

1. **Constructor** (`__init__`):
   - Lee los datos de los archivos y los convierte en estructuras de datos internas.

2. **Método `apply`**:
   - Ejecuta el análisis completo:
     - Calcula los pesos de los criterios.
     - Calcula los pesos globales de las clases.
     - Calcula las prioridades globales de las alternativas.
     - Asigna las alternativas a clases.

3. **Métodos Auxiliares**:
   - `obtain_criterios_weights`: Calcula los pesos de los criterios usando el método del vector propio.
   - `obtain_classes_weights`: Calcula los pesos globales para las clases.
   - `obtain_priorities_alternatives`: Calcula las prioridades globales de las alternativas.
   - `priority_alternative`: Calcula la prioridad de una alternativa para un criterio específico usando interpolación lineal.

### Archivo `main.py`

Este archivo inicializa la clase `AHP_SORT` con las rutas configuradas y ejecuta el método `apply`.

## Salida del Análisis

El archivo resultante (`ejercicio4.xlsx`) tendrá las siguientes columnas:

- **Alternatives**: Lista de alternativas analizadas.
- **GlobalPriority**: Prioridad global de cada alternativa.
- **NivelSeguridad**: Clase asignada a cada alternativa.

Ejemplo de salida:

| Alternatives | GlobalPriority | NivelSeguridad |
|--------------|----------------|----------------|
| Madrid       | 0.73           | 2              |
| Barcelona    | 0.85           | 1              |

## Notas Importantes

- **Formato de los Archivos**: Asegúrate de que los archivos tengan el formato correcto. Cualquier inconsistencia puede generar errores.
- **Compatibilidad**: Los archivos Excel deben ser compatibles con `openpyxl`.
- **Extensibilidad**: Puedes adaptar este código para incluir más criterios o clases según tus necesidades.

## Soporte

Si tienes dudas o encuentras problemas al ejecutar la aplicación, verifica que:

1. Todos los archivos requeridos están en las rutas especificadas.
2. Los archivos tienen el formato adecuado.
3. Todas las librerías están instaladas correctamente.

Para más información o ayuda, contacta al desarrollador. 😊