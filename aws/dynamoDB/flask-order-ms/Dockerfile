FROM python:3.9.15-alpine3.16
ENV PATH=/root/.local/bin:$PATH

ENV PYTHONPATH=/app

RUN pip install --upgrade pip \
  && pip install pipenv gunicorn

ADD . /app
WORKDIR /app
# install from the pipfile.lock
RUN pipenv install --system --deploy --ignore-pipfile
EXPOSE 5000
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "app:app"]
