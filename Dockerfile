FROM python:3.11

ENV PYTHONUNBUFFERED 1

ENV DJANGO_SETTINGS_MODULE "src.settings"

WORKDIR /app

COPY . .

RUN pip install -U poetry

RUN poetry config virtualenvs.create false && poetry install

CMD ["gunicorn", "src.wsgi"]