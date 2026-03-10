from uuid import UUID
from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field # type: ignore 

from app.core.enums import VoucherStatus

class VoucherCreate(BaseModel):

    voucher_code: UUID | None = Field(default=None, max_length=1000)
    voucher_status: VoucherStatus = Field(default="available")

    coupon_id: UUID = Field(max_length=255)
    user_id: UUID | None = Field(max_length=255, default=None)

class VoucherOut(BaseModel):
    id: UUID
    voucher_code: str
    voucher_status: VoucherStatus

    coupon_id: UUID
    user_id: UUID

    created_at: datetime
    modified_at: datetime | None
    created_by: UUID #Change to fk
    modified_by: UUID | None # change to fk

class VoucherUpdate(BaseModel):
    voucher_code: str | None = Field(default=None, max_length=1000)
    voucher_status: VoucherStatus | None = Field(default="available")

    coupon_id: UUID | None = Field(max_length=255)
    user_id: UUID | None = Field(max_length=255, default=None)
