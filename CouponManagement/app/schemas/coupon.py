from typing import Optional
from datetime import datetime

from pydantic import BaseModel, EmailStr, Field # type: ignore 

from app.core.enums import CouponEligibility, CouponScope, CouponStatus, CouponType

class CouponCreate(BaseModel):

    coupon_status: CouponStatus = Field()
    description: Optional[str] = Field(default=None, max_length=1000)
    expiry_date: Optional[str] = Field(default=None)
    start_date: Optional[str] = Field(default=None)
    stackable: bool = Field(default=False)
    coupon_type: CouponType = Field()
    coupon_scope: CouponScope = Field()
    caps: str = Field(min_length=1, max_length=255)
    coupon_name: str = Field(min_length=1, max_length=255)


class CouponOut(BaseModel):
    id: int
    title: str
    description: str | None = None
    is_published: bool

    owner_id: int
    created_at: datetime
    
    class Config:
        from_attributes = True

class CouponUpdate(BaseModel):
    title: str | None = None 
    description: str | None = None
    is_published: bool = False