import re

class NotValidCell(Exception):
  pass

class Cell(object):

  def __init__(self, value, permanent=False):
    self.value = value
    self.permanent = permanent

  @property
  def value(self):
    return self._value

  @value.setter
  def value(self, v):
      if not (re.match('^\d$', v)):
        raise NotValidCell("Value must single digit.")
      self._value = v

  def unset(self):
    self._value = None

  def set(self, value):
    self.value = value

if __name__ == '__main__':
  c = Cell('1')
  c.value = '2'
  c.unset()
  c.set('1')
  print(c.value)

