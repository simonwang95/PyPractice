

import jieba
import wordcloud
from scipy.misc import imread
import os

os.chdir('C:\\Users\\10696\\Desktop\\project\\PyBasic\\四大名著\\')
mask = imread('6.bmp')
names = {'红楼梦.txt','三国演义.txt','水浒传.txt','西游记.txt'}
for name in names:
    f = open(name, 'r', encoding = 'utf-8')
    t = f.read()
    f.close()
    ls = jieba.lcut(t)
    txt = ' ' .join(ls)
    w = wordcloud.WordCloud(font_path='msyh.ttc', width =1000, height = 800, mask = mask, colormap = 'BuPu')
    w.generate(txt)
    w.to_file(name.split('.')[0] + '3.png')
    
print('finished')