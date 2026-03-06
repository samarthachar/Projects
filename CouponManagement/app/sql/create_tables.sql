CREATE TABLE Coupons (
  id varchar(255) PRIMARY KEY,
  coupon_status coupon_status NOT NULL,
  description varchar(255) NULL,
  expiry_date TIMESTAMPZ NOT NULL,
  start_date TIMESTAMPZ NOT NULL,
  stackable BOOL NOT NULL, 
  coupon_type coupon_type NOT NULL,
  coupon_scope coupon_scope NOT NULL, 
  caps VARCHAR(255) NULL,
  coupon_name VARCHAR(255) NOT NULL,
  coupon_eligibility coupon_eligibility NOT NULL,

  created_at TIMESTAMPZ NOT NULL,
  modified_at TIMESTAMPZ NULL,
  created_by VARCHAR(255) NOT NULL,
  modified_by VARCHAR(255) NULL
);

CREATE TABLE Vouchers (
  id varchar(255) PRIMARY KEY,
  voucher_code varchar(255) NOT NULL,
  voucher_status voucher_status NOT NULL,
  coupon_id VARCHAR(255) NOT NULL,
  user_id VARCHAR(255)  NULL,

  
  created_at TIMESTAMPZ NOT NULL,
  modified_at TIMESTAMPZ NULL,
  created_by VARCHAR(255) NOT NULL,
  modified_by VARCHAR(255) NULL,
  
  FOREIGN KEY (coupon_id) REFERENCES coupons (id)
  /* FOREIGN KEY (user_id) REFERENCES users (id) */
)
