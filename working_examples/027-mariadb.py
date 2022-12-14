# ----------------------------------
# This script is used for learning
# Some prereq's should be done
# on the mariadb server ypu have to:
# 1. allow external connections sudo nano /etc/mysql/mariadb.conf.d/50-server.cnf bind-address = 0.0.0.0
# 2. import some testdb, in our example nation.sql
# https://www.mariadbtutorial.com/wp-content/uploads/2019/10/nation.zip
# mysql -uroot -p
# source /tmp/nation.sql
# 3. create user for python server, in our example
# 10.0.3.5 - dbserver
# 10.0.3.8 - python server
# GRANT ALL ON *.* to admin@'10.0.3.8' IDENTIFIED BY 'password';
# FLUSH PRIVILEGES;
# 4. on the python server we have to:
# wget https://downloads.mariadb.com/MariaDB/mariadb_repo_setup
# echo "367a80b01083c34899958cdd62525104a3de6069161d309039e84048d89ee98b  mariadb_repo_setup" | sha256sum -c -
# chmod +x mariadb_repo_setup
# sudo ./mariadb_repo_setup    --mariadb-server-version="mariadb-10.6"
# sudo apt install curl
# sudo ./mariadb_repo_setup    --mariadb-server-version="mariadb-10.6"
# sudo apt install libmariadb3 libmariadb-dev
# pip3 install mariadb
# Created by winadm
# Version 0.1
# Examples
# ...
# ----------------------------------
# Module Imports
import mariadb
import sys

# Connect to MariaDB Platform
# define host and port for mariadb
# define DB to work with
dbhost = "10.0.3.5"
dbport = 3306
dbname = "nation"
try:
    conn = mariadb.connect(
        user="admin",
        password="password",
        host=dbhost,
        port=dbport,
        database=dbname

    )
# write error on db connection try
except mariadb.Error as e:
    print(f"Error connecting to MariaDB Platform: {e}")
    sys.exit(1)

# Get Cursor
cursor = conn.cursor()
# define our query
cursor.execute("""
                select name, area, country_code3
                from countries
    """)
# write cursor fetchall to results variable
results = cursor.fetchall()
# print results in human readable format
for row in results:
    country = row[0]
    area = row[1]
    code3 = row[2]
    print ("Country is: " + country + " with area: " + str(area) + " and code: " + code3)
print("======once more example=========")
#retrieving information
some_contry = "Canada"
cursor.execute("SELECT name, area, country_code3 from countries WHERE name=?", (some_contry,))
for name, area, country_code3 in cursor:
    print(f"Country: {name}, Area: {area}, Code: {country_code3}")
# close mariadb connection
conn.close()


