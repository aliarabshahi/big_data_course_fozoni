### PostgreSQL is a row-based database

![](.\files\rows-vs-columns.png)



#### Note:

**▶ Row based databases are suitable for `transactional jobs`.** 

**▶ Column based databases are a good solution for `analytical tasks`.**

------

### Install PostgreSQL on Ubuntu

First check if you have already installed PostgreSQL by running this command:

```bash
postgres --version
or 
sudo lsof -i :5432
```

### Go for installation phase

```bash
sudo apt update

sudo apt install postgresql postgresql-contrib

nano ~/.bashrc

export PATH=/usr/lib/postgresql/14/bin:$PATH
```

### Login and create a database

```bash
sudo -u postgres psql
```

```sql
CREATE USER username WITH PASSWORD 'password';

CREATE DATABASE database_name;

GRANT ALL PRIVILEGES ON DATABASE database_name TO username;
```

### Work with airflow.cfg file

`sql_alchemy_conn = postgresql+psycopg2://USER:PASSWORD@localhost:PORT/DATABASE-NAME`

`sql_alchemy_conn = postgresql+psycopg2://airflow:123456@localhost:5432/airflow_db`

### Interact with Postgres from cli

![](.\files\000886.png)

```bash
chmod og+rX /home/amin

You can check again bu running this

chmod og-rX /home/amin 

cat /etc/passwd
```



![](.\files\000892.png)

------

### Install PostgreSQL on Windows

First check if you have already installed PostgreSQL on Windows OS by running this command:

```powershell
netstat -ano | findstr :5432

taskkill /F /PID <pid of task>
```

We have two options for installing Postgres:

1. Download it from [**This Link**](https://www.postgresql.org/download/) and the next is just some clicks ([Your Direct Download Link](https://get.enterprisedb.com/postgresql/postgresql-16.1-1-windows-x64.exe))
2. First, install `choco` from [**This Tutorial**](https://www.liquidweb.com/kb/how-to-install-chocolatey-on-windows/). Then install Postgres just by running your PowerShell in the Admin mode and using the following command: 

```powershell
choco install postgresql16

choco list
```

🛑**We can work with `choco` easily from Iran!**🛑

![](.\files\photo_2024-05-03_17-15-05.jpg)

See [**this page**](https://community.chocolatey.org/packages/postgresql) for more options and flags on installation of PostgreSQL. 

🛑 Note that you should set the path. If you install PostgreSQL by `choco`, it will do this automatically for you.

![](.\files\000891.png)

### Change the generated password

```powershell
psql -U postgres -d <your_database_name>

ALTER USER <username> WITH PASSWORD 'new_password';
```

### Get help in psql 

```sql
\?

\h

\h command

\h DO

\du
# list all users for us

\l
# list all databases for us

\c testdb
# conect us to testdb database

\q
# quit the psql cli

DROP DATABASE <database-name>;
```

------

### Connect to PostgreSQL from DBeaver

![](.\files\000887.png)



🛑One of the best database tool for PostgreSQL is [**pgAdmin**](https://www.pgadmin.org/). But I'm no longer use of it!🛑



------

### We can insert json data into PostgreSQL

```sql
CREATE TABLE json_table (
    id SERIAL PRIMARY KEY,
    json_data JSONB
);

INSERT INTO my_table (json_data) VALUES ('{"name": "John", "age": 30}');

INSERT INTO my_table (json_data) VALUES ('{"name": "John", "age": 30, "new":[1,2,3]}');
```

------

### Now that we have a good setup of PostgreSQL on our device, let's go for some SQL statements. 