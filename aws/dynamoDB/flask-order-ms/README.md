# Order management microservice

This Flask Restful app exposes the following API
| VERB | Description |
| --- | --- |
| GET /orders | get all orders from the backend |
| GET /orders:id | get order giving its ID |
| POST /orders | create a new order |
| PUT /orders:id | update an exiting order giving its ID |

This app uses [Blueprint](https://realpython.com/flask-blueprint/) to organize the code, [Prometheus client](https://github.com/prometheus/client_python) to expose metrics API and instruments routes to expose metrics, and Swagger to expose API doc .

## Run in development mode


```shell
docker run --rm  --name pythonapp -v $(pwd):/app -it  -p 5000:5000 jbcodeforce/python bash 
pipenv shell
pipenv lock
pipenv install --dev
```
Then use python shell: `python app.py` and point to http://localhost:5000 to get the API

### Test the following APIS

```shell
curl localhost:5000/health
curl localhost:5000/metrics
curl localhost:5000/api/v1/orders
```

## The Order resource


```sh
curl localhost:5000/api/v1/orders
```

## Dockerize

And push it to ECR.

```shell
docker build -t 403993201276.dkr.ecr.us-west-2.amazonaws.com/jbcodeforce/flask-orderms .

docker run -p 5000:5000 403993201276.dkr.ecr.us-west-2.amazonaws.com/jbcodeforce/flask-orderms
docker push 403993201276.dkr.ecr.us-west-2.amazonaws.com/jbcodeforce/flask-orderms
# If authentication token expire 
```

## Deploy with Fargate

## Read more

* [Flasgger to get API doc from code](https://github.com/flasgger/flasgger)
* [Flask Blueprints](https://flask.palletsprojects.com/en/2.2.x/blueprints/)
