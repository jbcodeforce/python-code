#!/bin/bash
echo "##########################################################"
echo " A docker image for python 3.7 development: "
echo
docker run -e DISPLAY=192.168.1.89:0 --name jbpython -v $(pwd):/home -it --rm -p 5000:5000 jbcodeforce/python37 bash 
