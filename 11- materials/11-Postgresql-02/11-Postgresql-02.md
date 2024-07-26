# 0- SQL in PostgreSQL

![[]()](.\files\0.jpg)

🛑 To see this course [**CLICK HERE**](https://youtu.be/lTFQ6EGPk0w?si=9zOogvuGm4FvbEVi).

# 1- Designing a database in PostgreSQL

In this session, we are going to use of [Quick Database Diagram](https://www.quickdatabasediagrams.com/) to create and design a database in PostgreSQL. 

Someone come to our office and ask for creating a database for his ecommerce business. 

**Let's assume that our client wants data for `items` on the following data classes:**

- Item name
- Item category
- Item price

**For `customers`, he wants data on the following:**

- The first name of the customer
- The last name of the customer
- The details about the item that was bought
- The address of the customer

**For `orders`, he wants data on the following:**

- The details on all of the items that were bought
- The details about the customer that bought the item
- The quantity of the items that were bought

To design the database and the tables, we need to specify all the fields needed for each table. Then we will do data normalization and define table relationships. Normalizing data is the process of organizing data to reduce redundancy and make it more flexible and efficient.

#### items table

```scheme
items
-
item_id int pk
item_name varchar(50)
item_category varchar(50)
item_price int

```

#### customer table

```scheme
customers
-
customer_id int pk
customer_firstname varchar(50)
customer_lastname varchar(50)
customer_address varchar(50)
```

#### orders table

```scheme
orders
-
order_id int pk
customer_firstname varchar(50)
customer_lastname varchar(50)
item_name varchar(50)
item_category varchar(50)
item_price int
items_bought int
customer_address varchar(100)
```



At this point we should have this view of our tables.



![](.\files\1.png)



Looking at the three tables we designed, you will realize that the `orders table` has fields similar to the `items table` and `customers table`. This is where we can use 🛑**normalization**🛑 by breaking a larger table, like `orders table`, into smaller tables and defining the relationships between the tables. This will enable us to eliminate repetitive data fields and ensure data is stored logically.

#### Change the order table

```
orders
-
order_id int pk
customer_firstname varchar(50)
customer_lastname varchar(50)
item_id int FK >- items.item_id 
items_bought int
customer_address varchar(100)
```

Now we should see this



![](.\files\2.png)



#### Second change the order table

```
orders
-
order_id int pk
customer_id int FK >- customers.customer_id 
item_id int FK >- items.item_id 
items_bought int
```

So we have this view now



![](.\files\3.png)



And finally the magic will happen

 ![](.\files\4.png)



This export operation give us this SQL code

```sql
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
```

**Now go to DBeaver and make your database and tables.**



# 2- Order of columns in PostgreSQL is important

🛑 PostgreSQL stores data in a row-oriented manner, meaning each row occupies contiguous storage space regardless of column order.

### Benefits of Column Ordering

1. Reduced table size
2. Less time consuming operations (ALTER, VACUUM etc.)

------



```sql
CREATE TABLE user_order_default (
  is_shipped    BOOLEAN NOT NULL DEFAULT false, #BOOLEAN is 2 Bytes
  user_id       BIGINT NOT NULL,				#BIGINT is 8 Bytes
  order_total   NUMERIC NOT NULL,
  order_dt      TIMESTAMPTZ NOT NULL,
  order_type    SMALLINT NOT NULL,
  ship_dt       TIMESTAMPTZ,
  item_ct       INT NOT NULL,
  ship_cost     NUMERIC,
  receive_dt    TIMESTAMPTZ,
  tracking_cd   TEXT,
  id            BIGSERIAL PRIMARY KEY NOT NULL
);
###########################################################################

CREATE TABLE user_order_tweaked (
  id            BIGSERIAL PRIMARY KEY NOT NULL,
  user_id       BIGINT NOT NULL,
  order_dt      TIMESTAMPTZ NOT NULL,
  ship_dt       TIMESTAMPTZ,
  receive_dt    TIMESTAMPTZ,
  item_ct       INT NOT NULL,
  order_type    SMALLINT NOT NULL,
  is_shipped    BOOLEAN NOT NULL DEFAULT false,
  order_total   NUMERIC NOT NULL,
  ship_cost     NUMERIC,
  tracking_cd   TEXT
);

-- VARCHAR comes from "variable-length character"
```

### Populate table with record

```sql
INSERT INTO user_order_default (
    is_shipped, user_id, order_total, order_dt, order_type,
    ship_dt, item_ct, ship_cost, receive_dt, tracking_cd
)
SELECT true, 1000, 500.00, now() - INTERVAL '7 days',
       3, now() - INTERVAL '5 days', 10, 4.99,
       now() - INTERVAL '3 days', 'X5901324123479RROIENSTBKCV4'
  FROM generate_series(1, 1000000);
```



```sql
INSERT INTO user_order_tweaked (
    is_shipped, user_id, order_total, order_dt, order_type,
    ship_dt, item_ct, ship_cost, receive_dt, tracking_cd
)
SELECT true, 1000, 500.00, now() - INTERVAL '7 days',
       3, now() - INTERVAL '5 days', 10, 4.99,
       now() - INTERVAL '3 days', 'X5901324123479RROIENSTBKCV4'
  FROM generate_series(1, 1000000);
```

### check table size

```sql
SELECT pg_relation_size('user_order_default') AS size_bytes,
       pg_size_pretty(pg_relation_size('user_order_default')) AS size_pretty;

SELECT pg_relation_size('user_order_tweaked') AS size_bytes,
       pg_size_pretty(pg_relation_size('user_order_tweaked')) AS size_pretty;
```

🛑 The table created with careful consideration of column ordering exhibited a smaller footprint compared to its counterpart. This reduction in size not only translates to more efficient storage utilization but also extends to associated indexes, **potentially leading to faster query execution times and improved overall system performance**.



# 3- Partitioning and Sharding 

**When our tables are getting big enough, we should handle this. Because the response time reduce dramatically. Here we mention some solutions. Note that `Sharding` is the last solution, not the first one!**

##### 1- partition a table in our database (horizontal) 



![](.\files\5.png)



##### 2- Vertical partitioning

🛑 we can send the part that is not queried most to a HDD storage.  



![](.\files\6.webp)



##### 3- Master slave architecture



![](.\files\7.png)



##### 4- Using of Redis as a Cash manager  



![](.\files\8.png)





##### 5- Database Sharding 



![](.\files\9.png)



🛑 YouTube is using MySQL and shard this database. When we shard a database we can not use of ACID property anymore. 