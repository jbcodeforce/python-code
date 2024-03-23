FROM python:3.11-alpine
ADD . /code
WORKDIR /code
RUN pip install flask

EXPOSE 5000
CMD ["flask", "app.py"]
