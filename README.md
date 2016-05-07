#SuperJump
This script allows linux command line users to change to the desired directory 
without specifying the full path to the directory  

 example: `sj.py myDir`  

would change to the directory even if it's several sub-directories deep. It uses 
ORM functionality in sqlalchemy to map the local database to the class. Creates a local database
sql_filesystem.db and queries for the directory specified in this database. To install sqlalchemy
 `pip install sqlalchemy` should do the trick.

Options
=======
* -r reload the database to get recently added directories

Usage
=======
In order to use this app you have to place it in /usr/local/bin or in a folder thets in your path
then add this to your .bashrc  

  :`function sj(){
  output="$( sj.py $1 $2)"
    if [ -d "$output" ]; then
        	cd $output
    else
        	echo $output
    fi


  }`


Now you need to populate the database with the file system folders, do this by providing the -r option
and a base_path this is the root of the tree that will be in your database. If not specified the home
path will be used as default.

  : `sj -r base_path`

your databse is now populated and you can jump to any directory with

  :`sj  mydir`.

