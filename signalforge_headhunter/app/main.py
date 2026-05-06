from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.api.routes import router
from app.core.db import Base, engine

app = FastAPI(title="SignalForge Headhunter")
app.include_router(router, prefix="/api")
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")


@app.on_event("startup")
def startup():
    Base.metadata.create_all(bind=engine)


@app.get("/", response_class=HTMLResponse)
def ui(request: Request):
    screens = [
        "Dashboard", "Companies", "Roles", "People", "Outreach Generator",
        "Resume Matcher", "Interaction Tracker", "Export Center"
    ]
    return templates.TemplateResponse("index.html", {"request": request, "screens": screens})
