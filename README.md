Objetivo: se tienen fotogradias y videos duplicados, solo se deben de copiar a una sola carpeta de destino evitando duplicar los archivos
ademas se deben de organisar por año y fecha

1 leer las fotos y videos de dentro de una carpeta y sus subcarpetas
2 debe de leer el archivo obtener la fecha de creacion, nombre del archivo y tamaño en bytes
3 debe de copiar el archivo a una carpeta de destino y debe de crear una subcarpeta con el nombre del sigiente formato 
  YYYY_mm si no exsiste la carpeta 
4 solo debe de copiar archivos de fotos y videos cullos atributos la fecha de creacion, nombre del archivo y tamaño en bytes no exsistan en la carpeta de destino
5 hacer una lista de los archivos de fotos y videos duplicados y poner el contenido en un archivo llamado dupllicdos.txt donde especifique el path completo de las fotos y videos duplicados
# Photo and Video Organizer

## Objective
The goal of this project is to organize and deduplicate photos and videos by copying them to a single destination folder, avoiding duplicates. Additionally, the files should be organized by year and date.

## Functional Requirements

1. **Read Photos and Videos**: The program should read photos and videos from a specified folder and its subfolders.
2. **Extract File Attributes**: The program should extract the creation date, file name, and size in bytes for each file.
3. **Copy Files to Destination**: The program should copy each file to a destination folder, creating a subfolder in the format `YYYY_mm` if it does not already exist.
4. **Avoid Duplicates**: The program should only copy files whose attributes (creation date, file name, and size in bytes) do not already exist in the destination folder.
5. **Log Duplicates**: The program should create a list of duplicate photos and videos and save the full path of these duplicates in a file named `duplicates.txt`.

## Usage

1. **Specify Source and Destination**: Define the source folder containing the photos and videos and the destination folder where the organized files will be copied.
2. **Run the Program**: Execute the program to start the deduplication and organization process.
3. **Check Duplicates Log**: Review the `duplicates.txt` file to see the list of duplicate files that were not copied.

## Example

```bash
python organize_photos_videos.py --source /path/to/source --destination /path/to/destination
