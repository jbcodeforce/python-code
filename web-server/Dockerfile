FROM python:3.11-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

EXPOSE 80
CMD ["uvicorn", "fastapi_main:app", "--host", "0.0.0.0", "--port", "80"]