# Define python 3 image with needed libraries to do mathematical code
FROM python:3.9
ENV PATH=/root/.local/bin:$PATH
RUN pip install --upgrade pip \
  && pip install --user numpy scipy matplotlib astropy
WORKDIR /home
EXPOSE 5000
CMD bash