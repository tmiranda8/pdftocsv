# PDFtoCSV
Script desarrollado en Python, de gran utilidad para transformar extensas tablas de datos para su posterior uso en, por ejemplo, Microsoft Excel.
## Finalidad
El objetivo es permitirle al usuario manipular tablas de datos con orígen en archivos PDF, en una planilla de cálculo. Para ello es necesario convertir los datos en un formato acorde para importarlos, como CSV.
> [!NOTE]
> Se ha incluido el archivo de prueba `test.pdf` para que el usuario pueda probar rápidamente la lógica de funcionamiento. Para ello, correr ```py main.py``` en terminal, que devolverá el índice de la fila correspondientes a cada salto de página. `test.csv` deberá encontrarse en el directorio correspondiente. 

## Implementacion
> [!IMPORTANT] 
> Es necesario que los datos esten incrustados como texto en el archivo PDF. De lo contrario, no es posible su procesamiento (por ej, si estan como imagen).
El script esta orientado a procesar de forma dinámica archivos que comparten ciertas características en común:
- El formato de presentación de los datos, como la disposición de las columnas, es igual en todos los PDF.
- Los márgenes de todas las páginas entre la primera y la última, es el mismo.
- Unicamente el márgen superior de la primer página y el márgen inferior de la última son ajustables.
> [!NOTE]
Luego de procesar los datos, es necesario adicionalmente editarlos en bulk (por ejemplo, con Power Query). Hace falta quitar puntuacion innecesaria, cambiar el punto decimal (de ',' a '.') y finalmente el tipo de dato de las columnas, de texto a numero decimal.

### Deployment
Python utilizará principalmente dos librerías:
- `tabula-py`
- `pandas`
> [!WARNING]
> Es requisito tener instalado Java Runtime Environment. 

Luego de clonar el repositorio, realizar los siguientes pasos para ejecutar el script:
1. Crear entorno virtual ```python -m venv /path/to/new/virtual/environment```
2. Iniciar el entorno virtual ```source venv_path/Scripts/Activate```
3. Instalar los paquetes necesarios: ```pip install -r requirements.txt```
4. Copiar los archivos PDF a la carpeta **pdf**
5. Ejecutar el script:
```py main.py pdf_file csv_file pages last_page_length first_page_length```
> [!CAUTION]
> Los argumentos se pasan al intérprete (terminal) **en el orden indicado**.

- `pdf_file`: nombre del archivo a procesar (**required**)
- `csv_file`: nombre del archivo de destino (*optional*)
- `pages`: cantidad de páginas a procesar (*optional*)
     - es posible ```py main.py pdf_file pages``` 
- `last_page_length`: tamaño relativo (0-100%) de la última página (*optional*)
- `first_page_length`: tamaño relativo (0-100%) de la última página (*optional*)

> [!NOTE]
> El script funciona con uno, ningún o con algunas combinaciones especificas de argumentos. El órden de importancia de los argumentos es: `pdf_file` -> `pages` -> `csv_file` -> `last_page_length`.

Si se omite:
- `pdf_file`: se procesará el archivo de prueba
- `csv_file`: se exportará con el mismo nombre del archivo de origen.
- `pages`: se tomará el valor por defecto, calibrado al archivo de prueba.
- `last_page_length`: se tomará el valor por defecto, calibrado al archivo de prueba.
- `first_page_length`: se tomará el valor por defecto, calibrado al archivo de prueba.

