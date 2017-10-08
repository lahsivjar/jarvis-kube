# Simple flask python app for hello world
import json

from flask import Flask
app = Flask(__name__)

@app.route("/")
def print_hello():
  return json.dumps({
    'type': 'message',
    'result': 'Hello World~'
  })

if __name__ == '__main__':
  app.run()

