from uuid import UUID

from sqlalchemy.orm import Session # type: ignore

from app.models.voucher import Voucher
from app.schemas.voucher import VoucherUpdate, VoucherCreate

def create(db: Session, *, obj_in: VoucherCreate) -> Voucher:
    db_obj = Voucher(**obj_in.model_dump())
    
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj


def get(db: Session, voucher_id: UUID) -> Voucher | None:
    return db.query(Voucher).filter(Voucher.id == voucher_id).first()

def list(db: Session, *, skip: int = 0, limit: int = 20) -> list[Voucher]: # type: ignore
    return db.query(Voucher).offset(skip).limit(limit).all()

def update(db: Session, db_obj: Voucher, obj_in: VoucherUpdate) -> Voucher:
    update_data = obj_in.model_dump(exclude_unset=True)

    for field, value in update_data.items():
        setattr(db_obj, field, value)

    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return db_obj

def mark_redeemed(db: Session, db_obj: Voucher):
    db_obj.voucher_status = "redeemed"
    db.add(db_obj)
    db.commit()
    db.refresh(db_obj)
    return 

def delete(db: Session, voucher: Voucher):
    db.delete(voucher)
    db.commit()
    return
