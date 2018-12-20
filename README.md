# features-requests-app

## Getting Started

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

``` bash
pip install -r requirements.txt
```

Create the database

``` bash
python manage.py create_db
```

Initialize the database

``` bash
python manage.py init_db
```

Start the Flask development server:

``` bash
python manage.py runserver
```

Alternatively you can run the application using the flask run command to do that, set the Environmental variables.

``` bash
export FLASK_ENV=development
```

Then:

``` bash
flask run
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in a web browser to view the output of your service.

## Deployment Method

Currently, the app is deployed to heroku.
Alternatively, other deployment options exist.
The app could be deployed using Zappa and AWS Lambda

**Deploy With Zappa and AWS lambda**

``` bash
zappa init
```

``` bash
zappa deploy dev
```

Then for **local deployment**, there is the option of using Docker. by using the command to build your docker image:

``` bash
docker-compose up --build
```

then run the following to run the image:

``` bash
docker run -it -p 500:500 features-request-app_web
```

**Deploy with docker-machine**

Have your AWS Credentials already configured then run the following command to create a virtual machine:

``` bash 
docker-machine create --driver amazonec2 britecoreapp
```
You set the environment variables that belong to the virtual machine by issuing the following command:

``` bash
eval $(docker-machine env britecoreapp)
```

the command to build your docker image:

``` bash
docker-compose up --build
```

then run the following to run the image:

``` bash
docker run -d -p 500:500 features-request-app_web
```

```bash
docker-machine ip hobbyprojects
```



If you intend to deploy to Digital Ocean or AWS EC2 service, and want to implement
a CI/CD process, I have you in mind and have plans for CircleCI integration.

## Dev Approach

Design Architeture

#Built With

* Flask - The web framework used
* AWS (S3, Lambda) - Hosting Platform
* Gunicorn - Python WSGI HTTP Server for UNIX
* Knockout.js - Javascript framework
* Jquery - Javascript framework
* CircleCI - Continuous Deployment