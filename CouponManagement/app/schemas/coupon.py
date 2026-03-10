from uuid import UUID
import uuid

from datetime import datetime, timedelta, timezone

from pydantic import BaseModel, EmailStr, Field # type: ignore 

from app.core.enums import CouponEligibility, CouponScope, CouponStatus, CouponType

class CouponCreate(BaseModel):
    start_date: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc)
    )
    expiry_date: datetime = Field(
        default_factory=lambda: datetime.now(timezone.utc) + timedelta(days=10)
    )
    stackable: bool = Field(default=False)
    coupon_type: CouponType = Field()
    coupon_scope: CouponScope = Field()
    caps: str = Field(min_length=1, max_length=255)
    coupon_name: str = Field(min_length=1, max_length=255)
    coupon_eligibility : CouponEligibility = Field()


class CouponOut(BaseModel):
    id: UUID 
    coupon_status: CouponStatus 
    description: str | None

    expiry_date: datetime  
    start_date: datetime 
    stackable: bool 
    coupon_type: CouponType 
    coupon_scope: CouponScope
    caps: str | None
    coupon_name: str 

    created_at: datetime
    modified_at: datetime | None
    created_by: UUID 
    modified_by : UUID | None

class CouponUpdate(BaseModel):
    coupon_status: CouponStatus | None = Field(default=None)
    coupon_type: CouponType | None = Field(default=None)
    coupon_scope: CouponScope | None = Field(default=None)
    
    description: str | None = Field(default=None, max_length=1000)
    expiry_date: datetime | None = Field(default=None)
    start_date: datetime | None = Field(default=None)
    stackable: bool | None = Field(default=False)
    
    caps: str | None = Field(default=None)
    coupon_name: str | None = Field(default=None)