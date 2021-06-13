from __future__ import (absolute_import, division, print_function,
                        unicode_literals)
from builtins import (dict, int, round, str, super)

try:
  from actors import *
except ImportError:
  from .actors import *
try:
  from things import *
except ImportError:
  from .things import *

class TheTool(object):
  def __init__(self,*args,**kwargs):
    self.ten = 10
    self.actor = TheActor()
    self.thing = TheThing()
