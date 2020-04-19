# Flask Vehicle Location

## **Instalacion con docker**

### requisitos:
- docker: https://docs.docker.com/install/

- docker-compose: https://docs.docker.com/compose/install/

clonar el proyecto

dentro del proyecto usar el siguiente comando

`docker-compose up -d`

una vez terminado la url será: http://0.0.0.0:5000

si requieres ver el log puedes usar este comando

`docker logs -f  web_flask`

para ver el log de Postgres

`docker logs -f  psql_flask`

## **Instalacion con VirtualEnv**

requisitos:

- virtualenv: https://pypi.org/project/virtualenv/
- virtualenvwrapper (opcional) https://virtualenvwrapper.readthedocs.io/en/latest/


### Crear el ambiente

si usas virtualenvwrapper 

`mkvirtualenv <nombre_ambiente>`

si usas virtualenv

`python3 -m venv /path/to/new/virtual/<nombre_ambiente>`


`source /path/to/new/virtual/<nombre_ambiente>/activate`

### Instalar las dependencias


`pip install -r requirements.txt`

Si todo se instalo correctamente ya solo es necesario ejecutar boot.sh

`./boot.sh`

## Pruebas unitarias

En caso de que estes usando docker 
puedes usar el siguiente comando

`docker exec -ti web_project python3 simple_testing.py -v`

Si usas virtualenv o virtualenvwrapper

`python3 simple_testing.py -v`


### Sitio Web:
https://github.com/erickdsama/locationclient

http://testingfront.s3-website-us-east-1.amazonaws.com/

usuario: erick@gmail.com

contraseña: 123456

### Documentación de api:

https://documenter.getpostman.com/view/148100/Szf6WTAo?version=latest#8f4c4ccf-7d97-4ece-955e-ade32338c03c
