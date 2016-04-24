#!/usr/bin/python2.7
"""
File: sj.py
Author: Murima
Github: https://github.com/murima
Description: super Jump to any directory in the filesystem without a full or relative path
"""
import os
import argparse
import sys
import re

from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import sessionmaker
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
        return "<FileSystem {}>".format(self.path)



    def populate_database(self, session_populate):
        """
        Populate the database with the files and
        paths
        """

        base_path=os.path.expanduser('~')
        for dirpath, dirnames, filnames in os.walk(base_path):

            record=FileSystem(path=unicode(dirpath, 'utf8'))
            #add the record object to the database
            session_populate.add(record)
                        #commit the changes to close the database
        session_populate.commit()
        print('database repopulated')
        sys.exit()


#create the database
    def find_name(self, path_name, session):
        ''' find the name of the path specified from the local db'''
        #tree = []
        #new_path = ''
        found_path = session.query(FileSystem).filter(FileSystem.path.endswith(path_name)).first()
        if found_path != '[]':
            output = str(found_path)
            cls_name, output = output.split(' ')
            new_path = re.sub('>', '', output)
            print(new_path)


    def change_dir(self, path):
        ''' prints the path of the directory found in tree and changes to the DIR'''
        print(path)

if __name__ == '__main__':
    #d = os.path.expanduser('~')
    parser = argparse.ArgumentParser(description = 'small app that super jumps to any path in any level of the file system')
    parser.add_argument('-r', action='store_true', default=False, dest='populate')
    parser.add_argument('-p', action='store', dest='path')
    arg= parser.parse_args()

    filesys= FileSystem()
    engine=create_engine("sqlite:///sql_filesystem.db")
    Session=sessionmaker(bind=engine, autoflush=True)
    session=Session()
    find_path= arg.path
    if arg.populate == True:
        Base.metadata.create_all(engine)
        filesys.populate_database(session)

    filesys.find_name(find_path, session)
