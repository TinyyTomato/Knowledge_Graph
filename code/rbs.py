import numpy as np
import pandas as pd

# path = '../data/dblp.csv'
# data = pd.read_csv(path, encoding='utf-8')
# data_list = np.array(data).tolist()
# print(data.isnull().sum())
#
# # 处理authors, 删除没有作者信息的论文
# rb_nan1 = str(data_list[0][1])
# rb_nan2 = str(data_list[17][1])
# list_del1 = []
# for i in range (len(data_list)):
#     if (str(data_list[i][1]) == rb_nan1 or str(data_list[i][1]) == rb_nan2):
#         list_del1.append(i)
#
# # 删除没有keywords和abstract信息的作者
# list_del2 = []
# for i in range (len(data_list)):
#     if ((str(data_list[i][3]) == rb_nan2 and str(data_list[i][4]) == rb_nan1) or
#             (str(data_list[i][3]) == rb_nan1 and str(data_list[i][4]) == rb_nan1)):
#         list_del2.append(i)
#
# list_ = []
# list_= list(set(list_del1).union(set(list_del2)))
# print(list_)
# print(len(list_))
#
# data_del = data.drop(data.index[list_])
# data_del_list = np.array(data_del).tolist()
# data_del = pd.DataFrame(data_del_list)
# data_del.to_csv('../data/data_del&author&keywords&abstract.csv', index=False, header=True)


'''
# 现在有zzh的1.2w数据，我需要把这其中作者对应的 论文 找出来（年份、关键字、摘要）
path_zzh = '../data/my_data_author_name_imp.csv'
# path_zzh = '../data/1.csv'
data_zzh = pd.read_csv(path_zzh, encoding='utf-8')
# data_zzh_author = np.array(data_zzh['author']).tolist()
data_zzh_author = np.array(data_zzh['author']).tolist()
# print(data_zzh_author)
# data_zzh = data_zzh.set_index('author')
# # print(data_zzh)
# data_zzh_dic = data_zzh.to_dict('index')
# print(data_zzh_dic)
# print(data_zzh_author)

path_data_del = '../data/data_del&author&keywords&abstract.csv'
# path_data_del = '../data/'
data_del = pd.read_csv(path_data_del, encoding='utf-8')
# 0是title, 1是authors, 2是year, 3是keywords, 4是abstract, 5是论文的cntid

# ans = []
# for i in range (0, 12887):
#     rb = []
#     ans.append(rb)
# print(ans)

data_del_author = data_del['1']
data_del_author_list = np.array(data_del_author).tolist()

final = []
for i in range (len(data_zzh_author)):
    flag = 0
    ans = []
    for j in range (len(data_del_author_list)):
        rb_list = data_del_author_list[j]
        rb_list_eval = eval(rb_list)
        # print(rb_list_eval)
        # for k in range(len(data_zzh_author)):
        for k in range (len(rb_list_eval)):
            if ('name' in rb_list_eval[k].keys()):
                if (rb_list_eval[k]['name'] == data_zzh_author[i]):
                    flag = 1
                    # print(data_zzh_author[i])
                    ans.append(j)
    if (flag == 0):
        rb = []
        rb.append(-1)
        final.append(rb)
    else:
        final.append(ans)

    print(i * 1.00 / len(data_zzh_author))
                  # if (data_zzh_dic[rb_list_eval[j]['name']] != None):
                  #     ans.append(i)
        # if (data_zzh_author[k] == rb_list_eval[j]['name']):
        #     ans.append(i)
        # if (flag):
        #     ans.append(flag)
        # else:
        #     ans.append(-1)
# for i in range (len(ans)):
    # print(ans[i])
# for i in range (len(anss)):
#     print(anss[i])
print(final)
for i in range (len(final)):
    print(final[i])
df = pd.DataFrame(final)
df.to_csv('../data/final.csv', index=False, header=True)


# [[-1], [1], [2], [0, 2]]
'''
path_data_del = '../data/data_del&author&keywords&abstract.csv'
data_del = pd.read_csv(path_data_del, encoding='utf-8')
# 补全缺省数据
data_del_keywords = data_del['3']
data_del_keywords_list = np.array(data_del_keywords).tolist()
# rb_empty1 = data_1w_del_keywords_list[1678]
for i in range (len(data_del_keywords_list)):
    if (data_del_keywords_list[i] == '[]'):
        data_del_keywords_list[i] = '["empty"]'
    # if (str(data_1w_del_keywords_list[i]) == str(rb_empty1)):
    #     data_1w_del_keywords_list[i] = 'empty'
    else:
        continue
