#!/bin/bash
echo "##########################################################"
echo " docker image for python development "
echo
docker run -e DISPLAY=192.168.1.89:0 --name jbpython -v $(pwd):/home -it --rm -p 8888:8888 ibmcase/python bash 
