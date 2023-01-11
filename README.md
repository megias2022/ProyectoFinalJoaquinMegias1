Proyecto Final - Joaquín Megías - Blog de Playas

Sistema para gestionar contenido simple, en éste caso, imágenes de distintas playas del mundo que se pueden ver, actualizar o eliminar mediante un registro/ingreso de usuario... 

Se realizó un CRUD. 
CRUD es una metodología que te ayuda a crear una base de datos, para luego, darle lectura, actualizar o eliminar información en una base de datos ya existente, es una práctica común en el desarrollo web para manejar datos en aplicaciones.

:::: Requisitos ::::

* Tener instalado Python en tu sistema. Puedes descargar la última versión desde el sitio oficial: https://www.python.org/downloads/
* Tener instalado pip, que es el gestor de paquetes de Python. Si ya tienes Python instalado, deberías tenerlo disponible en tu terminal.
* Tener instalado Django. Para instalarlo, abre la terminal y escribe:

pip install django

Instalación
1. Descarga o clona el repositorio de tu aplicación Django en tu equipo.
2. Abre Visual Studio Code y selecciona "File > Open Folder" y elige la carpeta donde has guardado el repositorio.
3. Abre la terminal de Visual Studio Code (Ctrl + ñ).
4. Instala las dependencias necesarias para tu aplicación escribiendo en la terminal:
pip install -r requirements.txt

5. Crea la base de datos ejecutando las migraciones de Django:

python manage.py makemigrations
python manage.py migrate


Ejecución
1. Inicia el servidor de desarrollo de Django escribiendo en la terminal:

python manage.py runserver

2. Abre tu navegador y escribe en la barra de direcciones:

http://127.0.0.1:8000/

3. Ya puedes utilizar tu aplicación Django en el navegador.

