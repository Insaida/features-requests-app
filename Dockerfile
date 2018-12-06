FROM python:3.7.1-alpine
ENV FLASK_APP featurerequests

EXPOSE 5000

WORKDIR /app

ADD . /app/
RUN pip install -r requirements.txt
RUN python manage.py create_db
RUN python manage.py init_db

ENTRYPOINT ["flask", "run", "--host", "0.0.0.0"]