# Logs Analysis Project
### Questions
1. What are the most popular three articles of all time?
  Which articles have been accessed the most?
  Present this information as a sorted list with the most popular article at the top
2. Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.
3. On which days did more than 1% of requests lead to errors?
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

## Requirements
* Python 3+
* psycopg2
* Postgresql 9.6

## How to run

* load the data onto the database
```sql
psql -d news -f newsdata.sql
```
* connect to the database
```sql
psql -d news
```
* Create Views
* `python3 log-analysis.py`

### Create Views

```sql
create view total_views as select date(time), count(*) as views from log group by date(time);
```

```sql
create view error_views as select date(time), count(*) as errors from log where status='404 NOT FOUND' group by date(time);
```
