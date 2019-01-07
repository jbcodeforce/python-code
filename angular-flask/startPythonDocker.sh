#!/bin/bash
echo "##########################################################"
echo " docker image for python development "
echo
docker run -e DISPLAY=192.168.1.89:0 --name jbcodeforcepython -v $(pwd):/home/jbcodefoce/work -it --rm -p 3000:3000 jbcodeforce/python3.7 /bin/bash 
# docker run -v $(pwd):/home/work -it continuumio/miniconda  /bin/bash