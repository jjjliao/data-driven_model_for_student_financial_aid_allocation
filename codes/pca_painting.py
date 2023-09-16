import numpy as np
import matplotlib.pyplot as plt

# 假设你已经有了 cumulative_variance_ratio 和 n_components 变量

# 创建主成分的序号数组
components = np.arange(1, len(cumulative_variance_ratio) + 1)

# 绘制关系图
plt.plot(components, cumulative_variance_ratio, marker='o', linestyle='-', color='b')
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Variance Ratio')
plt.title('Cumulative Variance Ratio vs. Number of Components')
plt.grid(True)
plt.show()