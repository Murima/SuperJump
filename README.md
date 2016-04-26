#SuperJump
This script allows linux command line users to change to the desired directory 
without specifying the full path to the directory  

 example: `sj.py -p myDir/`  

would change to the directory even if it's several sub-directories deep. It uses 
ORM functionality in sqlalchemy to map the local database to the class. Creates a local database
sql_filesystem.db and queries for the directory specified in this database.

Options
=======
* -p specify the path you want to jump to
* -r reload the database to get recently added directories

Usage
=======
In order to use this app you have to place it in /usr/local/bin or in a folder thets in your path
then add this to your .bashrc  

  :`function sj(){
  cd "$(sj.py -p $1 $2)" 
  }`


Now you need to populate the database with the file system folders, do this by providing the -r option

  : `sj -r`

your databse is now populated and you can jump to any directory with

  :`sj -p mydir`.

