import uuid

from datetime import datetime, timezone

from sqlalchemy import Column, String, DateTime, ForeignKey, Enum # type:ignore
from sqlalchemy.dialects.postgresql import UUID # type: ignore

from app.db.base import Base
from app.core.enums import VoucherStatus



class Voucher(Base):
    __tablename__ = "vouchers"

    id = Column(UUID(as_uuid=True), primary_key=True, index=True, default=uuid.uuid4)
    voucher_code = Column(String(255), nullable=False)
    voucher_status = Column(Enum(VoucherStatus, name="voucher_status"), nullable=False)

    coupon_id = Column(String(255), ForeignKey("coupons.id"), nullable=False)
    user_id = Column(String, nullable=True) # Developer Note: Change to something similar to: Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), default=(datetime.now(timezone.utc)), nullable=False)
    modified_at = Column(DateTime(timezone=True))
    created_by = Column(String, nullable=False) # Developer Note: Change this to a FK
    modified_by = Column(String, nullable=True)