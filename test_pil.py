#!/usr/local/bin/python
# -*- coding: utf-8 -*-
'''test_pil
'''

from PIL import Image
from PIL import ImageChops
from PIL import ImageMath
from PIL import ImageDraw
from PIL import ImageFont
import matplotlib.pyplot as plt
import matplotlib.patches as patches
import matplotlib
import numpy as np

TEST_IMG = 'D:/Temp/fuji_red_201711090065_top_img_A.jpg'
FNT = 'fonts/migu-1m-bold.ttf'

fnt = {'family': 'Migu 1M'}
matplotlib.rc('font', **fnt)
fig, ax = plt.subplots(1)
plt.title('富士山')
img = Image.open(TEST_IMG)
dr = ImageDraw.Draw(img)
dr.font = ImageFont.truetype(FNT, 48)
txt, col, bk = '日本語', (255, 255, 0), (0, 0, 0,)
dr.text((np.array(img.size) - np.array(dr.font.getsize(txt))) / 2, txt, col)
dr.line([(100, 100), (200, 200)], col, 3)
dr.ellipse(((300, 300), (400, 400)), fill=bk, outline=col)
dr.rectangle(((450, 450), (500, 500)), fill=bk, outline=col)
im = np.array(img, dtype=np.uint8)
ax.imshow(im)
p, w, h = (75, 175), 150, 50
rct = patches.Rectangle(p, w, h, linewidth=1, edgecolor='r', facecolor='none')
ax.add_patch(rct)
plt.show()
