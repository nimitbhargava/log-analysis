#!/usr/bin/env python3
#
# A reporting tool that prints out reports (in plain text) based on the data
# in the database. This reporting tool is a Python program using the psycopg2
# module to connect to the database.

import psycopg2


def main():
    '''Reporting tool that prints out reports (in plain text)'''
    DBNAME = 'news'

    db = psycopg2.connect(database = DBNAME)
  
    
if __name__ == '__main__':
    main()
    