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

Then for local deployment, there is the option of using Docker. by using the command to build your docker image:

``` bash
docker build -t features-request-app/featuresrequest
```

then run the following to run the image:

``` bash
docker run -it features-request-app/featuresrequest
```

If you intend to deploy to Digital Ocean or AWS EC2 service, and want to implement
a CI/CD process, I have you in mind and have plans for CircleCI integration.

## Dev Approach
