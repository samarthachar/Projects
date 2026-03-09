from fastapi import APIRouter, Depends, HTTPException, Query # type: ignore
from sqlalchemy.orm import Session # type: ignore
from app.api.deps import get_db
from app.schemas.coupon import CouponCreate, CouponOut
from app.crud import coupon as crud_coupon

router = APIRouter(prefix="/coupons", tags=["coupons"])

@router.post("", response_model=CouponOut, status_code=201)
def create_coupon(obj_in: CouponCreate, db: Session = Depends(get_db)):
    return crud_coupon.create(db, obj_in=obj_in)

@router.get("/{coupon_id}", response_model=CouponOut)
def get_coupon(coupon_id: str, db: Session = Depends(get_db)):
    coupon = crud_coupon.get(db, coupon_id=coupon_id)
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")
    return coupon

@router.delete("/{coupon_id}", status_code=204)
def delete_coupon(
    coupon_id: str,
    db: Session = Depends(get_db),
):
    coupon = crud_coupon.get(db, coupon_id=coupon_id)
    if not coupon:
        raise HTTPException(status_code=404, detail="Coupon not found")

    crud_coupon.delete(db, coupon)
    return

@router.get("")
def list_coupons(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1, le=100),
    db: Session = Depends(get_db),
):
    return crud_coupon.list(db, skip=skip, limit=limit)



