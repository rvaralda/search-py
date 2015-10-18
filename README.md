#Search-py

Search example using Elasticsearch written in Python.

It consumes https://swapi.co/ to index, and return sw caracters with movies.

To run:

```
$ export ES_HOST=<elasticsearch_host>
$ export ES_PORT=<elasticsearch_port>

$ pip install -r requirements.txt
$ python run.py

```

To run with docker, use:

```
$ docker run -e "ES_HOST=<elasticsearch_host> -e "ES_PORT=9200" -d -p 5000:5000 \
--name search-go search-go
```