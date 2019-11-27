# pull official base image
FROM python:3.7.4-alpine
ENV PATH=/root/.local/bin:/project/deps/bin:$PATH

# install dependencies
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add postgresql-dev && \
    apk add netcat-openbsd && \
    pip install --upgrade pip && \
    pip install --upgrade --user pipenv 

# set working directory
WORKDIR /usr/src/app

# set environment varibles
# Prevents Python from writing pyc files to disc
ENV PYTHONDONTWRITEBYTECODE 1
# Prevents Python from buffering stdout and stderr 
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/usr/src/app/

# add and install requirements
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/app/entrypoint.sh
RUN chmod +x /usr/src/app/entrypoint.sh

# add app
COPY . .

