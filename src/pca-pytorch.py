import torch
from sklearn import datasets
from sklearn.decomposition import PCA


def PCA_eig(X,k, center=True, scale=False):
  n,p = X.size()
  ones = torch.ones(n).view([n,1])
  h = ((1/n) * torch.mm(ones, ones.t())) if center  else torch.zeros(n*n).view([n,n])
  H = torch.eye(n) - h
  X_center =  torch.mm(H.double(), X.double())
  covariance = 1/(n-1) * torch.mm(X_center.t(), X_center).view(p,p)
  scaling =  torch.sqrt(1/torch.diag(covariance)).double() if scale else torch.ones(p).double()
  scaled_covariance = torch.mm(torch.diag(scaling).view(p,p), covariance)
  eigenvalues, eigenvectors = torch.eig(scaled_covariance, True)
  components = (eigenvectors[:, :k]).t()
  print(components)
  explained_variance = eigenvalues[:k, 0]
  print(explained_variance)
  return { 'X':X, 'k':k, 'components':components,     
    'explained_variance':explained_variance }

# TEST
def PCA_test_eig():
  iris = datasets.load_iris()
  iris_data = torch.from_numpy(iris.data)
  n, p = iris_data.size()
  k = p
  X_reduced = PCA(n_components=k).fit(iris.data)
  X_reduced_eig = PCA_eig(iris_data, k)
  comps_isclose = (torch.allclose(
   torch.abs(torch.from_numpy(X_reduced.components_).double()),
   torch.abs(X_reduced_eig['components'])
   ))
  print('Equal Components: ', comps_isclose)
  vars_isclose = (torch.allclose(
   torch.from_numpy(X_reduced.explained_variance_).double(),
   X_reduced_eig['explained_variance']
   ))
  print('Equal Explained Variance: ', vars_isclose)
  return

PCA_test_eig()

def PCA_svd(X, k, center=True):
  n = X.size()[0]
  ones = torch.ones(n).view([n,1])
  h = ((1/n) * torch.mm(ones, ones.t())) if center  else torch.zeros(n*n).view([n,n])
  H = torch.eye(n) - h
  X_center =  torch.mm(H.double(), X.double())
  u, s, v = torch.svd(X_center) 
  components  = v[:k].t()
  explained_variance = torch.mul(s[:k], s[:k])/(n-1)
  return { 'X':X, 'k':k, 'components':components,     
    'explained_variance':explained_variance }

# TEST
def PCA_test_svd():
  iris = datasets.load_iris()
  iris_data = torch.from_numpy(iris.data)
  n, p = iris_data.size()
  k = p
  X_reduced = PCA(n_components=k).fit(iris.data)
  X_reduced_svd = PCA_svd(iris_data, k)
  comps_isclose = (torch.allclose(
   torch.abs(torch.from_numpy(X_reduced.components_).double()),
   torch.abs(X_reduced_svd['components'])
   ))
  print('Equal Components: ', comps_isclose)
  vars_isclose = (torch.allclose(
   torch.from_numpy(X_reduced.explained_variance_).double(),
   X_reduced_svd['explained_variance']
   ))
  print('Equal Explained Variance: ', vars_isclose)
  return

#PCA_test_svd()