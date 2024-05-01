# FastAPI

[FastAPI](https://fastapi.tiangolo.com/) helps to build backend REST api in python.

## Boilerplate

```python

```

## Running

To start an app, use uvicorn in a shell script

```sh
uvicorn orchestrator_api:app --host 0.0.0.0 --port 8000 --reload
```

Or add this in the main server python code:

```python
import uvicorn

if __name__ == "__main__":
     uvicorn.run(app, host="0.0.0.0", port=8000)
```


* Some URLs

```sh
http://127.0.0.1:8000/docs
http://127.0.0.1:8000/redoc
```


## How tos

* [A server with a websocket listener](https://github.com/jbcodeforce/python-code/tree/master/web_server/websocket_server)
* [Test to upload file and pydantic object in the same URL](https://github.com/jbcodeforce/python-code/tree/master/web_server/file_upload)
* [Expose async function to stream content with a generator](https://github.com/jbcodeforce/python-code/tree/master/web_server/api_stream). It uses yield and asyncio


## Some content to read

* [See full tutorial](https://fastapi.tiangolo.com/tutorial/)

