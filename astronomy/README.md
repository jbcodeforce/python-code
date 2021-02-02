# Astronomy code study

See [the note on deep dive theory]()

## How to run those code?

```shell
# In one terminal 
socat TCP-LISTEN:6000,reuseaddr,fork UNIX-CLIENT:\"$DISPLAY\"
# In second terminal start X server
open -a Xquartz
# Get IP address 
ifconfig
# 10.0.0.183 for en0 interface
# build the docker image for the python env
docker build -t jbcodeforce/astronomy .
# run it with mounted folder to home
docker run -ti -e DISPLAY=10.0.0.183:0  -v $(pwd):/home jbcodeforce/astronomy bash
```