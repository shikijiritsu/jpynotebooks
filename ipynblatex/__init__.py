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
--------
'''

__version__ = '0.0.2'
