import numpy as np
from sklearn import datasets
from sklearn.decomposition import PCA

def PCA_eig(X,k, center=True, scale=False):
  n,p = X.shape
  ones = np.ones([n,1])
  h = ((1/n) * np.matmul(ones, ones.transpose())) if center  else np.zeros([n,n])
  H = np.eye(n) - h
  X_center =  np.matmul(H, X)
  covariance = 1/(n-1) * np.matmul(X_center.transpose(), X_center)
  scaling =  np.sqrt(1/np.diag(covariance)) if scale else np.ones(p)
  scaled_covariance = np.matmul(np.diag(scaling), covariance)
  w,v = np.linalg.eig(scaled_covariance)
  components = v[:, :k]
  explained_variance = w[:k]
  return { 'X':X, 'k':k, 'components':components,     
    'explained_variance':explained_variance }


# TEST
def PCA_test_eig():
  iris = datasets.load_iris()
  p = iris.data.shape[1]
  k = p
  X_reduced = PCA(n_components=k).fit(iris.data)
  X_reduced_eig = PCA_eig(iris.data, k)
  comp_diff = np.round(np.absolute(X_reduced.components_) - np.absolute(X_reduced_eig['components'].transpose()),3)
  print('Equal Components: ', np.array_equal(comp_diff,np.zeros([p,p])))
  var_diff = np.round(X_reduced.explained_variance_ -X_reduced_eig['explained_variance'], 3)
  print('Equal Explained Variance: ', np.array_equal(var_diff, np.zeros(k)))
  return

# PCA_test_eig()

def PCA_svd(X, k, center=True):
  n,p = X.shape
  ones = np.ones([n,1])
  h = ((1/n) * np.matmul(ones, ones.transpose())) if center  else np.zeros([n,n])
  H = np.eye(n) - h
  X_center =  np.matmul(H, X)
  u, s, v = np.linalg.svd(X_center) 
  components  = v[:k]
  explained_variance = np.square(s[:k])/(n-1)
  return { 'X':X, 'k':k, 'components':components,     
    'explained_variance':explained_variance }

# TEST
def PCA_test_svd():
  iris = datasets.load_iris()
  n, p = iris.data.shape
  k = p
  X_reduced = PCA(n_components=k).fit(iris.data)
  X_reduced_svd = PCA_svd(iris.data, k)
  comp_diff = np.round(np.absolute(X_reduced.components_) - np.absolute(X_reduced_svd['components']),3)
  print('Equal Components: ', np.array_equal(comp_diff,np.zeros([p,p])))
  var_diff = np.round(X_reduced.explained_variance_ - X_reduced_svd['explained_variance'], 3)
  print('Equal Explained Variance: ', np.array_equal(var_diff, np.zeros(k)))
  return


PCA_test_svd()

