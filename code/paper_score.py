import pandas as pd
import numpy as np

path_my_score = '../data/my_data_words_score.csv'
data_my_score = pd.read_csv(path_my_score, encoding='utf-8')
score1 = np.array(data_my_score['score']).tolist()

path_dcy_score = '../data/搜人得到的人15000.csv'
data_dcy_score = pd.read_csv(path_dcy_score, encoding='utf-8')
score2 = np.array(data_dcy_score['score']).tolist()

score = []
for i in range (len(score1)):
    for j in range (len(score2)):
        score.append(score1[i] + score2[i])
        break
# print(score)
