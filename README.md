# PDFtoCSV
Este pequeño programa es un "simple-yet-powerful" script desarrollado en Python que me fue de gran utilidad para resolver una problemática laboral en donde era necesario trabajar con extensas tablas de datos, y cuyos orígenes eran archivos con formato PDF.
## Finalidad
El objetivo de este script es permitirle al usuario trabajar sobre tablas de datos incrustadas en archivos PDF. Para ello es necesario procesar e interpretar, y posteriormente exportar los datos en un formato compatible. 
El diseño del programa esta basado en mi caso particular de estudio, donde todos los archivos PDF comparten ciertas características en común a tener en cuenta, a saber:
- El formato de la primer página es igual para todos los PDF.
- El formato de todas las páginas entre la primera y la última, es el mismo.
- El formato de la última hoja respeta el formato de las hojas previas a excepción del largo de la tabla, el cual será variable.
> [!NOTE]
> El script cuenta con un archivo de prueba incorporado, denominado `test.pdf`, para poder realizar una prueba inicial.

## Implementacion
El scripting esta realizado en lenguaje Python y, adicionalmente, se utilizaron principalmente dos librerías:
- `tabula-py`
- `pandas`

Con `tabula-py` realizamos la lectura de los archivos PDF, definiendo el área total (de manera relativa, %) y el ancho de cada columna. Este paso es ligeramente arbitrario, pero tiene bases tanto en inspección visual como en el uso de la metodología "trial and error".
> [!IMPORTANT] 
> El correcto procesamiento de las tablas PDF yace en una correcta delimiticación del área a interpretar. De tal modo, para adaptar el script a otros archivos es imperativo corregir adecuadamente los límites del dicha área.

Los datos recoletados por `tabula.read_pdf()` se pasan a lista y se van concatenando a medida que el programa va recorriendo iterativamente las hojas del documento PDF en cuestión.
Finalmente, mediante la utilización de DataFrames de la libreria `pandas`, procedemos a crear un DataFrame con la información recolectada para ser exportada gracias al método `.to_csv()`
### Deployment
> [!WARNING]
> Es muy importante no perder de vista que, dada la variabilidad en la cantidad de hojas y el tamaño de la tabla de la hoja final, es necesario definir estos parámetros cada vez que se ejecute este script.

Para arrancar el servicio en su totalidad luego de clonar el repositorio, deben realizarse los siguientes pasos:
1. Crear entorno virtual: ```python -m venv /path/to/new/virtual/environment```
2. Arrancar el entorno virtual. Este comando depende del sistema, por ejemplo en bash: ```source venv_path/Scripts/Activate```
3. Instalar los paquetes necesarios: ```pip install -r requirements.txt```
4. Copiar los archivos PDF a la carpeta **pdf**
5. Iniciar el servicio: ```py main.py pdf_file csv_file pages last_page_length```
     - `pdf_file`: nombre del archivo a procesar (**required**)
     - `csv_file`: nombre del archivo de destino (*optional*)
     - `pages`: cantidad de páginas a procesar (*optional*)
     - `last_page_length`: tamaño relativo de la última página; teniendo en cuenta el caso particular de estudio, será un número entre 23 y 92 (*optional*)
> [!CAUTION]
> Los argumentos se pasan al intérprete (terminal) **en el orden indicado**. El script funciona con uno, varios o ningún argumento.


> [!TIP]
> Si se omite:
1. `csv_file`: se exportará con el mismo nombre del archivo de origen.
2. `pages`: se tomará el valor por defecto, calibrado al archivo de prueba
3. `last_page_length`: se tomará el valor por defecto, calibrado al archivo de prueba
El órden de precedencia de los argumentos es:
`pdf_file` -> `pages` -> `csv_file` -> `last_page_length`

