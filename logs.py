import psycopg2

DBNAME = "news"


def popular_articles():
    query = """
    select title, count(*) as c from articles, log
    where log.path like concat('%', articles.slug, '%')
    and status = '200 OK'
    group by articles.title order by c desc limit 3"""
    return execute_query(query)


def popular_authors():
    query = """
    select author_article.name, count(*) as c
    from author_article, log
    where log.path like CONCAT('%', author_article.slug)
    and status = '200 OK'
    group by author_article.name order by c desc
    """
    return execute_query(query)


def errors_per_day():
    query = """
    select requests_per_day.date,
    round(errors_per_day.count * 100.0 / requests_per_day.count, 2)
    from requests_per_day, errors_per_day
    where requests_per_day.date = errors_per_day.date
    and (errors_per_day.count * 100.0 / requests_per_day.count) > 1.0;
    """
    return execute_query(query)


def execute_query(query):
    db = psycopg2.connect(database=DBNAME)
    c = db.cursor()
    c.execute(query)
    result = c.fetchall()
    db.close()
    return result


def print_query_result(message, result):
    print(message)
    for r in result:
        print("- " + str(r[0]) + ": " + str(r[1]))
    print("\n")


if __name__ == "__main__":
    print_query_result(
        "3 most popular articles of all time:",
        popular_articles())

    print_query_result(
        "Most popular authors of all time:",
        popular_authors())

    print_query_result(
        "Days with more than 1% of requests lead to errors:",
        errors_per_day())
