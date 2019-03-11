#!/bin/bash
echo "##########################################################"
echo " docker image for python jupyter notebook development "
echo
docker run -v $(pwd):/home -ti -p 8888:8888 continuumio/miniconda /bin/bash -c "/opt/conda/bin/conda install jupyter -y --quiet && mkdir /opt/notebooks && /opt/conda/bin/jupyter notebook --notebook-dir=/opt/notebooks --ip='*' --port=8888 --no-browser"