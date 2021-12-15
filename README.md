# Backend_auth

Backend auth para el proyecto Bolet

Este repositorio esta hecho con la finalidad de dar funcionamiento al microservicio de usuario para la pagína Bolet, este consiste en la creacion de la cuenta de usuario, obtener infomación del usuario y generar la autentificación necesaria para el correcto uso de la pagína principal.

Los requerimientos usados para este repositorio se encuentran en el documento requirements.txt que se encuentra en la base principal del repositorio.

datos del requirements.txt :
    Django==3.2.9
    djangorestframework==3.12.4
    djangorestframework-simplejwt==5.0.0
    psycopg2-binary==2.9.1
    PyJWT==2.1.0
    gunicorn==20.1.0
    django-heroku==0.3.1

forma de instalación: pip install -r requirements.txt

Este repositorio hara uso del Api Gateway Bolet para realizar sus funciones de backend.