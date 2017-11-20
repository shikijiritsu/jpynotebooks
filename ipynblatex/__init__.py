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

  def setexpr(self, ltxex=''):
    self.lexpr.append(ltxex)

  def getlatex(self):
    ltx = ''.join(sympy.latex(_) for _ in self.lexpr)
    self.lexpr = []
    return ltx

  def display(self, ltxex=None, isltx=True):
    if isltx: ltx = ltxex if ltxex else self.getlatex()
    else: ltx = sympy.latex(ltxex) if ltxex else self.getlatex()
    display(Math(ltx))

__version__ = '1.1.1'
