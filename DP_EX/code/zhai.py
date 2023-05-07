import pandas as pd
import numpy as np

# path_node = '../data/my_node_socre.csv'
# data_node = pd.read_csv(path_node, encoding='utf-8')
# data_node_cntid = data_node['cntid']
# data_node_cntid_list = np.array(data_node_cntid).tolist()
# print(data_node_cntid_list)
#
# path = '../data/aaa.author.csv'
# data = pd.read_csv(path, encoding='utf-8')
# data = data.set_index('cntid')
# data_dic = data.to_dict('index')

path_my = '../data/my.csv'
data_my = pd.read_csv(path_my, encoding='utf-8')
data_source = np.array(data_my['source']).tolist()
data_target = np.array(data_my['target']).tolist()
print(data_source)
print(data_target)
# data_source_dic = data_source.to_dict('index')
# data_target_dic = data_target.to_dict('index')

path = '../data/author.csv'
author = pd.read_csv(path, encoding='utf-8')
name = author['name']
cntid = author['cntid']
df = pd.DataFrame()
df = pd.concat([name, cntid], axis=1)
print(df)
df = df.set_index('cntid')
df_dic = df.to_dict('index')


ans_source = []
for i in range (len(data_source)):
    if (data_source[i] in df_dic.keys()):
        ans_source.append(df_dic.get(data_source[i])['name'])
print(ans_source)

ans_target = []
for i in range (len(data_target)):
    if (data_target[i] in df_dic.keys()):
        ans_target.append(df_dic.get(data_target[i])['name'])
print(ans_target)

dff = pd.DataFrame()
dff['source'] = ans_source
dff['target'] = ans_target
dff = dff.iloc[0:543]
dff.to_csv('../data/my_edge.csv', index=False, header=True)
# data_node = data_node.drop(columns=['cntid'], axis=1)
# data_node['name'] = ans
# data_node_score = data_node['score']
# data_node = data_node.drop(columns=['score'], axis=1)


# data_node.to_csv('../data/myy_node_socre.csv', index=False, header=True)