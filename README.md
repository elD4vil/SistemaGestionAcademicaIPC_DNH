# 🚀 Guía para Ejecutar el proyecto SistemaGestionAcademicaIPC

Este documento explica cómo ejecutar el proyecto utilizando Docker en sistemas **Linux** y **Windows**. Sigue los pasos según tu sistema operativo.

---

## 🛠 Requisitos Previos

Para poder ejecutar este proyecto, necesitas tener instalado **Docker** y **Docker Compose** en tu sistema.

### 🔹 Instalación en Linux

Ejecuta los siguientes comandos en la terminal para instalar Docker y Docker Compose:

```sh
# Instalar paquetes necesarios
sudo apt update
sudo apt install -y docker.io docker-compose

# Verificar instalación
docker --version
docker-compose --version
```

Asegúrate de que el servicio de Docker esté corriendo:

```sh
sudo systemctl start docker
sudo systemctl enable docker
```

Si deseas ejecutar Docker sin `sudo`, agrega tu usuario al grupo `docker`:

```sh
sudo usermod -aG docker $USER
newgrp docker
```

### 🔹 Instalación en Windows

1. Descarga e instala **Docker Desktop** desde [la página oficial](https://www.docker.com/products/docker-desktop/).
2. Asegúrate de activar **WSL 2 Backend** si usas Windows 10/11.
3. Reinicia tu computadora después de la instalación.
4. Abre una terminal (PowerShell o Git Bash) y verifica que Docker esté instalado:

   ```sh
   docker --version
   docker-compose --version
   ```

---

## 🚀 Iniciar el Proyecto

Una vez que Docker está instalado, sigue estos pasos:

1. **Abre una terminal** y navega hasta la carpeta principal del proyecto.
2. Ejecuta el siguiente comando para iniciar el contenedor:

   ```sh
   docker-compose up
   ```

3. Una vez iniciado, el proyecto estará disponible en tu navegador en la siguiente URL:

   👉 [http://localhost:3006](http://localhost:3006)

Si deseas detener la ejecución del contenedor, presiona `Ctrl + C` en la terminal o ejecuta:

```sh
docker-compose down
```

4. Para iniciar secion en la pagina la contraseña es : 1234
---

¡Listo! Ahora puedes ejecutar correctamente el proyecto 🚀
