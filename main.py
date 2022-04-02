from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

# if __name__ == "__main__":
#     import uvicorn
#     uvicorn.run("main:app", host="localhost", reload=True)




"""
Project Key
b0tcl5mr_xQjG1yCADXkJ2mDRWkBoEaCxBNt9LGmi
Project ID
b0tcl5mr
"""