import pandas as pd
import numpy as np
data = pd.read_csv("D:/wtz_code/shumo/数据集聚类标注.csv")

labels = data["聚类种类"]

from sklearn.cluster import KMeans


# 创建KMeans对象并指定聚类簇的数量
kmeans = KMeans(n_clusters=3)

# 执行K-means聚类
kmeans.fit(data)

# 获取聚类结果，即每个样本所属的簇标签
labels = kmeans.labels_

# 获取聚类的中心点
centroids = kmeans.cluster_centers_

# 输出聚类结果和中心点
print("聚类结果：", labels)
print("聚类中心点：", centroids)

import matplotlib.pyplot as plt


# 绘制聚类图
plt.rcParams['font.sans-serif']= ['SimHei']
plt.title('K-means Clustering')
for i in range(n):
    for j in range(n):
        plt.subplot(5,5,5 * j + i + 1 )
        plt.scatter(data[i], data[j], c = labels, cmap='viridis')
        plt.xlabel("features"+str(i))
        plt.ylabel("features"+str(j))
plt.show()
