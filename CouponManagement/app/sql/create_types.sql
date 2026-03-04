CREATE TYPE coupon_type AS ENUM ('percentage', 'fixed_amount', 'price_overide');

CREATE TYPE coupon_scope AS ENUM ('item_level', 'order_level');

CREATE TYPE coupon_eligibility AS ENUM ('customer', 'product', 'order_context','geography');

CREATE TYPE coupon_status AS ENUM ('draft', 'active', 'paused', 'expired', 'revoked');

CREATE TYPE voucher_status AS ENUM ('available', 'redeemed');