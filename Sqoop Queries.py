# All the scripts are written in command line

# Import table from MYSQL to SQOOP - this was written in web shell(putty from edureka)
# using a cloud based MYSQL location

sqoop import --connect jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal/linkinba
rb10edu --driver 'com.mysql.jdbc.Driver' --username linkinbarb10edu --password MaroonEagle68@ --table CUSTOMERS -m 1 --ta
rget-dir 'sqoop_sql5';

# Import table from MYSQL to SQOOP with filter
sqoop import --connect jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal/linkinba
rb10edu --driver 'com.mysql.jdbc.Driver' --username linkinbarb10edu --password MaroonEagle68@ --table CUSTOMERS -m 1 --ta
rget-dir 'sqoop_sql5';

# Export table from SQOOP to MYSQL
sqoop export /
--connect jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal/linkinbarb10edu/
--driver 'com.mysql.jdbc.Driver'/
--username linkinbarb10edu/
--password MaroonEagle68@/
--table CUSTOMERS/
- m 1/
--export-dir '/user/linkinbarb10edu/sqoop_sql2'/
;


# SQOOP command to list databases
sqoop export \
--connect jdbc:mysql://ip-10-1-1-204.ap - south - 1.compute.internal / linkinbarb10edu \
- -driver 'com.mysql.jdbc.Driver' \
- -username linkinbarb10edu \
- -password MaroonEagle68@ \
--table CUSTOMERS
--m 1\
--export-dir '/user/linkinbarb10edu/sqoop_sql2';

# SQOOP command to tables
sqoop list-tables --connect jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal/lin
kinbarb10edu --driver 'com.mysql.jdbc.Driver' --username linkinbarb10edu --password MaroonEagle68@

# SQOOP command to list databases
sqoop list-databases --connect jdbc:mysql://ip-10-1-1-204.ap-south-1.compute.internal/lin
kinbarb10edu --driver 'com.mysql.jdbc.Driver' --username linkinbarb10edu --password MaroonEagle68@