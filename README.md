# PDFtoCSV
Script en Python de gran utilidad para leer tablas en archivos PDF para su posterior uso.
## Introducción
### Finalidad
El objetivo es permitirle al usuario manipular en una planilla de cálculo tablas de datos con orígen en archivos PDF. Para ello el dataframe se exporta en formato CSV.
> [!IMPORTANT] 
> Es requisito que las tablas de datos esten incrustadas como texto, y no como imagen.
### Consideraciones
Es importante tener en cuenta que el script esta probado según los siguientes conceptos:
- El formato de presentación de las tabla de datos es consistente a través de todos los archivos PDF asociados a determinado modo.
- Los márgenes (top-left-bottom-right) entre la segunda y la anteúltima página son estáticos.
- El márgen superior de la primer página es un atributo del modo de operación. 
- Lo mismo sucede con el márgen inferior de la última página. Este mismo es variable en cada archivo PDF y por ende se establece manualmente en tiempo de ejecución.
- Cada modo se asocia a un banco. Actualmente estan en desarrollo: Galicia, Credicoop y Supervielle.
> [!NOTE]
> Se incluyeron archivos de prueba `test.pdf` en los directorios correspondientes a cada modo.
## Implementación
### Requisitos
- Python 3.11.5
- Java 8
- dependencias en requirements.txt
### Pasos
1. Clonar el repositorio
2. Abrir terminal y dirigirse al directorio del repositorio
3. Crear entorno virtual ```python -m venv venv_name```
4. Iniciar el entorno virtual (el comando es diferente según el terminal)
5. Instalar los paquetes necesarios: ```pip install -r requirements.txt```
6. Copiar los archivos PDF a la carpeta **pdf/mode**
7. Ejecutar el script: ```py main.py```

### Interfaz
Se implemento una ligera interfaz de menu por terminal, para facilitar la visualización e interacción con el mismo, y a su vez permite la validación de datos de entrada y seteo de parámetros por defecto. Se espera que el usuario indique 3 parámetros fundamentales:
1. Modo
2. Cantidad de páginas
3. Longitud relativa de la tabla en la última página