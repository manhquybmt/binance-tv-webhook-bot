from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from app.dashboard.routes import router as dashboard_router
from app.api.webhook import router as webhook_router

app = FastAPI(title="Binance Trading Platform")

app.mount("/static", StaticFiles(directory="app/static"), name="static")

templates = Jinja2Templates(directory="app/templates")

app.include_router(dashboard_router)
app.include_router(webhook_router)
