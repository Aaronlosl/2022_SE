#-*- coding:utf-8 -*-
import re
import jieba
import numpy as np
from collections import Counter
import difflib


def filter_str(s):
    # 去除数字
    str = re.sub('[0-9]', '*', s)
    # 定义空格
    m=re.compile('\s+')
    # 去除空格
    str = re.sub(m, '*', str)
    # 去除标点符号
    punctuation = """，！？＂#＄％＆＇（）＊＋－／：；＜＝＞＠［＼］＾＿｀｛｜｝～、〃》「」『』【】〔〕〖〗~〝〞–—‘'‛“”„。‟…‧,.﹏"""
    re_punctuation = "[{}]+".format(punctuation)
    str = re.sub(re_punctuation, '*', str)
    str = re.sub('\*', '', str)
    return str


def cos_sim(str1, str2):
    co_str1 = (Counter(str1))
    co_str2 = (Counter(str2))
    p_str1 = []
    p_str2 = []
    for temp in set(str1 + str2):
        p_str1.append(co_str1[temp])
        p_str2.append(co_str2[temp])
    p_str1 = np.array(p_str1)
    p_str2 = np.array(p_str2)
    return p_str1.dot(p_str2) / (np.sqrt(p_str1.dot(p_str1)) * np.sqrt(p_str2.dot(p_str2)) + 0.001)


def search_strategy(s, titles, obj_pk):
    list1 = jieba.lcut(filter_str(s))
    score_list, title_list, ans = [], [], []
    for title in titles:
         str2 = filter_str(title)
         list2 = jieba.lcut(filter_str(title))
         score1 = difflib.SequenceMatcher(None, s, str2).ratio()
         score2 = cos_sim(list1,list2)
         tot_score = score1*0.5 + score2*0.5
         score_list.append(tot_score)
    
    pk_list = sorted(range(len(score_list)), key=lambda k: score_list[k], reverse=True)
    for pk in pk_list:
        ans.append(obj_pk[pk])
    return ans
    

if __name__ == '__main__':
    s = "物理"
    titles = ['物理课','物理竞赛','物理老师']
    print(search_strategy(s, titles))
    
    
