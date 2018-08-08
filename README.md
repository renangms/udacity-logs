# udacity-logs
Source code for Log Analysis Project

## Views created

```
create view article_request as select title, slug, log.time from articles, log where log.path like CONCAT('/article/', articles.slug) and status = '200 OK';
```

```
create view author_article as select authors.name, articles.slug from authors, articles where authors.id = articles.author order by authors.name;
```

```
create view requests_per_day as select DATE(time) as date, count(*) from log group by date;
```

```
create view errors_per_day as select DATE(time) as date, count(*) from log where status = '404 NOT FOUND' group by date;
```

### How to run
```
python log.py
```