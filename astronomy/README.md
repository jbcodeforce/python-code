# Astronomy code study

See [the note on deep dive theory]()

## How to run those code?

```shell
# build the docker image for the python env
docker build -t jbcodeforce/astronomy .
# run it with mounted folder to home
docker run -ti -v $(pwd):/home jbcodeforce/astronomy bash
```