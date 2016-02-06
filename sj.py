#!/usr/bin/python3
"""

"""

"""
File: sj.py
Author: Murima
Github: https://github.com/yourname
Description: super Jump to any directory in the filesystem without a full or relative path
"""

import sys
import os



from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData
from sqlalchemy.orm import mapper,sessionmaker


class FileSystem(object):

    """mapped class to the database"""

    def __init__(self, added_path):
        """initialize the path and file

        :path: TODO
        :file: TODO

        """
        self.path = added_path

    #d = os.path.expanduser('~')
        #self.file = file

    def __repr__(self):
        return "[FileSystem {}]".format(self.path)

def populate_database():
    """
    Populate the database with the files and
    paths
    """
engine=create_engine("sqlite:///sql_filesystem.db")
#engine.raw_connection().connection.text_factory = str
#create metadata
metadata=MetaData()

file_systemtable=Table('filesystem',metadata
        ,Column('id',Integer,primary_key=True)\
                ,Column ('path',String(500))\
                ,Column ('file',String(250))\
                )
#creates database from the data stored in metadata
metadata.create_all(engine)
#maps the class to the database
mapper(FileSystem,file_systemtable)

#create a session using sessionmaker
Session=sessionmaker(bind=engine, autoflush=True)
session=Session()
base_path=os.path.expanduser('~')
for dirpath, dirnames, filnames in os.walk(unicode(base_path)):

    #fullpath=os.path.join(dirpath)
 #get record from filesystem class return statement
        record=FileSystem(dirpath)
 #add the record object to the database
        session.add(record)
 #commit the changes to close the database
session.commit()

#for record in session.query(FileSystem):
#        print (record.file)
#print(session.query(FileSystem).filter_by(file=\
        #       "Learning Parseltongue- Wizardry in Python.mp4").first())


    #d = os.path.expanduser('~')


#create the database
def find_name(path_name):
    ''' list all paths and sub-directories from home'''
    #tree = []
    #new_path = ''
    print(session.query(FileSystem).filter_by(path=path_name).first())
    print("hello")

def change_dir(path):
    ''' prints the path of the directory found in tree and changes to the DIR'''
    print(path)

if __name__ == '__main__':
    #d = os.path.expanduser('~')
    #self.populate_database()
    find_path=sys.argv[1]
    find_name(find_path)
