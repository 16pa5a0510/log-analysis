# log-analysis
 project 3
## Introduction
In this, we have to execute complex queries on a large database to extract intersting stats.
The database in question is a newspaper company database where we have 3 tables; articles, authors and log.

articles - Contains articles posted in the newspaper so far.
authors - Contains list of authors who have published their articles.
log - Stores log of every request sent to the newspaper server.
This project implements a single query solution for each of the question in hand. See main.py for more details.

## working
Make sure you have newsdata.sql, the SQL script file with all the data. It can be downloaded from the Udacity course page.
Then run the following command to execute it in news database. You might have to create the database before-hand.

psql -d news -f newsdata.sql
Finally run the script.
python news.py
It will present you with necessary stats.
