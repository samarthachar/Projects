from enum import Enum

class CouponType(Enum):
    percentage = "percentage"
    fixed_amount = "fixed_amount"
    price_overide = "price_overide"

class CouponScope(Enum):
    item_level = "item_level"
    order_level = "order_level"

class CouponEligibility(Enum):
    customer = "customer"
    product = "product"
    order_context = "order_context"
    geography = "geography"

class CouponStatus(Enum):
    draft = "draft"
    active = "active"
    paused = "paused"
    expired = "expired"
    revoked = "revoked"

class VoucherStatus(Enum):
    available = "available"
    redeemed = "redeemed"

