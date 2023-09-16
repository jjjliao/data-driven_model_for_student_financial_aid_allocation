import numpy as np

def entropy_weights(matrix):
    # 计算评价指标得分矩阵的行数和列数
    m, n = matrix.shape

    # 计算评价指标得分矩阵的列归一化矩阵
    normalized_matrix = matrix / np.sum(matrix, axis=0)

    # 计算每个评价指标的信息熵
    entropy = -np.sum(normalized_matrix * np.log2(normalized_matrix), axis=0)

    # 计算每个评价指标的权重
    weights = (1 - entropy) / np.sum(1 - entropy)

    return weights