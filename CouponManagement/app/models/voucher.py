from datetime import datetime, timezone
from enum import Enum 

from sqlalchemy import Column, String, DateTime, ForeignKey # type:ignore

from app.db.base import Base
from app.core.enums import VoucherStatus



class Voucher(Base):
    __tablename__ = "vouchers"

    id = Column(String(255), primary_key=True, index=True)
    voucher_code = Column(String(255), nullable=False)
    voucher_status = Column(Enum(VoucherStatus, name="voucher_status"), nullable=False)

    coupon_id = Column(String(255), ForeignKey("coupons.id"), nullable=False)
    user_id = Column(String, nullable=False) # Developer Note: Change to something similar to: Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), default=(datetime.now(timezone.utc)), nulllable=False)
    modified_at = Column(DateTime(timezone=True))
    created_by = Column(String, nullable=False) # Developer Note: Change this to a FK
    modified_by = Column(String, nullable=True)