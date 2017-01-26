import json

# Build the response as expected by jarvis administrator
def build_msg(message):
  response = {
    'type': 'message',
    'result': message
  }
  return json.dumps(response)
