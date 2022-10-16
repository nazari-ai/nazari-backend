FROM python:3.9

# Keeps Python from generating .pyc files in the container
ENV PYTHONDONTWRITEBYTECODE=1

# Turns off buffering for easier container logging
ENV PYTHONUNBUFFERED=1

ENV APP_HOME /app
WORKDIR $APP_HOME

COPY . ./
# Install & use pipenv
RUN pip install --upgrade pip
RUN apt-get update && apt-get install gcc -y \
    wget\
    ;

RUN pip install pipenv && pipenv install --system --deploy --ignore-pipfile

WORKDIR /app
COPY . /app

CMD exec gunicorn --bind :$PORT --workers 1 --worker-class uvicorn.workers.UvicornWorker  --threads 8 main:app