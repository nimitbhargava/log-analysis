# Logs Analysis Project
### A reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database.

## Requirements
* Python 3+
* psycopg2
* Postgresql 9.6

## How to run

1. Load the data onto the database `psql -d news -f newsdata.sql`
2. Connect to the database `psql -d news`
3. Create Views
4. Run Log Analysis python program `python3 log-analysis.py`

### Create Views

View to get total views by date
```sql
create view total_views as select date(time), count(*) as views from log group by date(time);
```
View to get error views by date
```sql
create view error_views as select date(time), count(*) as errors from log where status='404 NOT FOUND' group by date(time);
```
