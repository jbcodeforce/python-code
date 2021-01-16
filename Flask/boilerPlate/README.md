# Personal Boilerplate for Flask app

This app uses [Blueprint](https://realpython.com/flask-blueprint/) to organize the code. It uses [Prometheus client](https://github.com/prometheus/client_python) to expose metrics API and instruments routes to expose metrics.

## Run in development mode

```shell
docker run --rm  --name pythonapp -v $(pwd):/app -it  -p 5000:5000 jbcodeforce/python37 bash 
# Define the dependencies
pipenv lock -r >requirements.txt
# Install those dependencies
pip install -r requirements.txt
```

Then use python shell: `python app.py`

### Test the following APIS

```shell
curl localhost:5000/health
curl localhost:5000/greetings
curl  localhost:5000/metrics
```

## Dockerize

```shell
docker build -t jbcodeforce/pythonapp .
docker run --name firstApp --rm -p 5001:5000 jbcodeforce/pythonapp
docker push jbcodeforce/pythonapp
```

## Deploy on OpenShift

Use the k8s files.