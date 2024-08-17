CREATE KEYSPACE spark_db WITH replication = {'class': 'SimpleStrategy', 'replication_factor': 1};
USE spark_db;
CREATE TABLE users(Login_id text PRIMARY KEY, user_name text, last_login timestamp);

INSERT INTO users (Login_id, user_name, last_login) VALUES('100001', 'Ali', '2024-02-05 10:05:00');
INSERT INTO users (Login_id, user_name, last_login) VALUES('100009', 'Sara', '2024-03-07 11:03:00');
INSERT INTO users (Login_id, user_name, last_login) VALUES('100087', 'Ziba', '2024-06-12 09:43:00');

INSERT INTO users (Login_id, user_name, last_login) VALUES('100091', 'Mohammad', '2024-06-12 09:43:00');
INSERT INTO users (Login_id, user_name, last_login) VALUES('100196', 'Mahour', '2024-07-27 15:43:00');