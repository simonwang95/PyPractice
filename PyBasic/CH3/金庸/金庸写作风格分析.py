import jieba

fnames = {'飞狐外传', '雪山飞狐', '连城诀', '天龙八部', '射雕英雄传', '白马啸西风', '鹿鼎记',\
          '笑傲江湖', '书剑恩仇录', '神雕侠侣', '侠客行', '倚天屠龙记', '碧血剑', '鸳鸯刀'}

def printJYChars(fname):
    '''
    输入：金庸作品文件名
    输出：前20最多字符
    d : 空字典，用于记录字频 / out: 用于输出
    '''
    txt = open(fname, 'r', encoding = 'utf8').read()
    d = {}
    out = ''
    
    for w in txt:
        d[w] = d.get(w, 0) + 1
    for w in "，。“”：？\n【】:' '「」∶":
        try:
            del d[w]
        except:
            pass
    # 统计字频，用字典记录，删除特殊字符的键
    
    lst = list(d.items())
    lst.sort(key = lambda x: x[1], reverse = True)
    # 根据值（出现次数）进行排序
    
    for i in range(20):
        word, count = lst[i]
        out += word
    #print(out)
    return out

def printJYWords(fname):
    #统计词频，使用jieba分词，统计两个字符以上的词
    txt = open(fname, 'r', encoding = 'utf8').read()
    d = {}
    out = ''
    
    for w in jieba.lcut(txt):
        if len(w) == 1:
            continue
        d[w] = d.get(w, 0) + 1
    
    lst = list(d.items())
    lst.sort(key = lambda x: x[1], reverse = True)
    
    for i in range(50):
        word, count = lst[i]
        out += word + ','
    return out

# 统计字频，利用集合求交集
txt1 = printJYChars("天龙八部" + ".txt")
A = set(txt1)
for fname in fnames:
    txt1 = printJYChars(fname + '.txt')
    A &= set(txt1)
print('金庸作品中出现频率最高的20个字是：')
print(A)
    
# 统计词频
txt2 = printJYWords('天龙八部' + '.txt')
B = set(txt2.strip(',').split(','))
#print(B)
for fname in fnames:
    txt2 = printJYWords(fname + '.txt')
    B &= set(txt2.strip(',').split(','))
print('金庸作品最高词频：')
print(B)

# 统计14部作品各自的词频分布
import pandas as pd

dic = {}
for fname in fnames:
    dic[fname] = [printJYChars(fname + '.txt'), printJYWords(fname + '.txt')]

data = pd.DataFrame(dic).T
data.columns = ['字频', '词频'] 
data.to_excel('金庸作品词频.xlsx', encoding = 'utf8')

print('finished')