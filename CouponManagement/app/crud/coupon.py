from datetime import datetime

from sqlalchemy.orm import Session #type: ignore

from app.models.coupon import Coupon
from app.schemas.coupon import CouponUpdate, CouponCreate, CouponOut
from app.core.enums import CouponEligibility, CouponScope, CouponStatus, CouponType

def create(db: Session,
            *, 
            id: str,
            coupon_status: CouponStatus,
            description: str | None, 
            expiry_date: str, 
            start_date: str,
            stackable: bool,
            coupon_type: CouponType,
            coupon_scope: CouponScope,
            caps: str | None,
            coupon_name: str,
            coupon_eligibility : CouponEligibility,

            created_at: datetime,
            created_by: str,
            modified_at: datetime | None,
            modified_by: str | None

    ) -> Coupon:
    coupon = Coupon(
        id=id,
        coupon_status=coupon_status,
        description=description,
        expiry_date=expiry_date,
        start_date=start_date,
        stackable=stackable,
        coupon_type=coupon_type,
        coupon_scope=coupon_scope,
        caps=caps,
        coupon_name=coupon_name,
        coupon_eligibility=coupon_eligibility,

        created_at=created_at,
        created_by=created_by,
        modified_at=modified_at,
        modified_by=modified_by
    )

    db.add(coupon)
    db.commit()
    db.refresh(coupon)
    return coupon