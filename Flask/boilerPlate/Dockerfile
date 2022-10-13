FROM python
ENV PATH=/root/.local/bin:$PATH

ENV PYTHONPATH=/app

RUN pip install --upgrade pip \
  && pip install pipenv flask gunicorn flasgger

ADD . /app
WORKDIR /app
# First we get the dependencies for the stack itself
RUN pipenv lock -d
RUN python -m pip install -r Pipfile
EXPOSE 5000
CMD ["gunicorn", "-w 4", "-b 0.0.0.0:5000", "app:app"]
