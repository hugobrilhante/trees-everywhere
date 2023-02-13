# Trees Everywhere

Project test for Youshop.

## How to use?

> Assuming you docker and pre-commit (optional but recommended)

Clone the project: 

````shell
git clone https://github.com/hugobrilhante/trees-everywhere.git
````

Enter the project folder and create a `.env` use` .env.example`

```shell
cd trees-everywhere
cp .env.example .env
```

Build image 

```shell
docker compose build
```

Start project 

```shell
docker compose up
```    
    

> Now he performs the migrations, create a super user with login `admin` and password `qwerty` and starts the project in [localhost](http://127.0.0.1:8000)

## To guarantee a quality code, install the [pre-commit](https://pre-commit.com/#install). 

Update hooks (optional)

```shell
pre-commit autoupdate
```

Install the hooks

```shell
pre-commit install
```
    

> Now the linters will be executed at each commit

To check if everything is in order before the commit run

```shell
pre-commit run -a
```

## Installed packages


[django-configurations](https://github.com/jazzband/django-configurations) - A helper for organizing Django settings.

- [django-cache-url](https://github.com/epicserve/django-cache-url) - Use Cache URLs in your Django application.
  
- [dj-database-url](https://github.com/kennethreitz/dj-database-url) - Use Database URLs in your Django Application.
     
- [dj-email-url](https://github.com/migonzalvar/dj-email-url) - Use an URL to configure email backend settings in your Django Application.

[gunicorn](https://gunicorn.org/) - WSGI HTTP Server for UNIX

[psycopg2](https://www.psycopg.org/) - Python-PostgreSQL Database Adapter

[whitenoise](https://github.com/evansd/whitenoise) - Radically simplified static file serving for WSGI applications

