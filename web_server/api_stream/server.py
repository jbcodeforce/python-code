from fastapi import FastAPI
from typing import Generator
from fastapi.responses import StreamingResponse

app = FastAPI()

# coroutine which will suspend the execution if there is await or yield
# yield creates an asynchronous generator, which we iterate over with async for.
async def fake_video_streamer():
    for i in range(10):
        yield b"some fake video bytes"

# another example
# A simple method to open the file and get the data
async def get_data_from_file(file_path: str) -> Generator:
    with open(file=file_path, mode="rb") as file_like:
        yield file_like.read()

@app.get("/")
async def main():
    return StreamingResponse(content=fake_video_streamer(),media_type="text/media")