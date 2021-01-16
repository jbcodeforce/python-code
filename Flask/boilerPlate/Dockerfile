FROM python:3.7.4-stretch
ENV PATH=/root/.local/bin:$PATH

ENV PYTHONPATH=/app

RUN pip install --upgrade pip \
  && pip install pipenv flask gunicorn

ADD . /app
WORKDIR /app
# First we get the dependencies for the stack itself
RUN pipenv lock -r > requirements.txt
RUN python -m pip install -r requirements.txt
EXPOSE 5000
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "app:app"]
