#!/bin/bash
echo "##########################################################"
echo " docker image for python development "
echo
# docker run -e DISPLAY=192.168.1.89:0 --name jbcodeforcepython -v $(pwd):/home/jbcodefoce/work -it --rm -p 8888:8888 jbcodeforce/python3 /bin/bash 
docker run -i -t -p 8888:8888 continuumio/miniconda /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser"