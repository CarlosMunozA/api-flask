# API-Rest

_Esta API esta desarrollada en el framework Flask, utiilzando lenguaje Python_


### Pre-requisitos 📋

_Clonar el repositorio de GITHUB, posicionarse en la rama master_

### Instalación 🔧

_Instalar Flask_

```
pip install flask
```

_Correr Flask_

```
flask run
```

_La API esta configurada para correr en el puerto 5000 del localhost (localhost:5000)._

### Datos de prueba 🚀

_Se crearon cuatro rutas las cuales están protegidas por una api-key, la clave se enviara por correo, por temas de seguridad._

_Al realizar una petición por Postman se debe agregar en el header una api-key del tipo x-api-key, su valor será enviado por correo_

```
http://localhost:5000/usersQuestions
http://localhost:5000/usersAnswer
http://localhost:5000/lastQuestion
http://localhost:5000/admin
```
_La ruta /usersQuestions Entrega información de las preguntas que seran realizadas a los usuarios_

_La ruta /usersAnswer Obtiene las respuestas de los usuario a las preguntas realizadas_

_La ruta /lastQuestion Hace refencia a la última entrega de respuestas que dio el usuario al cuestionario_

_La ruta /admin Contiene y devuelve la lista de usuarios que existe actualmente_

### Mejoras

_Dentro de las posibles mejoras están:_

_Implementar un middleware para validar si la información del usuario es fidedigna (Por ejemplo validaciones de correo, rut, etc.)_

_Agregar un archivo que contenga las variables de entorno por un tema de orden y seguridad_

_Agregar la información en base de datos_

_Mejorar la seguridad de la API con autenticación_