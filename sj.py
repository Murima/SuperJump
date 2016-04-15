#!/usr/bin/python3
"""
File: sj.py
Author: Murima
Github: https://github.com/murima
Description: super Jump to any directory in the filesystem without a full or relative path
"""

import sys
import os



from sqlalchemy import create_engine
from sqlalchemy import Table,Column,Integer,String,MetaData
from sqlalchemy.orm import mapper,sessionmaker
from sqlalchemy.ext.declarative import declarative_base


Base = declarative_base()

class FileSystem(Base):
    """
    class to store the paths of the directories
    """
    __tablename__ = 'filesystem'
    id = Column(Integer,primary_key=True)
    path = Column (String(500))

    def __repr__(self):
        return "<FileSystem {}, {}]".format(self.path)



    def populate_database():
            """
    Populate the database with the files and
    paths
    """
    base_path=os.path.expanduser('~')
    for dirpath, dirnames, filnames in os.walk(unicode(base_path)):

        record=FileSystem(dirpath)
        #add the record object to the database
        session.add(record)
                    #commit the changes to close the database
    session.commit()


#create the database
    def find_name(path_name, session):
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
    
    engine=create_engine("sqlite:///sql_filesystem.db")
    Session=sessionmaker(bind=engine, autoflush=True)
    session=Session()

    find_path=sys.argv[1]
    session_find= Session()
    A
    find_name(find_path, session_find)
