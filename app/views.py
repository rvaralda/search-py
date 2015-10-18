from app import app
from flask import render_template, stream_with_context, Response

import requests, json, os

from elasticsearch import Elasticsearch


# configuration
app.config.update(dict(
    ES_HOST = os.environ['ES_HOST'],
    ES_PORT = os.environ['ES_PORT']
))

# Elasticsearch 
es = Elasticsearch([{'host': app.config['ES_HOST'], 'port': app.config['ES_PORT'] }])

#index
def add_data():
    r = requests.get('http://' + app.config['ES_HOST'] + ':' + app.config['ES_PORT'] ) 
    i = 1
    yield "People\n"
    while r.status_code == 200:
        if i == 17:
            i = 18
        r = requests.get('http://swapi.co/api/people/'+ str(i))
        yield str(i) + ' Add: ' + json.loads(r.content)['name'].encode('utf-8') + '\n'
        # print str(i) + ' Add: ' + json.loads(r.content)['name'].encode('utf-8') + '\n'
        es.index(index='sw', doc_type='people', id=i, body=json.loads(r.content))
        i += 1

@app.route('/index')
def index():
    def generate():
        for row in add_data():
            yield row
    return Response(stream_with_context(generate()))


#search
@app.route('/search/<query>')
def search(query):
    results = es.search(index="sw", body={"query": {"fuzzy_like_this_field" : { "name" : {"like_text": query, "max_query_terms":5}}}})
    return render_template('search_results.html',
                            query=query,
                            results=results['hits']['hits'])

if __name__ == '__main__':
    app.run()