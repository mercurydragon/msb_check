
FROM python:3.8-slim

WORKDIR /app

COPY . .

RUN pip3 install -r ./requirements.txt
RUN python manage.py migrate

CMD ["gunicorn", "wsgi:application", "--bind", "0:8000" ]

