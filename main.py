from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from starlette.templating import Jinja2Templates
from starlette.requests import Request

# FastAPI instance
app = FastAPI()

# Middleware to allow CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from all origins
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)

# Set up templates (to serve HTML files)
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
def get_home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.get("/add/")
def add(a: float, b: float):
    return {"result": a + b}

@app.get("/sub/")
def subtract(a: float, b: float):
    return {"result": a - b}

@app.get("/mul/")
def multiply(a: float, b: float):
    return {"result": a * b}

@app.get("/div/")
def divide(a: float, b: float):
    if b == 0:
        return JSONResponse(status_code=400, content={"error": "Cannot divide by zero"})
    return {"result": a / b}
