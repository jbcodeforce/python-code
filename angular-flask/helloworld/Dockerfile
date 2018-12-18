FROM python:3.7-alpine
ADD . /code
WORKDIR /code
RUN pip install -r requirements.txt

EXPOSE 5000
ENV FLASK_APP=firstApp.py
# CMD ["flask", "run"]
ENTRYPOINT [ "python" ]
CMD [ "firstApp.py" ]