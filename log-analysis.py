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

    queryOne = """select title, count(*) as views from log inner join articles
     on concat('/article/', articles.slug) = log.path where status='200 OK' 
     and path like '%article%' group by title order by views desc limit 3;"""
    queryTwo = """select name, count(*) as views from authors join articles 
     on authors.id = articles.author join log on log.path = 
     concat('/article/', articles.slug) group by name order by views desc;"""
    queryThree = """select to_char(total_views.date, 'Month dd, YYYY'), 
    trunc(100.0*error_views.errors/total_views.views, 1) as percent from
    total_views join error_views on total_views.date = error_views.date and 
    (100.0*error_views.errors/total_views.views) > 1;"""
    print("\n\n1. What are the most popular three articles of all time?")
    for(title, views) in fetchAll(db, queryOne):
        print("\"{}\" -- {} views".format(title, views))
    print("\n\n2. Who are the most popular article authors of all time?")
    for(title, views) in fetchAll(db, queryTwo):
        print("{} -- {} views".format(title, views))
    print("\n\n3. On which days did more than 1% of requests lead to errors?")
    for(date, errors) in fetchAll(db, queryThree):
        print("{} -- {}% errors".format(date, errors))        
    db.close()    


def fetchAll(db, query):
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    
    
if __name__ == '__main__':
    main()