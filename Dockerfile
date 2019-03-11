FROM python:3.6-stretch
ENV PATH=/root/.local/bin:$PATH
RUN pip install --upgrade pip \
  && pip install --user pipenv requests black pytest
WORKDIR /home/
EXPOSE 5000
CMD bash



