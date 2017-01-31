import re

class NotValidCell(Exception):
  pass


class PermanentCell(Exception):
  pass


class Cell(object):

  def __init__(self, value, permanent=False):
    self.permanent = permanent
    self.value = value

  def __hash__(self):
    return hash(str(self))

  def __cmp__(self, other):
    # TODO(jedrzej): Implement better hashing method.
    return self.value == other.value

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, v):
      if self.permanent:
        raise PermanentCell("Cell is permanent.")
      if not (re.match('^\d$', str(v))):
        raise NotValidCell("Cell must single digit.")
      self._value = v

  def unset(self):
    self._value = None

  def set(self, value):
    self.value = value
