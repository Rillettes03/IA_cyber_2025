from elasticsearch import Elasticsearch
from elasticsearch.helpers import scan
import json

# Connexion à Elasticsearch
es = Elasticsearch("http://10.100.1.184:9200")

# Define the index and query
index_name = "good-malice"
query = {
    "query": {
        "match_all": {}
    },
}

# Fetch logs using scan (for large datasets)
results = scan(
    client=es,
    query=query,
    index=index_name,
    scroll='2m',
    size=1000
)

# Save results to a JSON file
logs = []
for doc in results:
    logs.append(doc['_source'])

with open('logs.json', 'w') as f:
    json.dump(logs, f, indent=2)

print("Logs have been downloaded successfully.")
