import jieba
import wordcloud
from scipy.misc import imread
import os

fnames = {'飞狐外传', '雪山飞狐', '连城诀', '天龙八部', '射雕英雄传', '白马啸西风', '鹿鼎记',\
          '笑傲江湖', '书剑恩仇录', '神雕侠侣', '侠客行', '倚天屠龙记', '碧血剑', '鸳鸯刀'}

mask = imread('6.bmp')
t = ''
for name in fnames:
    f = open(name + '.txt', 'r', encoding='utf-8').read()
    t += f

ls = jieba.lcut(t)
txt = ' '.join(ls)
w = wordcloud.WordCloud(font_path='msyh.ttc', width=1000, height=800, mask=mask, colormap='binary', background_color = 'white')
w.generate(txt)
w.to_file('金庸词云1.png')

print('finished')