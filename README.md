# Logs Analysis Project
#### Udacity - [Full Stack Web Developer Nanodegree](https://www.udacity.com/course/full-stack-web-developer-nanodegree--nd004)

## About
This project is to create a reporting tool that prints out reports (in plain text) based on the data in the database. This reporting tool is a Python program using the psycopg2 module to connect to the database. 

Here are the questions the reporting tool should answer:

 1. What are the most popular three articles of all time? 
 2. Who are the most popular article authors of all time?
 3. On which days did more than 1% of requests lead to errors?

## Requirements
 * [Python3](https://www.python.org/)
 * [Vagrant](https://www.vagrantup.com/)
 * [VirtualBox](https://www.virtualbox.org/)

## VM Setup

#### Get VM files
```
$ git clone https://github.com/udacity/fullstack-nanodegree-vm
```

#### Start VM
```
$ cd vagrant
$ vagrant up
```

#### Login
```
$ vagrant ssh
```

## Database setup
Download database from [here](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip). Extract newsdata.sql file.

#### Load data
```
$ psql -d news -f newsdata.sql
```

#### Connect to database
```
$ psql -d news
```

#### Create views

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
$ python log.py
```