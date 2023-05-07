import numpy as np
import pandas as pd

path_my_node = '../data/my_node.csv'
data_my_node = pd.read_csv(path_my_node, encoding='utf-8')
# print(data_my_node['cntid'])
data = np.array(data_my_node['cntid']).tolist()
# print(data)

path_author = '../data/author.csv'
data_author = pd.read_csv(path_author, encoding='utf-8')
name = data_author['name']
cntid = data_author['cntid']
df = pd.concat([name, cntid], axis=1)
print(df)
dff = df.set_index(cntid)
df2dic = dff.to_dict('index')

ans = []
for i in range (len(data)):
    if (data[i] in df2dic.keys()):
        rb = df2dic.get(data[i])
        ans.append(rb['name'])
    print(i * 1.00 / len(data))
print(ans)
ans_df = pd.DataFrame(ans)
ans_df.to_csv('../data/cntid2name.csv', index=False, header=True)

