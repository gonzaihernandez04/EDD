# Recuperacion de informacion en redes sociales.

Facebook: Utiliza grafos no direccionales para por ejemplo relacionar a los usuarios y sus amistades.

El primer paso es registrarse como desarrollador en la plataforma de Meta (Facebook) y obtener un token de acceso para usar la API Graph de Facebook. Este token es necesario para autenticar las solicitudes y acceder a los datos permitidos. Ver Anexo: Facebook para una guía detallada.
https://untref-edd.github.io/apuntes/Anexos/Facebook.html


Cuenta: la de facebook.
https://developers.facebook.com/apps/

Para trabajar con la API de Facebook en Python, vamos a usar la librería facebook-sdk:
    pip install facebook-sdk


GENERA TOKEN DE 1 A 2 HORAS DE DURACION

Informacion de usuario actual:
/me?fields=id,name,email,birthday,location

Paginas que le gustan al usuario:
/me/likes?fields=name,category,fan_count,website


Cantidad de amigos
/me/friends?fields=name,id



PARA PROBAR TOKEN:
# Verificar información del usuario
curl -i -X GET "https://graph.facebook.com/me?access_token={your-token}"

# Verificar páginas que le gustan
curl -i -X GET "https://graph.facebook.com/me/likes?access_token={your-token}"


O verificar con python.
