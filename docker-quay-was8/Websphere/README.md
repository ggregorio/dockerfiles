# Docker Template
El proposito de este template es mantener imagenes de docker

## Pipeline
EL pipeline consiste en la construccion de la imagen y la subida al registry con el nombre del branch como el tag de la imagen 

## Como usar el template
Modificar el dockerfile a gusto. El pipeline buildea una imagen con el nombre del branch como tag.
Por ejemplo, si se crea un branch con el nombre "prueba" el pipeline crea una imagen con el tag "prueba"

