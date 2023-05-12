# Prueba Tecnica TalentPitch
Este repositorio contiene los archivos necesarios segun el desafio para la posicion de Data Engineer

Pasos para realizar:

1. Instalar los siguientes aplicaciones:

  * Instalar Docker
  * Instalar Docker Compose
  * Instalar Docker Desktop

2. Clonar el repositorio con git-clone

3. Crear las carpetas faltantes en la raiz del repositorio

```bash
$ mkdir logs plugins
 ```
 
 4. Ejecutar la entorno del yml (dependiendo del sistema operativo)

```bash
# Windows
docker-compose up -airflow-init

# Linux
$ docker compose up airflow-init
 ```
  
  5. Correr el siguiente comando (dependiendo del sistema operativo)

```bash
# Windows
docker-compose up --build

# Linux
sudo docker-compose up --build
```



