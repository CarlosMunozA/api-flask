# API-Rest

_Esta API esta desarrollada en el framework Flask, utiilzando lenguaje Python_


### Pre-requisitos 馃搵

_Clonar el repositorio de GITHUB, posicionarse en la rama master_

### Instalaci贸n 馃敡

_Instalar Flask_

```
pip install flask
```

_Correr Flask_

```
flask run
```

_La API esta configurada para correr en el puerto 5000 del localhost (localhost:5000)._

### Datos de prueba 馃殌

_Se crearon cuatro rutas las cuales est谩n protegidas por una api-key, la clave se enviara por correo, por temas de seguridad._

_Al realizar una petici贸n por Postman se debe agregar en el header una api-key del tipo x-api-key, su valor ser谩 enviado por correo_

```
http://localhost:5000/usersQuestions
http://localhost:5000/usersAnswer
http://localhost:5000/lastQuestion
http://localhost:5000/admin
```
_La ruta /usersQuestions Entrega informaci贸n de las preguntas que seran realizadas a los usuarios_

_La ruta /usersAnswer Obtiene las respuestas de los usuario a las preguntas realizadas_

_La ruta /lastQuestion Hace refencia a la 煤ltima entrega de respuestas que dio el usuario al cuestionario_

_La ruta /admin Contiene y devuelve la lista de usuarios que existe actualmente_

### Mejoras

_Dentro de las posibles mejoras est谩n:_

_Implementar un middleware para validar si la informaci贸n del usuario es fidedigna (Por ejemplo validaciones de correo, rut, etc.)_

_Agregar un archivo que contenga las variables de entorno por un tema de orden y seguridad_

_Agregar la informaci贸n en base de datos_

_Mejorar la seguridad de la API con autenticaci贸n_