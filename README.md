# PasswordManager


This application for saving your passwords for something in your teams 

For work it is required:

1) Download Docker https://www.docker.com/get-started
2) Clone the repository.
3) Open repository in your IDE.
4) In the terminal being in the root folder(djangoProject1/) of the application, write the commands:

a)"docker compose up" to run the container

b) you need to make migtations in DB with command:
"docker-compose run web python manage.py makemigrations" to build migrations and
"docker-compose run web python manage.py migrate" to do migrations

c)Than you need create superuser:
"docker-compose run web python manage.py createsuperuser" You need write name of superuser, email and password.
Congratulation you are almost there!

3) You need open application in browser and change name in address on http://localhost:8000/admin
login in and create users and groups Take users in groups and use aplications. 

P.S. If user don`t have groups it will see 404 errors
