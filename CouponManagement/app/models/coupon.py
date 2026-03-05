from datetime import datetime, timezone, timedelta
from app.core.enums import CouponScope, CouponEligibility, CouponStatus, CouponType
from enum import Enum
from sqlalchemy import Column, String, Boolean, DateTime # type: ignore

from app.db.base import Base



class Coupon(Base):
    __tablename__ = "coupons"

    id = Column(String(255), primary_key=True, index=True)
    coupon_status = Column(Enum(CouponStatus, name="coupon_status"), nullable=False)
    description = Column(String(255), nullable=True)

    expiry_date = Column(DateTime(timezone=True), default=(datetime.now(timezone.utc)+ timedelta(days=10)), nullable=False)
    start_date = Column(DateTime(timezone=True), default=(datetime.now(timezone.utc)), nullable=False)
    stackable = Column(Boolean, default=False, nullable=False)
    coupon_type = Column(Enum(CouponType, name="coupon_type"), nullable=False)
    coupon_scope = Column(Enum(CouponScope, name="coupon_scope"), nullable=False)
    caps = Column(String(255), nullable=True)
    coupon_name = Column(String(255), nullable=False)
    coupon_eligibility = Column(Enum(CouponEligibility, name="coupon_eligibility"), nullable=False)

    created_at = Column(DateTime(timezone=True), default=(datetime.now(timezone.utc)), nulllable=False)
    modified_at = Column(DateTime(timezone=True))
    created_by = Column(String, nullable=False) # Developer Note: Change this to a FK
    modified_by = Column(String, nullable=True)

