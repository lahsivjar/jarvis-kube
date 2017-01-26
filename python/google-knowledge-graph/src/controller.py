import queryclient
import utility
import responsebuilder

from flask import Flask
from flask import request
from flask import jsonify
from custom_exception import NoResultFound

mapping = Flask(__name__)

# This method will return a detailed description of the query as per 
# the first search result
@mapping.route("/v1/describe", methods=['GET'])
def describe():
  query = request.args.get('query')
  try:
    result = utility.get_first_result(queryclient.do(query, 1))
    return responsebuilder.build_msg(utility.get_article_body_from_result(result))
  except NoResultFound as e:
    return responsebuilder.build_msg(e.value)

if __name__ == "__main__":
    mapping.run()
