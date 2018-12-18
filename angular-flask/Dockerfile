FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install flask

EXPOSE 5000
CMD ["flask", "app.py"]
