# features-requests-app


#Getting Started

To work on the code, you'll need to clone your project's repository to your local computer. 

Create a Python virtual environment for the Flask project. This virtual environment allows you to isolate this project and install any packages you need without affecting the system Python installation. At the terminal, type the following command:

``` bash
 virtualenv .venv 
 ```


Activate the virtual environment:

```  bash
activate ./venv/bin/activate 
```

Install Python dependencies for this project:

```
pip install -r requirements.txt 
```


Create the database

```
python manage.py create_db --port 8000 
```

Initialize the database

```
python manage.py init_db --port 8000 
```


Start the Flask development server:

```
python manage.py runserver --port 8000 
```


Alternatively you can run the application using.

```
flask run --port 8000 
```

Open http://127.0.0.1:8000/ in a web browser to view the output of your service.