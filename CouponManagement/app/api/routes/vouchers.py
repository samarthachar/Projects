from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, Query # type: ignore
from sqlalchemy.orm import Session # type: ignore
from app.api.deps import get_db
from app.schemas.voucher import VoucherCreate, VoucherOut, VoucherUpdate
from app.crud import voucher as crud_voucher

router = APIRouter(prefix="/vouchers", tags=["vouchers"])

@router.post("", response_model=VoucherOut, status_code=201)
def create_voucher(obj_in: VoucherCreate, db: Session = Depends(get_db)):
    return crud_voucher.create(db, obj_in=obj_in)

@router.get("/{voucher_id}", response_model=VoucherOut)
def get_voucher(voucher_id: UUID, db: Session = Depends(get_db)):
    voucher = crud_voucher.get(db, voucher_id=voucher_id)
    if not voucher:
        raise HTTPException(status_code=404, detail="Voucher not found")
    return voucher

@router.patch("/{voucher_id}", response_model=VoucherOut)
def update_coupon(voucher_id: UUID, voucher_update: VoucherUpdate,db: Session = Depends(get_db)):
    voucher = crud_voucher.get(db, voucher_id=voucher_id)
    if not voucher:
        raise HTTPException(status_code=404, detail="Voucher not found")

    update_data = voucher_update.model_dump(exclude_unset=True)

    for key, value in update_data.items():
        setattr(voucher, key, value)

    db.add(voucher)
    db.commit()
    db.refresh(voucher)
    return voucher

@router.delete("/{voucher_id}", status_code=204)
def delete_voucher(
    voucher_id: UUID,
    db: Session = Depends(get_db),
):
    voucher = crud_voucher.get(db, voucher_id=voucher_id)
    if not voucher:
        raise HTTPException(status_code=404, detail="Voucher not found")

    crud_voucher.delete(db, voucher)
    return

@router.get("")
def list_vouchers(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return crud_voucher.list(db, skip=skip, limit=limit)



