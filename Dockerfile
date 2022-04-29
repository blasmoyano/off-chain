FROM python:3.8.13

WORKDIR /usr/src/off_chain

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV DJANGO_SETTINGS_MODULE="off_chain.settings.production"

RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

COPY . .


RUN python manage.py makemigrations authentication --settings=off_chain.settings.production
RUN python manage.py makemigrations balance --settings=off_chain.settings.production
RUN python manage.py migrate --settings=off_chain.settings.production
RUN python manage.py collectstatic --no-input --settings=off_chain.settings.production

CMD ["sh","-c","gunicorn off_chain.wsgi:application --bind 0.0.0.0:8000" ]
