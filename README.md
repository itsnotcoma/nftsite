# NFT Marketplace
#### Proyecto Desarrollo de Aplicaciones Web

## Descripción del proyecto

Esta aplicacion web crea una especie de marketplace de NFTs, dobde los usuarios pueden subir su colecciones favoritas.

Las carracteristicas que estan actualmente implementadas son:
* Modelos para NFTs, colecciones, creadores y usuarios
* Los usuarios con acceso podran subir, actualizar y eliminar dichas colecciones, NFTs o creadores
* Esta implementada la opcion de poder subir una foto de perfil, pero no ha sido posible poder mostrarla aun.

## Instalar

Para poder utilizar este proyecto:
1. Crea un espacio virtual con Python (https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/development_environment).
1. Asumiendo que esta creado el entorno virtual, ejecutariamos los siguientes comandos (si estas utlizando Windows puede que necesites usar `py` o `py -3`, debendiendo de la version que utilices, en vez de `python`).
```
pip3 install -r requirements.txt
python3 manage.py makemigrations
python3 manage.py migrate
python3 manage.py createsuperuser # Crear un usuario para poder utilizar la base de datos:
python3 manage.py runserver

```
1. Habre el navegador `http://127.0.0.1:8000/` o `http://localhost:8000/` para visualizar la pagina web Django
1. `http://127.0.0.1:8000/admin/` para utilizar el sitio admin