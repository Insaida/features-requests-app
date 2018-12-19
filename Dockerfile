FROM python:2.7-alpine
ENV FLASK_APP featurerequests

#EXPOSE 5000

WORKDIR /opt/code

ADD . /opt/code
RUN pip install -r requirements.txt
RUN python manage.py create_db
RUN python manage.py init_db

CMD ["flask", "run", "--host", "0.0.0.0"]