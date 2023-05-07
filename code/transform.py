import numpy as np
import pandas as pd

path = '../data/tranform.csv'
data = pd.read_csv(path, encoding='utf-8')
data = data.set_index('_id')
data_dic = data.to_dict('index')
# data = np.array(data).tolist()
# print(data_dic)

path_ = '../data/搜人得到的人15000.csv'
data_ = pd.read_csv(path_, encoding='utf-8')
data_id = data_['key']
data_id = np.array(data_id).tolist()

path_node = '../data/node.csv'
data_node = pd.read_csv(path_node, encoding='utf-8')
data_node = data_node.set_index('cntid')
data_node_dic = data_node.to_dict('index')

ans = []
for i in range (len(data_id)):
    if (data_id[i] in data_dic.keys()):
        rb = data_dic.get(data_id[i])
        rb = rb['cntid']
        ans.append(rb)
print(ans)
    # print(i * 1.00 / len(data_))


node = []
for i in range (len(ans)):
    if (ans[i] in data_node_dic.keys()):
        node.append(ans[i])
    print(i * 1.00 / len(ans))
node_df = pd.DataFrame(node)
print(node_df)
node_df.to_csv('../data/my_node.csv', index=False, header=True)
#
# target = []
# path__ = '../data/edge.csv'
# edge_data = pd.read_csv(path__, encoding='utf-8')
# edge_data_list = np.array(edge_data).tolist()
# for i in range (len(edge_data_list)):
#     for j in range (len(list)):
#         if edge_data_list[i][0] == list[j]:
#             target.append(edge_data_list[i][1])
# print(target)
#
# data_ = np.array(data_).tolist()
# for i in range (len(target)):
#     for j in range (len(data_)):
#         if (target[i] == data_[j][0]):
#             print(data_[j][0])
