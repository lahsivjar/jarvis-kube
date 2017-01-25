import queryclient
import utility

from flask import Flask
from flask import request
from flask import jsonify
from custom_exception import NoResultFound

mapping = Flask(__name__)

# This method will return a detailed description of the query as per 
# the first search result
@mapping.route("/v1/get/description", methods=['GET'])
def get_desciption():
  query = request.args.get('query')
  try:
    result = utility.get_first_result(queryclient.do(query, 1))
    return utility.get_article_body_from_result(result)
  except NoResultFound as e:
    return e.value

if __name__ == "__main__":
    mapping.run()
