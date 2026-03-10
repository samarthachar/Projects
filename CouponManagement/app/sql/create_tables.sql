CREATE TABLE Coupons (
  id UUID PRIMARY KEY,
  coupon_status coupon_status NOT NULL,
  description varchar(255) NULL,
  expiry_date TIMESTAMPTZ NOT NULL,
  start_date TIMESTAMPTZ NOT NULL,
  stackable BOOL NOT NULL, 
  coupon_type coupon_type NOT NULL,
  coupon_scope coupon_scope NOT NULL, 
  caps VARCHAR(255) NULL,
  coupon_name VARCHAR(255) NOT NULL,
  coupon_eligibility coupon_eligibility NOT NULL,

  created_at TIMESTAMPTZ NOT NULL,
  modified_at TIMESTAMPTZ NULL,
  created_by VARCHAR(255) NOT NULL,
  modified_by VARCHAR(255) NULL
);

CREATE TABLE Vouchers (
  id UUID PRIMARY KEY,
  voucher_code varchar(255) NOT NULL,
  voucher_status voucher_status NOT NULL,
  coupon_id UUID NULL,
  user_id UUID  NULL,

  
  created_at TIMESTAMPTZ NOT NULL,
  modified_at TIMESTAMPTZ NULL,
  created_by UUID NOT NULL,
  modified_by UUID NULL,
  
  FOREIGN KEY (coupon_id) REFERENCES coupons (id) ON DELETE SET NULL
  /* FOREIGN KEY (user_id) REFERENCES users (id) */
)
