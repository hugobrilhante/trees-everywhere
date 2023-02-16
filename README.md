# Trees Everywhere

Project test for Youshop.

> Note: I would like to apologize for not having done the template part, if this is an impediment I will understand. I haven't worked with templates in years, and while the test deadline was excellent, I had a pretty unusual week, so I didn't have time to review how to do it.

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

[model_bakery](https://github.com/model-bakers/model_bakery) - Smart fixtures for better tests

[djangorestframework](https://github.com/encode/django-rest-framework) - Django REST framework is a powerful and flexible toolkit for building Web APIs.


## I would like to share an open source project I made.

[django-outbox-pattern](https://github.com/juntossomosmais/django-outbox-pattern) - A django application to make it easier to use the transactional outbox pattern