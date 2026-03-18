from fastapi import FastAPI # type: ignore

from app.api.routes import coupons # type : ignore
from app.api.routes import vouchers # type : ignore

app = FastAPI(title="Coupons API", version="0.1.0")


app.include_router(coupons.router)
app.include_router(vouchers.router)