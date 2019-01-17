import torch
from sklearn import datasets
from sklearn.decomposition import PCA



def PCA_eig(X,k, center=True, scale=False):
  n,p = X.size()
  ones = torch.ones(n).view([n,1])
  h = ((1/n) * torch.mm(ones, ones.t())) if center  else torch.zeros(n*n).view([n,n])
  H = torch.eye(n) - h
  X_center =  torch.mm(H, X)
  covariance = 1/(n-1) * torch.mm(X_center.t(), X_center)
  scaling =  torch.sqrt(1/torch.diag(covariance)) if scale else torch.ones(p).view([p,1])
  scaled_covariance = torch.mm(torch.diag(scaling), covariance)
  w,v = torch.symeig(scaled_covariance)
  components = v[:, :k]
  explained_variance = w[:k]
  return { 'X':X, 'k':k, 'components':components,     
    'explained_variance':explained_variance }

#  torch.from_numpy(iris.data).float().to(device)

