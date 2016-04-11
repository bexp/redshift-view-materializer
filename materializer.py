import json;
from sqlalchemy import *;

engine = create_engine('CONNECTION STRING')
connection = engine.connect()

with open('config.json', 'r') as jsonFile:
    jsonString = jsonFile.read()

config = json.loads(jsonString)

snippets = config['snippets']

for snippet in snippets:
    with open(snippets[snippet]) as snippetFile:
        snippets[snippet] = snippetFile.read()

for view in config['views']:
    with open(view['query_file'], 'r') as queryFile:
        query = queryFile.read()

    for snippet in snippets:
        query = query.replace(snippet, snippets[snippet])

    trans = connection.begin()

    connection.execute('drop table if exists ' + view['name'] + ';')
    connection.execute('create table ' + view['name'] + ' as ' + query)
    connection.execute('grant select on ' + view['name'] + ' to ' + view['user_list'] + ';')

    trans.commit()