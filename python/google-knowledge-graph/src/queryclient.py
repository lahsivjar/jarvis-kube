import os
import json
import urllib

# Get API key that should be setup as environment variable
GOOGLE_API_KEY = os.environ['GOOG_KNOWLEDGE_GRAPH_API_KEY']

# Service URL for google's knowledge graph
SERVICE_ENDPOINT = 'https://kgsearch.googleapis.com/v1/entities:search'

# Method to query knowlege search endpoint
def do(query, limit):
  params = {
    'query': query,
    'limit': limit,
    'indent': False,
    'key': GOOGLE_API_KEY
  }
  url = SERVICE_ENDPOINT + '?' + urllib.urlencode(params)
  return json.loads(urllib.urlopen(url).read())
