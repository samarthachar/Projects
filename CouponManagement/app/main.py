from fastapi import FastAPI # type: ignore

from app.db.base import Base
from app.db.session import engine

app = FastAPI(title="Test API", version="0.1.0")


