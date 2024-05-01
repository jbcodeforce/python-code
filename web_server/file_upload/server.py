from fastapi import FastAPI, UploadFile, File, Depends
from pypdf import PdfReader 
from pydantic import BaseModel
from typing import Optional
import uvicorn

app = FastAPI()
class FileDescription(BaseModel):
    name: Optional[str] = ''
    description: Optional[str] = ''
    type: str= "md"
    file_name: Optional[str] = ''


@app.post("/upload")
async def upload_file(fd: FileDescription = Depends(), aFile: UploadFile = File(...)):
    print(fd)
    contents =  await aFile.read()
    f = open("./file.pdf", "wb")
    f.write(contents)
    f.close()
    reader =  PdfReader("./file.pdf")
    txt = ""
    for page in range(len(reader.pages)): 
        pageObj = reader.pages[page]
        txt+= pageObj.extract_text(extraction_mode="layout")
    rettxt=txt.encode("utf-8")
    return rettxt



if __name__ == "__main__":
     uvicorn.run(app, host="0.0.0.0", port=8000)