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

    coupon_id = Column(UUID(as_uuid=True), ForeignKey("coupons.id", ondelete="SET NULL"), nullable=True)
    user_id = Column(UUID(as_uuid=True), nullable=True) # Developer Note: Change to something similar to: Column(Integer, ForeignKey("users.id"), nullable=False)

    created_at = Column(DateTime(timezone=True), default=(datetime.now(timezone.utc)), nullable=False)
    modified_at = Column(DateTime(timezone=True))
    created_by = Column(UUID(as_uuid=True), nullable=False,
                        default=uuid.UUID("d1c8e0ae-ea1a-4c38-9714-a6142c4ff819"
                        )
     ) # Developer Note: Change this to a FK, and remove default
    modified_by = Column(String, nullable=True)