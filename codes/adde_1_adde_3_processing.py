import pandas as pd
from sklearn.decomposition import PCA
from scipy.stats import f_oneway

pca = PCA(n_components=100)

adde_1 = pd.read_excel('C:\\Users\\Herrywen\\Desktop\\adde_1.xlsx')
adde_2 = pd.read_excel('C:\\Users\\Herrywen\\Desktop\\adde_2.xlsx')
adde_3 = pd.read_excel('C:\\Users\\Herrywen\\Desktop\\adde_3.xlsx')

adde_3 = adde_3.iloc[:,1:]
adde_1 = adde_1.iloc[:,1:]
adde_2 = adde_2.iloc[:,1:]

non_zero_counts = adde_1.astype(bool).sum()
columns_to_drop = non_zero_counts[non_zero_counts < 1000].index
adde_1 =  adde_1.drop(columns_to_drop, axis=1)
adde_1

non_zero_counts = adde_2.astype(bool).sum()
columns_to_drop = non_zero_counts[non_zero_counts < 1000].index
adde_2 =  adde_2.drop(columns_to_drop, axis=1)
adde_2

non_zero_counts = adde_3.astype(bool).sum()
columns_to_drop = non_zero_counts[non_zero_counts < 1000].index
adde_3 =  adde_3.drop(columns_to_drop, axis=1)
adde_3