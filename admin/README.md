Esta sección detallará aspectos técnicos sobre la instalación del servidor.

## Objetivos

El objetivo de hostear los archivos en anakena es tener una especie de "backup" o repositorio desde el cual poder obtener todos los mods necesarios en caso de querer volver a abrir el servidor en otra maquina.

Como objetivos tengo:

1. Tener instrucciones de como iniciar el servidor desde cero, y como descargar los mods desde aca
2. Tener un listado de los mods utilizados y sus descripciones

## Tutoriales

Para iniciar tuve que ver algunos tutoriales, de los que destaco y no quiero perder:

1. [Como usar Iris con Forge](https://www.youtube.com/watch?v=NPNzp4N05xg)
2. [Versiones de Oculus + Rubidium](https://www.youtube.com/watch?v=dOckgD2W8_0)
3. [Versiones de Create + Rubidium](https://www.reddit.com/r/CreateMod/comments/16r1cow/can_not_start_game_with_create_and_rubidium/)

## Server

Para instalar el servidor usare Docker Compose. En el directorio `docker` estaran los archivos necesarios para descargar y ejecutar `docker compose up -d`. A la fecha no tengo conocimientos de como respaldar el servidor y el mundo.

Empecé viendo [este tutorial](https://www.youtube.com/watch?v=NUlUk6hc-mQ), y luego me guié por la [documentación de ITZG](https://docker-minecraft-server.readthedocs.io/en/latest/)

Lo que obtuve es una manera de "portar" el servidor con un docker-file simple y un archivo de texto con los links de descarga de los mods.

### Archivos

El archivo `/admin/files.json` contiene todos los mods y librerías necesarias para este servidor particular. Este archivo fue hecho a mano y está ligeramente desordenado, pero me gusta porque le pude meter harta información y me permite hacer muchas cosas jeje

El archivo `/admin/docker/docker-compose.yml` es el docker file que permite levantar el servidor. Para que funcione, en el archivo `/admin/docker/.env` debe estar seteada la variable DATA_PATH a un directorio (tiene que ser la ruta absoluta) donde se desea guardar la data del mundo.

El archivo `/admin/server_mods_generator.py` utiliza el archivo `files.json` para generar el archivo `mods.txt` que contiene los enlaces de descarga de todos los mods que requiere el servidor. Luego de generarlo hay que moverlo a `/admin/docker`, y el servidor descargará los mods si es que es necesario (si ya están descargados no lo hace).

### Comandos utiles

Iniciar el servidor:
```bash
docker compose up -d
```

Cerrar el servidor:
```bash
docker compose down
```

Acceder a la consola de Minecraft (por ejemplo para usar comandos como give, kill, gamemode, etc.)
```bash
docker exec -i mc rcon-cli
```