# data_1w_del_keywords = pd.DataFrame(data_1w_del_keywords_list)

data_del_abstract = data_del['4']
data_del_abstract_list = np.array(data_del_abstract).tolist()
# print(data_1w_del_abstract_list)
rb_empty2 = data_del_abstract_list[1]
# print(str(rb_empty2) == str(data_1w_del_abstract_list[26]))
# print(str(data_1w_del_abstract_list[11]) == str(data_1w_del_abstract_list[26]))
for i in range (len(data_del_abstract_list)):
    if (str(data_del_abstract_list[i]) == str(rb_empty2)):
        data_del_abstract_list[i] = 'empty'
    else:
        continue
# data_1w_del_abstract = pd.DataFrame(data_1w_del_abstract_list)
# print(data_1w_del_abstract_list)

data_del_cntid = data_del['5']
data_del_cntid_list = np.array(data_del_cntid).tolist()

data_del = data_del.drop(columns=['3'], axis=1)
data_del = data_del.drop(columns=['4'], axis=1)
data_del = data_del.drop(columns=['5'], axis=1)
data_del['keywords'] = data_del_keywords_list
data_del['abstract'] = data_del_abstract_list
data_del['cntid'] = data_del_cntid_list
# print(data_1w_del)
# data_1w_del = pd.concat([data_1w_del, data_1w_del_keywords, data_1w_del_abstract, data_1w_del_cntid], columns=['', '', ''],axis=1)
# print(data_1w_del)
#
# data_1w_del.to_csv('../data/rb.csv', index=False, header=True)
author_index = pd.DataFrame(columns=('author', 'paper', 'year', 'keywords', 'abstract', 'cntid'))
title = data_del['0']
title_list = np.array(title).tolist()
# print(title)
year = data_del['2']
year_list = np.array(year).tolist()
keywords = data_del['keywords']
keywords_list = np.array(keywords).tolist()
abstract = data_del['abstract']
abstract_list = np.array(abstract).tolist()
cntid = data_del['cntid']
cntid_list = np.array(cntid).tolist()

print("begin writing!")
xh = 0
# 将csv文件变化为以author为索引: author是第一列
data_del_author = data_del['1']
data_del_author_list = np.array(data_del_author).tolist()
for i in range (len(data_del_author_list)):
    rb_list = data_del_author_list[i]
    rb_list_eval = eval(rb_list)
    for j in range (len(rb_list_eval)):
        if ('name' in rb_list_eval[j].keys()):
            rb_title = title[i]
            rb_year = year[i]
            rb_keywords = keywords[i]
            rb_abstract = abstract[i]
            rb_cntid = cntid[i]
            rb_name = rb_list_eval[j]['name']
            author_index.loc[xh] = [rb_name, rb_title, rb_year, rb_keywords, rb_abstract, rb_cntid]
            xh += 1
    print(i * 1.000 / len(data_del_author_list))
