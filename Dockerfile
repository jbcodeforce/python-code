from ubuntu
# bring system up-to-date
RUN apt-get update -qq && \
    apt-get upgrade -qqy

# install a particular version of Python and other stuff
RUN apt-get install -qqy \
    python-virtualenv \
    libpq-dev \
    python3.7 \
    python3.7-dev \
    python3.7-venv \
    python3-pip \
    curl \
    sudo

RUN adduser --system --home /home/jbcodeforce jbcodeforce \
&& addgroup --system  jbcodeforce

RUN mkdir work
WORKDIR /home/jbcodeforce
RUN chown -R jbcodeforce:jbcodeforce ./

EXPOSE 5000
USER jbcodeforce
