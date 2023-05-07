import numpy as np
import pandas as pd

# path = '../data/tranform.csv'
# data = pd.read_csv(path, encoding='utf-8')
# data = data.set_index('cntid')
# data_dic = data.to_dict('index')
# data = np.array(data).tolist()
# print(data_dic)

# path_ = '../data/搜人得到的人15000.csv'
# data_ = pd.read_csv(path_, encoding='utf-8')
# data__score = data_['score']
# # print(data_)
# #
# data_id = data_['key']
# data_id = np.array(data_id).tolist()
# # print(data_id)
#
# ans = []
# for i in range (len(data_id)):
#     if (data_id[i] in data_dic.keys()):
#         ans.append(data_dic.get(data_id[i])['cntid'])
# # print(ans)
# df = pd.DataFrame()
# df['cntid'] = ans
# df = pd.concat([df, data__score], axis=1)
# print(df)
# df = df.set_index('cntid')
# df_dic = df.to_dict('index')
#
# score = []
path_node = '../data/node_socre.csv'
data_node = pd.read_csv(path_node, encoding='utf-8')
data_node_score = data_node['score']

# data_node_list = np.array(data_node['cntid']).tolist()
# for i in range (len(data_node_list)):
#     if (data_node_list[i] in df_dic.keys()):
#         score.append(df_dic.get(data_node_list[i])['score'])
# print(score)
#
# data_node['score'] = score
# data_node.to_csv('./data/node_socre.csv', index=False, header=True)



# ans = []
# for i in range (len(data_node_list)):
#     if (data_node_list[i] in data_dic.keys()):
#         ans.append(data_dic.get(data_node_list[i])['_id'])
# data_node['_id'] = ans
# data_node.to_csv('../data/node_id_cntid.csv', index=False, header=True)