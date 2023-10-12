# Proyecto de Microservicios con FastAPI y Nginx

## Descripción

Este proyecto es una plantilla base para desarrollar localmente un conjunto de microservicios usando FastAPI. Se utiliza Nginx como un API Gateway para enrutar las solicitudes a los microservicios correspondientes.

## Estructura del Proyecto

- `/service1`: Código y recursos del microservicio 1.
- `/service2`: Código y recursos del microservicio 2.
- `/nginx`: Archivos de configuración de Nginx para el API Gateway.
- `/docker-compose.yml`: Archivo de Docker Compose para orquestar los microservicios y Nginx.

## Funcionamiento del API Gateway

Este proyecto utiliza Nginx como un API Gateway para enrutar las solicitudes a los microservicios individuales. A continuación, se explica cómo funciona este enrutamiento:

- **Worker Processes y Worker Connections**: Nginx se configura con un solo proceso de trabajador (`worker_processes 1`) y un límite de conexiones (`worker_connections 1024`).

- **Upstream**: Se definen bloques `upstream` para cada microservicio. Por ejemplo, `service1_backend` y `service2_backend` apuntan a los microservicios `service1` y `service2`, respectivamente. Cada `upstream` especifica la dirección y el puerto en los que se ejecutan los microservicios.

- **Server Block**: El servidor Nginx escucha en el puerto 80. Dentro de este bloque, se configuran ubicaciones (`location`) para redirigir las solicitudes entrantes.

- **Location Block**: Cada ubicación corresponde a un microservicio. Por ejemplo, `/service1/` redirige las solicitudes a `service1_backend`, y `/service2/` redirige las solicitudes a `service2_backend`. El comando `proxy_pass` envía la solicitud al microservicio correspondiente.

Esto permite que Nginx sirva como un punto de entrada para las solicitudes y las enrute a los microservicios adecuados. Al agregar más microservicios, puedes seguir esta misma estructura, configurando los bloques `upstream` y `location` según corresponda.

## Agregar Más Microservicios

Si deseas agregar más microservicios a este proyecto, puedes seguir estos pasos:

1. Crea el código del nuevo microservicio en un directorio dentro de `/microservices`.

2. Agrega un bloque `upstream` en el archivo `nginx.conf` para el nuevo microservicio, especificando la dirección y el puerto en los que se ejecutará.

3. Agrega un bloque `location` en el archivo `nginx.conf` para el nuevo microservicio, redirigiendo las solicitudes al `upstream` correspondiente.

4. Asegúrate de que el nuevo microservicio esté configurado en tu archivo `docker-compose.yml`.

5. Ejecuta `docker-compose up -d` para iniciar el nuevo microservicio y Nginx.

Con estos pasos, Nginx enrutará las solicitudes al nuevo microservicio de la misma manera que lo hace con los existentes.


## Requisitos de Instalación

- Docker

## Instalación y Uso

1. Clona este repositorio:

   ```bash
   git clone https://github.com/nicolas-97/fast_api_microservices.git

2. Levanta los contenedores:
    Asegurate de no tener ocupado el puerto 80 de ser asi, cambie el puerto o termine el proceso que ocupa dicho puerto en el docker-compose del servicio api-gateway y ejecuta:
    ```bash
    docker compose up -d

3. Para acceder al microservicio: service1 tienes que dirigirte a: http://localhost/service1/

4. Para acceder al microservicio: service2 tienes que dirigirte a: http://localhost/service2/
