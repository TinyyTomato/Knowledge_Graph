import numpy as np
import pandas as pd

# data = pd.read_csv('../data/data_del&author&keywords&abstract.csv', encoding='utf-8')
# # 0是title, 1是authors, 2是year, 3是keywords, 4是abstract, 5是论文的cntid
# data_title = data['0'].fillna('empty')
# data_keywords = data['3'].fillna('["empty"]')
# data_keywords_list = np.array(data_keywords).tolist()
# for i in range (len(data_keywords_list)):
#     if (data_keywords_list[i] == '[]'):
#         data_keywords_list[i] = '["empty"]'
#     else:
#         continue
# data_keywords_ = pd.DataFrame(data_keywords_list, columns=['keywords'])
# data_abstract = data['4'].fillna('empty')
# my_data = pd.concat([data_title, data['2'], data_keywords_, data_abstract, data['5']], axis=1)
# my_data.to_csv('../data/my_data.csv', index=False, header=True)

# xb = []
# for i in range (0, 1000):
#     xb.append(i)
# my_data_1k = my_data.loc[xb]
# my_data_1k.to_csv('../data/my_data_1k.csv', index=False, header=True)








# data_ = pd.read_csv('../data/my_data.csv', encoding='utf-8')
# data_title = data_['0']
# data_keywords = data_['keywords']
# data_abstract = data_['4']
# data_title_ = np.array(data_title).tolist()
# data_keywords_ = np.array(data_keywords).tolist()
# data_abstract_ = np.array(data_abstract).tolist()
# # print(data_title_)
# # print(data_keywords_[0])
# # print(data_abstract_)
# # 第一个和第三个是list, 第二个是list嵌套list的形式
#
# list_title = []
# for i in range (len(data_title_)):
#     list_title.append(data_title_[i])
#     print(i * 1.00 / len(data_title_))
#
# list_abstract = []
# for i in range (len(data_abstract_)):
#     list_abstract.append(data_abstract_[i])
#     print(i * 1.00 / len(data_abstract_))
#
# list_keywords = []
# for i in range (len(data_keywords_)):
#     rb_keywords = data_keywords_[i]
#     data_my_author_index_keywords_eval = eval(rb_keywords)
#     list_keywords.append(data_my_author_index_keywords_eval)
#     print(i * 1.00 / len(data_keywords_))
#
# rb_str_keywords = ''
# rb_str_keywords_list = []
# for i in range (len(list_keywords)):
#     for j in range (len(list_keywords[i])):
#         rb_str_keywords = list_keywords[i][j] + ' '
#         # print(rb_str_keywords)
#     rb_str_keywords_list.append(rb_str_keywords)
#     print(i * 1.00 / len(list_keywords))
#
# words = []
# for i in range (len(list_title)):
#     rb_str = str(list_title[i]) + str(list_abstract[i]) + str(rb_str_keywords_list[i])
#     words.append(rb_str)
#     # print(i * 1.00 / len(list_title))
#
# data_ = data_.drop(columns=['0'], axis=1)
# data_ = data_.drop(columns=['keywords'], axis=1)
# data_ = data_.drop(columns=['4'], axis=1)
# data_['words'] = words
# data_.to_csv('../data/my_data_words.csv', index=False, header=True)



# data_ = pd.read_csv('../data/my_data_words.csv', encoding='utf-8')
# xb = []
# for i in range (0, 1000000):
#     xb.append(i)
# my_data_1M = data_.loc[xb]
# my_data_1M.to_csv('../data/my_data_1M.csv', index=False, header=True)



# data_ = pd.read_csv('../data/my_data_words.csv', encoding='utf-8')
# from TF_IDF import feature_select
# my_data_list = np.array(data_['words']).tolist()
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
#     # print(i * 1.00 / len(my_data_list))
#
# data_ = data_.drop(columns=['words'], axis=1)
# data_['TF-IDF'] = ans
# data_.to_csv('../data/my_data_words_tf-idf.csv', index=False, header=True)






# 对离散数据归一化(年份)
def normalization(x):
    x_max=np.max(x,axis=0)
    x_min=np.min(x,axis=0)
    x_new=(x-x_min)/(x_max-x_min)
    return x_new
data_ = pd.read_csv('../data/my_data_words_tf-idf.csv', encoding='utf-8')
data_year = data_['2']
data_year = normalization(data_year)
data_year_ = np.array(data_year).tolist()
# print(data_year_)
data_tfidf = np.array(data_['TF-IDF']).tolist()
# print(data_tfidf)

from sklearn.preprocessing import MinMaxScaler
scaler = MinMaxScaler(feature_range=(0, 100))
ans = []
for i in range (len(data_year_)):
    score = data_year_[i] * data_tfidf[i]
    ans.append(score)
ans_df = normalization(pd.DataFrame(ans))
ans_list = np.array(ans_df).tolist()
ans_ = scaler.fit_transform(pd.DataFrame(ans).values.reshape(-1, 1))
ans__ = ans_.tolist()
final_ans = []
for i in range (len(ans__)):
    final_ans.append(ans__[i][0])
print(final_ans)
data_ =data_.drop(columns=['2'], axis=1)
data_ =data_.drop(columns=['TF-IDF'], axis=1)
data_['score'] = final_ans
data_.to_csv('../data/my_data_words_score.csv', index=False, header=True)
