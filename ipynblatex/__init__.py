#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''ipynblatex
use with (...env...)/Lib/site-packages/ipynbutl/__init__.py
--------
import sys, os
from notebook import notebookapp

ipynb_dir = None
wd = os.getcwd()
for svr in notebookapp.list_running_servers():
  nd = svr['notebook_dir']
  if wd.startswith(nd):
    sys.path.append(nd)
    ipynb_dir = nd
    break

__version__ = '.....'
--------
'''

import sympy
import numpy as np
from matplotlib import pyplot as plt
from IPython.display import display, Math, Latex

class ipynbLatex(object):
  def __init__(self):
    self.lexpr = []

  def setexpr(self, s=''):
    self.lexpr.append(s)

  def getlatex(self):
    l = sympy.latex(''.join(self.lexpr))
    self.lexpr = []
    return l

  def display(self, sl=None):
    display(Math(sl if sl else self.getlatex()))

__version__ = '1.0.1'
