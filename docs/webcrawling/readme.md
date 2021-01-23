# Web crawling examples

## Requests


[Requests](https://requests.readthedocs.io/en/master/) is one modern library to do http calls. 

The Response object includes return code and text or can be transform using json() method.

## Using python multiple threading for assessing the most popular image on imgur.com

This is the implementation from [this article from MARCUS MCCURDY](https://www.toptal.com/python/beginners-guide-to-concurrency-and-parallelism-in-python)

The app was registered in imgur using [this link](https://api.imgur.com/oauth2/addclient). The client id is set in environment variable:

```shell
IMGUR_CLIENT_ID 85b0a015a03ea5798f2572bd6c47b6bd935ec090a10b7d4c1a31378
```

The code is under `web_data/imgur` folder. The module `single.py` is loading one image at a time. `DownloadWorker.py` implements a class which uses `Thread` to run the download in parallel. 


The script creates 8 threads and a queue to get the links from where to download the image.
The run method has been overridden, which runs an infinite loop. On every iteration, it calls `self.queue.get()` to try and fetch a URL to from a thread-safe queue. It blocks until there is an item in the queue for the worker to process. 

Once the worker receives an item from the queue, it then calls the same `download_link()` function, when the download is finished, the worker signals the queue that the task is done. This is very important, because the Queue keeps track of how many tasks were enqueued. The call to `queue.join()` would block the main thread forever if the workers did not signal that they completed a task.
