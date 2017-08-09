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

    queryOne = """select concat('"',title,'"'), concat(count(*), ' views') as views from log inner join articles
     on concat('/article/', articles.slug) = log.path where status='200 OK' 
     and path like '%article%' group by title order by views desc limit 3;"""
    queryTwo = """select name, concat(count(*), ' views') as views from authors join articles 
     on authors.id = articles.author join log on log.path = 
     concat('/article/', articles.slug) group by name order by views desc;"""
    queryThree = """select to_char(total_views.date, 'Month dd, YYYY'), 
    concat(trunc(100.0*error_views.errors/total_views.views, 1), '% errors') as percent from
    total_views join error_views on total_views.date = error_views.date and 
    (100.0*error_views.errors/total_views.views) > 1;"""
    print("\n\n1. What are the most popular three articles of all time?")
    printQueryResult(db, queryOne)
    print("\n\n2. Who are the most popular article authors of all time?")
    printQueryResult(db, queryTwo)
    print("\n\n3. On which days did more than 1% of requests lead to errors?")
    printQueryResult(db, queryThree)
    db.close()    

def printQueryResult(db, queryOne):
    for(title, value) in fetchAll(db, queryOne):
        print("{} -- {}".format(title, value))


def fetchAll(db, query):
    c = db.cursor()
    c.execute(query)
    return c.fetchall()
    
    
if __name__ == '__main__':
    main()