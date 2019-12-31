#!/bin/bash
echo "##########################################################"
echo " A docker image for python 3.7 development: "
echo

if [[ -z "$IPADDR" ]]
then
    export IPADDR=$(ifconfig en0 |grep "inet " | awk '{ print $2}')
fi

docker run -e DISPLAY=$IPADDR:0 -v /tmp/.X11-unix:/tmp/.X11-unix --name jbpython -v $(pwd):/home -it  -p 5000:5000 jbcodeforce/python37 bash 
