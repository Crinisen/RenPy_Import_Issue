from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import (dict, int, round, str, super)

try:
  # Try to load with absolute_import path
  from thingies import TheThing
except ImportError:
  # with absolute_import, I shouldn't need to use relative imports
  from .thingies import TheThing

class TheActor(object):
  def __init__(self,*args,**kwargs):
    self.thingy = TheThing()
    self.dictionary = dict()

  @property
  def all(self):
    return list()


class TheOtherActor(TheActor):
  pass
