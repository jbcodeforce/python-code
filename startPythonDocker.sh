#!/bin/bash
echo "##########################################################"
echo " docker image for python development "
echo
docker run -e DISPLAY=192.168.1.89:0 --name jbcodeforcepython -v $(pwd):/home/jbcodefoce/work -it --rm -p 8888:8888 jbcodeforce/python37 /bin/bash 
