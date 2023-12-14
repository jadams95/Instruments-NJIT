# Instruments-NJIT
### Instructions for Local Setup


#### Team Puzzles
- John Tyler Adams
- Ki Wai Kwan

 ##### requirements
 1. Postgres DB [Postgres_Install](https://www.enterprisedb.com/downloads/postgres-postgresql-downloads)
 2. Pip wrapper 
 
 ##### Local Setup
 - pip wrappper needs to install the following packages
 - pip install pyscopg2
 - pip install Pillow 
 - When installing the Postgres DB create a user to store the DB info in the settings.py

 - python manage.py runmigrations
 - python manage.py runmigrations core
 - python manage.py migrate


 
Database was created on the localhost. You need to run the 1. requirement and create a user that connection details are passed in the User, and Password

DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'postgres',
        'USER': 'postgres',
        'PASSWORD': '',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


###### Once DB Setup
1. create a superuser python .\manage.py createsuperuser
2. log into /admin console
3. create 5 items in the core module
4. click on view Website

 

### Errors
- If you get a description field on the Item models then delete default=False then run the runmigrations and migrate to create the description 