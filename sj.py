#!/usr/bin/python3
#super jump to any directory in the filesystem without a full given path

import sys
import os



from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData
from sqlalchemy.orm import mapper,sessionmaker
import os


class FileSystem(object):

    """mapped class to the database"""

    def __init__(self,path,file):
        """initialize the path and file

        :path: TODO
        :file: TODO

        """
        self.path = path
        self.file = file

    def __repr__(self):
        return "[FileSystem {}, {}]".format(self.path,self.file)


path ="/home/killer/games/Gilu/"

#create the database
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
def populate_database():
    """
    Populate the database with the files and
    paths
    """
    for dirpath,dirnames,filnames in os.walk(unicode(path)):
        for file in filnames:
            fullpath=os.path.join(dirpath,file)
     #get record from filesystem class return statement
            record=FileSystem(fullpath,file)
     #add the record object to the database
            session.add(record)
     #commit the changes to close the database
    session.commit()

#for record in session.query(FileSystem):
#        print (record.file)
print(session.query(FileSystem).filter_by(file=\
"Learning Parseltongue- Wizardry in Python.mp4").first())

def find_name(d, name):
    ''' list all paths and sub-directories from home'''
    tree = []
    new_path = ''
    for path, sub, files in os.walk(d, name):
        if name in path:
            tree.append(path[0:])

            try:
                new_path = tree[0]
            except IndexError:
                print('path not found')
                new_path = tree.append(d)
    change_dir(new_path)

def change_dir(path):
    ''' prints the path of the directory found in tree'''
    print(path)

if __name__ == '__main__':
    d = os.path.expanduser('~')
    find_name(d, sys.argv[1])
