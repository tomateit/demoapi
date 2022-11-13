FROM python:3.10

RUN apt-get update -y && apt-get upgrade -y && apt-get install -y curl python3-venv
RUN curl -sSL https://install.python-poetry.org | python3 -
RUN /root/.local/bin/poetry config virtualenvs.create false

WORKDIR /usr/src/app
COPY . .

RUN ~/.local/bin/poetry install
COPY .env .env
CMD [ "gunicorn", "-w", "4", "-b", "0.0.0.0:11104", "app_demoapi:app"]