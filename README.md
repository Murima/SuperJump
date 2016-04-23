#SuperJump
This script allows linux command line users to change to the desired directory 
without specifying the full path to the directory 
example: `sj.py -p myDir/`
would change to the directory even if it's several sub-directories deep. It uses 
ORM functionality in sqlalchemy to map the local database to the class. Creates a local database
sql_filesystem.db and queries for the directory specified in this database.

Options
=======
-p specify the path you want to jump to
-r reload the database to get recently added directories
