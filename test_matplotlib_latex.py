#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''test_matplotlib_latex
##rerwrite for py3k
print(matplotlib.matplotlib_fname())
#cp .../mpl-data/matplotlibrc ~/.matplotlib
#vi ~/.matplotlib/matplotlibrc
  font.serif : Source Han Code JP
  font.sans-serif : Source Han Code JP
#rm ~/.matplotlib/fontList.py3k.cache
'''

import sys, os
import numpy as np
import matplotlib
from matplotlib import pyplot as plt

if False:
  matplotlib.rcParams['text.usetex'] = True
  matplotlib.rcParams['text.latex.unicode'] = True

if False:
  plt.rc('text', usetex=True)
  plt.rc('font', family='serif')

#FNs = 'serif'
FNs = 'sans-serif'

def test_matplotlib_latex():
  x = np.arange(0.0, 2.0 * np.pi, 0.1)
  y = np.cos(x)
  plt.plot(x, y)
  #plt.title(r'$cos(x)$', fontsize=25, fontname=FNs)
  plt.title('日本語', fontsize=25, fontname=FNs)

  #plt.legend([r'''$\left(abc\right)$'''], loc='lower left')
  ##plt.legend([r'''$\left(\begin{array}{rrr}1&2&3\\4&5&6\\7&8&9\end{array}\right)$'''], loc='lower left')
  ##plt.legend([r'''$\begin{array}{rrr}1&2&3\\4&5&6\\7&8&9\end{array}$'''], loc='lower left')
  ##plt.legend([r'''$\left(1&2&3\\4&5&6\\7&8&9\right)$'''], loc='lower left')

  ##plt.legend([r'''$\begin{document}\begin{figure}\begin{center}a\end{center}\end{figure}\end{document}$'''], loc='lower left')
  #plt.legend([r'''$a$'''], loc='lower left')
  plt.legend([r'''$日本語$'''], loc='lower left') # no glyph

  ##plt.legend([r'''$\begin{eqnarray}\overrightarrow{\rm OA}\end{eqnarray}$'''], loc='lower left')
  #plt.legend([r'''$\overrightarrow{\rm OA}$'''], loc='lower left')

  plt.xlabel('t', fontsize=20, fontname=FNs)
  plt.ylabel(r'$\mu_0$', fontsize=20, fontname=FNs)
  plt.xticks([0, 3, 4, 5, 7], ['text', 'a', 'b', 'c', 'd'])
  plt.yticks(fontsize=15)
  plt.show()

if __name__ == '__main__':
  print(matplotlib.matplotlib_fname())
  test_matplotlib_latex()
