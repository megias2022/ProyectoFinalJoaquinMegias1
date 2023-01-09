Sistema para gestionar contenido simple

Este proyecto tiene como objetivo crear un sistema para la administración de contenido. 
Cosas que puedes hacer:
* Crear, buscar, leer, actualizar y eliminar registros.
* Establecer artículos como titulares.
* Añadir una imagen para cada artículo.


Instalar en iOS
Para instalar este software necesitas hacer:

*Comprobar la versión de Python
Este proyecto se escribió con python 3.11.0, por lo que le sugiero que pruebe con esta versión o superior para no tener problemas de compatibilidad.

Cómo verifico mi versión de python,
en sistemas *nix:
> python --versión
> Python 3.11.0
en Windows:
c:\> py --versión
c:\> Python 3.11.0

Instalar dependencias
Para instalar las dependencias, debe ejecutar pip install, asegúrese de estar en la carpeta del proyecto y puede ver el archivo requirements.txt cuando hace un ls o dir:
> pip install -r requisitos.txt

Este último devolverá un montón de cosas en la terminal.
Algunos sistemas operativos como iOS requerirán que uses pip3 en lugar de pip

Configuración de la aplicación Django
Una vez que termine la instalación de las dependencias, debe ejecutar algunos comandos Django.

Migraciones
Inicializar la base de datos * nix:
> python manage.py migrate
Windows:
c:\> py administrar.py migrate

Ejecutar el servidor de prueba
> python manage.py runserver
Windows:
c:\> py manage.py runserver

Ir a localhost:8000/ 
para tener acceso a la aplicación.
Si todo va bien, debería poder abrir el navegador y ver cómo se ejecuta la aplicación.
