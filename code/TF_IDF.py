from collections import defaultdict
import math
import operator
import numpy as np
import pandas as pd
import time
from tqdm import tqdm
from tqdm._tqdm import trange

"""
函数说明：特征选择TF-IDF算法
Parameters:
     list_words:词列表
Returns:
     dict_feature_select:特征选择词字典
     
#dataset:文件夹，word_list:某一个文件，word某个词
"""

def feature_select(dataset):
    # 总词频统计
    # 记录每个词出现的次数，可以把它理解成一个可变长度的list，只要你索引它，它就自动扩列
    doc_frequency = defaultdict(int)
    for file in dataset:
        for word in file:
            doc_frequency[word] += 1

    # 计算每个词的TF值
    # 存储没个词的tf值
    word_tf = {}
    for i in tqdm(doc_frequency):
        word_tf[i] = doc_frequency[i] / sum(doc_frequency.values())
    # 计算每个词的IDF值
    doc_num = len(dataset)
    # 存储每个词的idf值
    word_idf = {}
    # 存储包含该词的文档数
    word_doc = defaultdict(int)
    for word in tqdm(doc_frequency):
        for file in dataset:
            if word in file:
                word_doc[word] += 1

    # word_doc和doc_frequency的区别是word_doc存储的是包含这个词的文档数，
    # 即如果一个文档里有重复出现一个词则word_doc < doc_frequency
    for word in tqdm(doc_frequency):
        word_idf[word] = math.log(doc_num / (word_doc[word] + 1))

    # 计算每个词的TF*IDF的值
    word_tf_idf = {}
    for word in tqdm(doc_frequency):
        word_tf_idf[word] = word_tf[word] * word_idf[word]

    # 对字典按值由大到小排序
    dict_feature_select = sorted(word_tf_idf.items(), key=operator.itemgetter(1), reverse=True)
    return dict_feature_select
