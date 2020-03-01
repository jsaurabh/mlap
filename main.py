from fastapi import FastAPI, Form, Body
from starlette.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory='templates')

@app.route("/")
def home(request):
    context = {"request": request}
    return templates.TemplateResponse("index.html", context)

@app.get("/input/")
def read_input(search: str):
    return search