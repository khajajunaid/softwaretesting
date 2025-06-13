import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.decomposition import PCA
import matplotlib.pyplot as plt
from sklearn import datasets


iris = datasets.load_iris()
data = pd.DataFrame(iris.data, columns=iris.feature_names)

scaler = StandardScaler()
data_scaled = scaler.fit_transform(data)


pca = PCA(n_components=2)
pca_result = pca.fit_transform(data_scaled)


explained_variance = pca.explained_variance_ratio_
print("Cumulative Explained Variance:", np.sum(explained_variance))


plt.figure(figsize=(8, 6))
for target, color in zip(np.unique(iris.target), ['r', 'g', 'b']):
    plt.scatter(pca_result[iris.target == target, 0],
                pca_result[iris.target == target, 1],
                label=iris.target_names[target],
                alpha=0.7,
                edgecolors='k')

plt.title("PCA on Iris Dataset")
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.legend()
plt.grid(True)
plt.show()