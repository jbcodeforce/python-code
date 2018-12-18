from ubuntu
# bring system up-to-date
RUN apt-get update -qq && \
    apt-get upgrade -qqy && apt-get install -qqy sudo \
    && add-apt-repository ppa:jonathonf/python-3.6

# install a particular version of Python and other stuff
RUN apt-get install -qqy \
    python3.7 \
    python3.7-dev \
    python3.7-venv \
    python3-pip \
    curl 

RUN groupadd developer && useradd -g developer -m -d /home/jbcodeforce jbcodeforce && echo jbcodeforce:c0deforme | chpasswd

RUN mkdir work
WORKDIR /home/jbcodeforce/work
RUN chown -R jbcodeforce:jbcodeforce ./

EXPOSE 5000
USER jbcodeforce
