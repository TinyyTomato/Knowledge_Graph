import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
def cuircl(pointA,pointB):
    distance = np.sqrt(np.sum(np.power(pointA - pointB,2)))
    return distance

def firstCluster(dataSets,r,include):
    cluster = []
    m = np.shape(dataSets)[0]
    ungrouped = np.array([i for i in range (m)])
    for i in range (m):
        tempCluster = []
        #第一位存储中心点簇
        tempCluster.append(i)
        for j in range (m):
            if (cuircl(dataSets[i,:],dataSets[j,:]) < r and i != j ):
                tempCluster.append(j)
        tempCluster = np.mat(np.array(tempCluster))
        if (np.size(tempCluster)) >= include:
            cluster.append(np.array(tempCluster).flatten())
    center=[]
    n = np.shape(cluster)[0]
    for k in range (n):
        center.append(cluster[k][0])
    #非中心点
    ungrouped = np.delete(ungrouped,center)
    return cluster,center,ungrouped


def clusterGrouped(tempcluster,centers):
    m = np.shape(tempcluster)[0]
    group = []
    position = np.ones(m)
    unvisited = []
    unvisited.extend(centers)
    for i  in range (len(position)):
        coreNeihbor = []
        result = []
        if position[i]:
            coreNeihbor.extend(list(tempcluster[i][:]))
            position[i] = 0
            temp = coreNeihbor
            while len(coreNeihbor) > 0 :
                #选择当前点
                present = coreNeihbor[0]
                for j in range(len(position)):
                    #如果没有访问过
                    if position[j] == 1:
                        same = []
                        #求所有的可达点
                        if (present in tempcluster[j]):
                            cluster = tempcluster[j].tolist()
                            diff = []
                            for x in cluster:
                                if x not in temp:
                                    #确保没有重复点
                                    diff.append(x)
                            temp.extend(diff)
                            position[j] = 0
                # 删掉当前点
                del coreNeihbor[0]
                result.extend(temp)
            group.append(list(set(result)))
        i +=1
    return group


X,Y1 = datasets.make_circles(n_samples = 1500, factor = .4, noise = .07)
 
 
tempcluster,center,ungrouped = firstCluster(X,0.1,6)
group = clusterGrouped(tempcluster,center)
 
 
num = len(group)
voice = list(ungrouped)
Y = []
for i in range (num):
   Y.append(X[group[i]])
flat = []
for i in range(num):
    flat.extend(group[i])
diff = [x for x in voice if x not in flat]
Y.append(X[diff])
Y = np.mat(np.array(Y))

color = ['red','blue','green','black','pink','orange']
for i in range(num):
    plt.scatter(Y[0,i][:,0],Y[0,i][:,1],c=color[i])
plt.scatter(Y[0,-1][:,0],Y[0,-1][:,1],c = 'purple')
plt.show()