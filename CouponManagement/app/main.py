from fastapi import FastAPI # type: ignore

from app.api.routes.v1.coupons import router as coupons_router 
from app.api.routes.v1.vouchers import router as vouchers_router 

app = FastAPI(title="Coupons API", version="0.1.0")


app.include_router(coupons_router)
app.include_router(vouchers_router)