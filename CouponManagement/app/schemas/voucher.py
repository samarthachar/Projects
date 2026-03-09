from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field # type: ignore 

from app.core.enums import VoucherStatus

class VoucherCreate(BaseModel):

    voucher_code: str | None = Field(default=None, max_length=1000)
    voucher_status: VoucherStatus = Field(default="available")

    coupon_id: str = Field(max_length=255)
    user_id: str | None = Field(max_length=255, default=None)

class VoucherOut(BaseModel):
    id: str
    voucher_code: str
    voucher_status: VoucherStatus

    coupon_id: str
    user_id: str

    created_at = datetime
    modified_at = datetime | None
    created_by = str 
    modified_by = str | None

class VoucherUpdate(BaseModel):
    voucher_code: str | None = Field(default=None, max_length=1000)
    voucher_status: VoucherStatus | None = Field(default="available")

    coupon_id: str | None = Field(max_length=255)
    user_id: str | None = Field(max_length=255, default=None)
