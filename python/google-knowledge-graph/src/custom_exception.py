class NoResultFound(Exception):
  def __init__(self):
    self.value = 'No results found'
