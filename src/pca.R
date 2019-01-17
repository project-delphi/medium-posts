pr_comp <- function(X, k = ncol(X), center=T, scale=T){
  n <- dim(X)[1]
  p <- dim(X)[2]
  ones <- matrix(rep(1,n),nrow=n)
  if(center){
  H <- (diag(n) -  (1/n) * ones %*% t(ones))
  } else {
  H <- diag(n)
  }
  X_center <- H %*% X
  covariance <- 1/(n-1) * t(X_center) %*% X_center
  if(scale) {
  scaling <- sqrt(1/(diag(covariance)))
  } else {
  scaling <- rep(1, p)
  }
 scaled_covariance <- diag(scaling) %*% covariance
  eig <- eigen(scaled_covariance)
  components <- (eig$vectors)[, 1:k]
  explained_variance <- (eig$values)[1:k]
  return(list(X=X, k=k, components=components,     
    explained_variance=explained_variance))
}

pr_comp_SVD <- function(X, k = ncol(X), center=T){
  n <- dim(X)[1]
  ones <- rep(1,n)
  if(center){
   H <- (diag(n) -  (1/n) * ones %*% t(ones))
  } else {
   H <- diag(n)
  }
  X_center <- H %*% X
  factorization <- svd(X_center)
 return(list(X=X, k=k, components=factorization$v[,1:k],     
   explained_variance=1/(n-1)*(factorization$d^2)[1:k]))
}


# TEST
testPCA <- function(){
data(iris)
D <- data.matrix(iris[,c(1:4)])
pca_pr_comp <- pr_comp(D, scale=F)
pca_prcomp <- prcomp(D)
cat('\n Check for equivalence of pr_comp and prcomp: \n\n')
cat('\n components equal:', all(round(pca_pr_comp$components - pca_prcomp$rotation, 3) == 0))
cat('\n explained_variance equal:', all(round(pca_pr_comp$explained_variance - pca_prcomp$sdev^2, 3) == 0))
cat('\n')
}

testPCA()

testPCA_SVD <- function(){
data(iris)
D <- data.matrix(iris[,c(1:4)])
pca_pr_comp <- pr_comp_SVD(D)
print(pca_pr_comp)
pca_prcomp <- prcomp(D)
cat('\n Check for equivalence of pr_comp and prcomp: \n\n')
cat('\n components equal:', all(round(pca_pr_comp$components - pca_prcomp$rotation, 3) == 0))
cat('\n explained_variance equal:', all(round(pca_pr_comp$explained_variance - pca_prcomp$sdev^2, 3) == 0))
cat('\n')
}

testPCA_SVD()


