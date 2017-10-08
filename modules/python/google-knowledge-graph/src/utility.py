# Store utility methods to parse results

from custom_exception import NoResultFound

def get_result_list(target_jsonld):
  return target_jsonld['itemListElement'];

def get_first_result_item(target_jsonld):
  result_list = get_result_list(target_jsonld)
  try:
    return result_list[0]
  except IndexError:
    return {}

def get_first_result(target_jsonld):
  first_result_item = get_first_result_item(target_jsonld)
  try:
    return first_result_item['result']
  except KeyError:
    raise NoResultFound()

def get_article_body_from_result(target_result):
  detailed_desc = target_result['detailedDescription']
  return detailed_desc['articleBody']
