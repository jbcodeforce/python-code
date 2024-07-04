FROM python:3.7.4-stretch
ENV PATH=/root/.local/bin:$PATH

ENV PYTHONPATH=/app

RUN pip install --upgrade pip \
  && pip install pipenv flask gunicorn

ADD . /app
WORKDIR /app

EXPOSE 5000
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "staticApp:app"]
