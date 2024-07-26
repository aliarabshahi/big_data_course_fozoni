-- Exported from QuickDBD: https://www.quickdatabasediagrams.com/
-- NOTE! If you have used non-SQL datatypes in your design, you will have to change these here.


CREATE TABLE "items" (
    "item_id" int   NOT NULL,
    "item_name" varchar(50)   NOT NULL,
    "item_category" varchar(50)   NOT NULL,
    "item_price" int   NOT NULL,
    CONSTRAINT "pk_items" PRIMARY KEY (
        "item_id"
     )
);

CREATE TABLE "customers" (
    "customer_id" int   NOT NULL,
    "customer_firstname" varchar(50)   NOT NULL,
    "customer_lastname" varchar(50)   NOT NULL,
    "customer_address" varchar(50)   NOT NULL,
    CONSTRAINT "pk_customers" PRIMARY KEY (
        "customer_id"
     )
);

CREATE TABLE "orders" (
    "order_id" int   NOT NULL,
    "customer_id" int   NOT NULL,
    "item_id" int   NOT NULL,
    "items_bought" int   NOT NULL,
    CONSTRAINT "pk_orders" PRIMARY KEY (
        "order_id"
     )
);

ALTER TABLE "orders" ADD CONSTRAINT "fk_orders_customer_id" FOREIGN KEY("customer_id")
REFERENCES "customers" ("customer_id");

ALTER TABLE "orders" ADD CONSTRAINT "fk_orders_item_id" FOREIGN KEY("item_id")
REFERENCES "items" ("item_id");

