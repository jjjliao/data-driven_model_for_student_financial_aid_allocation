df = adde_1
import pandas as pd
from sklearn.decomposition import PCA
import numpy as np
# 假设你的数据存储在名为df的DataFrame对象中

# 创建PCA对象
pca = PCA()

# 执行PCA降维
pca.fit(df)

# 计算每个主成分的累计方差贡献
explained_variance_ratio = pca.explained_variance_ratio_

# 计算累计方差贡献的累积和
cumulative_variance_ratio = np.cumsum(explained_variance_ratio)

# 确定保留的主成分个数
n_components = np.argmax(cumulative_variance_ratio >= 0.255) + 1

# 根据保留的主成分个数重新执行PCA降维
pca = PCA(n_components=n_components)
reduced_data = pca.fit_transform(df)

# 输出降维后的数据
print("降维后的数据维度：", reduced_data.shape)

# 输出每个主成分的累计方差贡献
print("每个主成分的累计方差贡献：", cumulative_variance_ratio[:n_components])

# 可选：根据需要，将降维后的数据转换回DataFrame对象
data = pd.DataFrame(reduced_data)

# 对降维后的数据进行进一步的分析和评价
# 这可以包括可视化、聚类分析、分类器训练等
# 你可以根据你的具体需求对数据进行进一步的处理和探索