# print(author_index)
author_index.to_csv('../data/data_del&author&keywords&abstract_setauthorindex.csv', index=False, header=True)
'''




# path_another_author = '../data/author.csv'
# data_another_author = pd.read_csv(path_another_author, encoding='utf-8')
# # print(len(data_another_author))
# # print(data_another_author.isnull().sum())
# data_another_author_name = data_another_author['name']
# NULL = data_another_author_name[data_another_author_name.isnull().values == True]
# # print(NULL)
# rb_nan3 = str(data_another_author_name[7267])
# data_another_author_name_list = np.array(data_another_author_name).tolist()
#
# name_null = []
# for i in range (len(data_another_author_name_list)):
#     if (str(data_another_author_name_list[i]) == rb_nan3):
#         name_null.append(i)
# # print(name_null)
# # print(len(name_null))
#
# for i in range (len(name_null)):
#     data_another_author = data_another_author.drop(name_null[i])
# # print(data_another_author)
# # print(len(data_another_author))
#
# # org少了一半但先留着, 仅作为展示用
# data_another_author = data_another_author.drop(columns=['bio'], axis=1)
# data_another_author = data_another_author.drop(columns=['avatar'], axis=1)
# data_another_author = pd.DataFrame(np.array(data_another_author).tolist())
#
# xb = []
# for i in range (0, 10000):
#     xb.append(i)
# my_data_another_author = data_another_author.loc[xb]
# my_data_another_author.to_csv('../data/data_1w_delauthor_another_author.csv', index=False, header=True)
# 0是作者名字, 1是cntid, 2是org





# path_my_author_index = '../data/data_1w_delauthor_delkeywords&abstract_author_index.csv'
# data_my_author_index = pd.read_csv(path_my_author_index, encoding='utf-8')
# data_my_author_index['keywords'] = data_my_author_index['keywords'].fillna('["empty"]')
# # print(data_my_author_index)
# # print(data_my_author_index.isnull().sum())
#
#
# # 对离散数据归一化(年份)
# def normalization(x):
#     x_max=np.max(x,axis=0)
#     x_min=np.min(x,axis=0)
#     x_new=(x-x_min)/(x_max-x_min)
#     return x_new
#
# # data_my_author_index_year = data_my_author_index['year']
# # data_my_author_index_year = normalization(data_my_author_index_year)
#
# xb = []
# for i in range (0, 10000):
#     xb.append(i)
# data_my_author_index = data_my_author_index.loc[xb]
#
# data_my_author_index_title = data_my_author_index['paper']
# data_my_author_index_keywords = data_my_author_index['keywords']
# data_my_author_index_abstract = data_my_author_index['abstract']
# data_my_author_index_title = np.array(data_my_author_index_title).tolist()
# data_my_author_index_keywords = np.array(data_my_author_index_keywords).tolist()
# data_my_author_index_abstract = np.array(data_my_author_index_abstract).tolist()
# # # 第一个和第三个是list, 第二个是list嵌套list的形式
#
# list_title = []
# for i in range (len(data_my_author_index_title)):
#     list_title.append(data_my_author_index_title[i])
# # print(len(list_title))
#
# list_abstract = []
# for i in range (len(data_my_author_index_abstract)):
#     list_abstract.append(data_my_author_index_abstract[i])
# # print(len(list_abstract))
#
# # rb_keywords = data_my_author_index_keywords[12]
# # data_my_author_index_keywords_eval = eval(rb_keywords)
# # print(data_my_author_index_keywords_eval)
# list_keywords = []
# for i in range (len(data_my_author_index_keywords)):
#     rb_keywords = data_my_author_index_keywords[i]
#     data_my_author_index_keywords_eval = eval(rb_keywords)
#     list_keywords.append(data_my_author_index_keywords_eval)
# # print(list_keywords[0])
#
# rb_str_keywords = ''
# rb_str_keywords_list = []
# for i in range (len(list_keywords)):
#     for j in range (len(list_keywords[i])):
#         rb_str_keywords = list_keywords[i][j] + ' '
#         # print(rb_str_keywords)
#     rb_str_keywords_list.append(rb_str_keywords)
#
# words = []
# for i in range (len(list_title)):
#     rb_str = str(list_title[i]) + str(list_abstract[i]) + str(rb_str_keywords_list[i])
#     words.append(rb_str)
# # print(words)
#
# data_my_author_index = data_my_author_index.drop(columns=['paper'], axis=1)
# data_my_author_index = data_my_author_index.drop(columns=['keywords'], axis=1)
# data_my_author_index = data_my_author_index.drop(columns=['abstract'], axis=1)
# data_my_author_index['words'] = words
# data_my_author_index.to_csv('../data/data_1w_before_score.csv', index=False, header=True)

# path_before_score = '../data/data_1w_before_score.csv'
# data_before_score = pd.read_csv(path_before_score, encoding='utf-8')
#
# from TF_IDF import feature_select
# my_data_list = np.array(data_before_score['words']).tolist()
# list_list = []
# flag_list = [] # 全1
# for i in range (len(my_data_list)):
#     rb = []
#     rb.append(my_data_list[i])
#     flag_list.append(1)
#     list_list.append(rb)
#
# data_list, label_list = list_list, flag_list
# features = feature_select(data_list)  # 所有词的TF-IDF值
#
# ans = []
# for i in range (len(my_data_list)):
#     for j in range (len(features)):
#         if (my_data_list[i] == features[j][0]):
#             ans.append(features[j][1] * 1000)
#
# data_before_score = data_before_score.drop(columns=['words'], axis=1)
# data_before_score['TF-IDF'] = ans
#
# # 对离散数据归一化(年份)
# def normalization(x):
#     x_max=np.max(x,axis=0)
#     x_min=np.min(x,axis=0)
#     x_new=(x-x_min)/(x_max-x_min)
#     return x_new
#
# data_before_score_year = data_before_score['year']
# data_before_score_ = normalization(data_before_score_year)
# data_before_score_list = np.array(data_before_score_).tolist()
# data_before_score = data_before_score.drop(columns=['year'], axis=1)
# data_before_score['year'] = data_before_score_list
# data_before_score.to_csv('../data/data_1w_before_score_TF-IDF.csv', index=False, header=True)

# path_score = '../data/data_1w_before_score_TF-IDF.csv'
# data_score = pd.read_csv(path_score, encoding='utf-8')
# data_tfidf = data_score['TF-IDF']
# data_tfidf_list = np.array(data_tfidf).tolist()
# data_year = data_score['year']
# data_year_list = np.array(data_year).tolist()
# assert(len(data_tfidf_list) == len(data_year_list))
#
# score = []
# for i in range (len(data_tfidf_list)):
#     score_ = data_tfidf_list[i] + data_year_list[i]
#     score.append(score_)
# data_score = data_score.drop(columns=['TF-IDF'], axis=1)
# data_score = data_score.drop(columns=['year'], axis=1)
# data_score['score'] = score
# data_score.to_csv('../data/data_1w_score.csv', index=False, header=True)


import numpy as np
import pandas as pd

# path_return_author = '../data/node.csv'
# data_return_author = pd.read_csv(path_return_author, encoding='utf-8')
# data_return_author_list = np.array(data_return_author).tolist()
# # print(data_return_author_list)
# return_author_list = []
# return_author_importance = []
# # 手动记录第一个数据
# return_author_list.append(5354385)
# return_author_importance.append(5)
# for i in range (len(data_return_author_list)):
#     return_author_list.append(data_return_author_list[i][0])
#     return_author_importance.append(data_return_author_list[i][1])
#
# path_another_author = '../data/author.csv'
# data_another_author = pd.read_csv(path_another_author, encoding='utf-8')
# author_name = data_another_author['name']
# author_name_list = np.array(author_name).tolist()
# author_cntid = data_another_author['cntid']
# author_cntid_list = np.array(author_cntid).tolist()
# # data_another_author_list = np.array(data_another_author).tolist()
#
# my_author_name = []
# my_author_cntid = []
# my_author_importance = []
# for i in range (len(return_author_list)):
#     for j in range (len(author_cntid_list)):
#         if (return_author_list[i] == author_cntid_list[j]):
#             my_author_name.append(author_name_list[j])
#             my_author_cntid.append(author_cntid_list[j])
#             my_author_importance.append((return_author_importance[i]))
#         else:
#             continue
#
# print(my_author_name)
# print(my_author_cntid)
# print(my_author_importance)
# print(len(my_author_name))
# print(len(my_author_cntid))
# print(len(my_author_importance))
#
# my_author_name_df = pd.DataFrame(my_author_name)
# my_author_cntid_df = pd.DataFrame(my_author_cntid)
# my_author_importance_df = pd.DataFrame(my_author_importance)
# my_data_author_name_imp = pd.concat([my_author_name_df, my_author_cntid_df, my_author_importance_df], axis=1)
# # 未保留org信息(后续可以补充查找)
# my_data_author_name_imp.to_csv('../data/my_data_author_name_imp.csv', columns=['author', 'cntid', 'value'], index=False, header=True)

# path = '../data/my_data_author_name_imp.csv'
# data = pd.read_csv(path, encoding='utf-8')'''
