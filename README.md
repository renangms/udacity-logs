# udacity-logs
Source code for Log Analysis Project

## VM setup

### Start VM
```
$ vagrant up
```

### Login
```
$ vagrant ssh
```

## Database setup

### Load data
```
$ psql -d news -f newsdata.sql
```

### Connect to database
```
$ psql -d news
```

### Create views

```
news=> create view article_request as select title, slug, log.time from articles, log where log.path like CONCAT('/article/', articles.slug) and status = '200 OK';
```

```
news=> create view author_article as select authors.name, articles.slug from authors, articles where authors.id = articles.author order by authors.name;
```

```
news=> create view requests_per_day as select DATE(time) as date, count(*) from log group by date;
```

```
news=> create view errors_per_day as select DATE(time) as date, count(*) from log where status = '404 NOT FOUND' group by date;
```

## How to run
```
python log.py
```