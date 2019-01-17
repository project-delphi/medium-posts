pr_comp <- function(X, k = ncol(X), center=T, scale=T){
  n <- dim(X)[1]
  p <- dim(X)[2]
  ones <- rep(1,n)
  H <- (diag(n) - (ifelse(center, (1/n) * ones %*% t(ones), 0)))
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
  explained_sd <- (eig$values)[1:k]
  return(list(X=X, k=k, components=components,     
    explained_sd=explained_sd))
}

# TEST
testPCA <- function(){
data(iris)
D <- data.matrix(iris[,c(1:4)])
pca_pr_comp <- pr_comp(D, scale=F)
pca_prcomp <- prcomp(D)
cat('\n Check for equivalence of pr_comp and prcomp: \n\n')
cat('\n components:', all(round(pca_pr_comp$components - pca_prcomp$rotation,3) == 0))
cat('\n explained_variance:', all(round(pca_pr_comp$explained_sd - pca_prcomp$sdev, 3) == 0))
cat('\n')
}

testPCA()



