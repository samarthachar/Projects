CREATE TABLE Coupons (
  id varchar(255) PRIMARY KEY,
  coupon_status coupon_status NOT NULL,
  description varchar(255) NULL,
  expiry_date DATE,
  start_date DATE,
  stackable BOOL, 
  coupon_type coupon_type,
  coupon_scope coupon_scope, 
  caps VARCHAR(255),
  coupon_name VARCHAR(255),

  created_at date,
  modified_at date,
  created_by VARCHAR(255),
  modified_by VARCHAR(255)
);

CREATE TABLE Vouchers (
  id varchar(255) PRIMARY KEY,
  voucher_code varchar(255),
  voucher_status voucher_status,
  coupon_id VARCHAR(255),
  user_id VARCHAR(255),
  
  created_at date,
  modified_at date,
  created_by VARCHAR(255),
  modified_by VARCHAR(255),
  
  FOREIGN KEY (coupon_id) REFERENCES coupons (id)
  /* FOREIGN KEY (user_id) REFERENCES users (id) */
)
