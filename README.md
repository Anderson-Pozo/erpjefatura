## Django ERP 💱

Este es un proyecto ERP enfocado al cobro de 
impuestos relacionados a patentes municipales, 
alcabalas y plusvalias.
## 📑 Configurar entorno de desarrollo

### Prerequisitos

- Python
- Editor de código
- PostgreSQL

### Instalación
1. Clonar el repositorio
    ```sh
   git clone https://github.com/Anderson-Pozo/erpjefatura.git
   ```
2. Crear entorno virtual
    ```sh
    virtualenv venv
    ```
3. Instalar requerimientos
    ```sh
    pip install -r requirements.txt
    ```
4. Crear la base de datos en PostgreSQL
    ```sh
   CREATE DATABASE IF NOT EXISTS MY_DATABASE;
   ```
5. En el directorio principal crear el archivo .env con el
siguiente contenido
    ```sh
    DB_ENGINE=django.db.backends.postgresql_psycopg2
    DB_NAME=YOUR_DB_NAME
    DB_USER=YOUR_DB_USER
    DB_PASSWORD=YOUR_USER_PASSWORD
    DB_HOST=localhost
    DB_PORT=5432
    
    HOST_EMAIL = YOUR_HOST_EMAIL
    USER_EMAIL = YOUR_EMAIL
    USER_EMAIL_PASSWORD = YOUR_PASSWORD_EMAIL
   ```
6. Aplicar las migraciones desde el directorio principal
    ```sh
   python manage.py makemigrations
   python manage.py migrate
   ``` 
7. Crear superusuario administrador
    ```sh
   python manage.py createsuperuser
   ```
8. Ejecutar la aplicación
    ```sh
   python manage.py runserver
   ```
9. Abrir el navegador en la dirección [localhost:8000](http://localhost:8000/)


## 🚀 Deployment
Se puede hacer deploy de este proyecto en AWS, Digital Ocean o Heroku

## ⚙ Construido con

* [Django]() - Framework web
* [Postgresql]() - Motor de base de datos
* [Bootstrap 4]() - Framework CSS

## 👦 Autores

* **Anderson Pozo**
* **Jhon Paillacho**
