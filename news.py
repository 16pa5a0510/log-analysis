#!/usr/bin/env python3
import psycopg2


query_1_titlename = ("What are the most popular three articles of all time?")
query_1 = (
    "select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")


query_2_titlename = ("Who are the most popular article authors of all time?")
query_2 = (
    "select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")

query_3_titlename = ("On which days did more than 1% of requests lead to errors?")
query_3 = (
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


def connect(database_name="news"):
    """Connect to the PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable to connect to the database")


def get_query_result(query):
    """Return query results for given query """
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_query(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print ( index+1, results[0],str(results[1]), "views")

#!/usr/bin/env python3
import psycopg2


query_1_titlename = ("What are the most popular three articles of all time?")
query_1 = (
    "select articles.title, count(*) as views "
    "from articles inner join log on log.path "
    "like concat('%', articles.slug, '%') "
    "where log.status like '%200%' group by "
    "articles.title, log.path order by views desc limit 3")


query_2_titlename = ("Who are the most popular article authors of all time?")
query_2 = (
    "select authors.name, count(*) as views from articles inner "
    "join authors on articles.author = authors.id inner join log "
    "on log.path like concat('%', articles.slug, '%') where "
    "log.status like '%200%' group "
    "by authors.name order by views desc")

query_3_titlename = ("On which days did more than 1% of requests lead to errors?")
query_3 = (
    "select day, perc from ("
    "select day, round((sum(requests)/(select count(*) from log where "
    "substring(cast(log.time as text), 0, 11) = day) * 100), 2) as "
    "perc from (select substring(cast(log.time as text), 0, 11) as day, "
    "count(*) as requests from log where status like '%404%' group by day)"
    "as log_percentage group by day order by perc desc) as final_query "
    "where perc >= 1")


def connect(database_name="news"):
    """Connect to the PostgreSQL database. Returns a database connection """
    try:
        db = psycopg2.connect("dbname={}".format(database_name))
        cursor = db.cursor()
        return db, cursor
    except:
        print ("Unable connect to the database")


def get_query_results(query):
    """Return query results for given query """
    db, cursor = connect()
    cursor.execute(query)
    return cursor.fetchall()
    db.close()


def print_query(query_results):
    print (query_results[1])
    for index, results in enumerate(query_results[0]):
        print ( index+1, results[0],str(results[1]), "views")


def print_error(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print ( results[0], str(results[1]) + "% errors")


if __name__ == '__main__':

    popular_articles_results = get_query_results(query_1), query_1_titlename
    popular_authors_results = get_query_results(query_2), query_2_titlename
    load_error_days = get_query_results(query_3), query_3_titlename

    print_query(popular_articles_results)
    print_query(popular_authors_results)
    print_error(load_error_days)

def print_error(query_results):
    print (query_results[1])
    for results in query_results[0]:
        print ( results[0], str(results[1]) + "% errors")


if __name__ == '__main__':

    popular_articles_results = get_query_result(query_1), query_1_titlename
    popular_authors_results = get_query_result(query_2), query_2_titlename
    load_error_days = get_query_results(query_3), query_3_titlename

    print_query(popular_articles_results)
    print_query(popular_authors_results)
    print_error(load_error_days)
