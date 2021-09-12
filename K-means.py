#!/usr/bin/env python
# coding: utf-8

# In[39]:


from __future__ import print_function 
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial.distance import cdist

np.random.seed(11)
means = [[2, 2], [8, 3], [3, 6]]
cov = [[1, 0], [0, 1]]
N = 500
K = 4
X0 = np.random.multivariate_normal(means[0], cov, N)
X1 = np.random.multivariate_normal(means[1], cov, N)
X2 = np.random.multivariate_normal(means[2], cov, N)
X = np.concatenate((X0, X1, X2), axis = 0)

plt.plot(X0[:, 0], X0[:, 1], 'b^', markersize = 4, alpha = .8)
plt.plot(X1[:, 0], X1[:, 1], 'go', markersize = 4, alpha = .8)
plt.plot(X2[:, 0], X2[:, 1], 'rs', markersize = 4, alpha = .8)
plt.axis('equal')

def initialize_centroids(points, k):
    centroids = points.copy()
    np.random.shuffle(centroids)
    return centroids[:k]

plt.subplot(121)
plt.scatter(X[:, 0], X[:, 1])
centroids = initialize_centroids(X, K)
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

plt.subplot(122)
plt.scatter(X[:, 0], X[:, 1])
closest = closest_centroid(X, centroids)
centroids = move_centroids(X, closest, centroids)
plt.scatter(centroids[:, 0], centroids[:, 1], c='r', s=100)

def closest_centroid(X, centroids):
    distances = np.sqrt(((X - centroids[:, np.newaxis])**2).sum(axis=2))
    return np.argmin(distances, axis=0)

c = initialize_centroids(X, K)
closest_centroid(X, c)

def move_centroids(X, closest, centroids):
    return np.array([X[closest==k].mean(axis=0) for k in range(centroids.shape[0])])

move_centroids(X, closest_centroid(X, c), c)




# In[ ]:





# In[ ]:




