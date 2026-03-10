from uuid import UUID 


from sqlalchemy.orm import Session #type: ignore

from app.models.coupon import Coupon
from app.schemas.coupon import CouponUpdate, CouponCreate

def create(db: Session, *, obj_in: CouponCreate) -> Coupon:
    db_obj = Coupon(**obj_in.model_dump())
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get(db: Session, coupon_id: UUID) -> Coupon | None:
    return db.query(Coupon).filter(Coupon.id == coupon_id).first()

def update(db: Session, db_obj: Coupon, obj_in: CouponUpdate) -> Coupon:
    update_data = obj_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def revoke(db: Session, db_obj: Coupon):
    db_obj.coupon_status = "revoked"
    return


def delete(db: Session, coupon: Coupon):
    db.delete(coupon)
    db.commit()
    return

def list(db: Session, *, skip: int = 0, limit: int = 20) -> list[Coupon]: # type: ignore
    return db.query(Coupon).offset(skip).limit(limit).all()