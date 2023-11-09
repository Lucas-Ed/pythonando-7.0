FROM python:3.11

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

CMD python mangege.py makemigrations

CMD python mangege.py migrate

CMD python manage.py runserver 0.0.0.0:8000