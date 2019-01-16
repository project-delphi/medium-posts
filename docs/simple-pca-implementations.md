* * *

# Simple PCA implementations

[![Go to the profile of Ravi Kalia](https://cdn-images-1.medium.com/fit/c/100/100/0*fe677vY3CNf954Pl.jpg)](https://medium.com/@ravikalia?source=post_header_lockup)[Ravi Kalia](https://medium.com/@ravikalia)<span class="followState js-followState" data-user-id="e0e4bcb153a4"><button class="button button--smallest u-noUserSelect button--withChrome u-baseColor--buttonNormal button--withHover button--unblock js-unblockButton u-marginLeft10 u-xs-hide" data-action="sign-up-prompt" data-sign-in-action="toggle-block-user" data-requires-token="true" data-redirect="https://medium.com/@ravikalia/simple-pca-implementations-7edb130fb01b" data-action-source="post_header_lockup"><span class="button-label  button-defaultState">Blocked</span><span class="button-label button-hoverState">Unblock</span></button><button class="button button--primary button--smallest button--dark u-noUserSelect button--withChrome u-accentColor--buttonDark button--follow js-followButton u-marginLeft10 u-xs-hide" data-action="sign-up-prompt" data-sign-in-action="toggle-subscribe-user" data-requires-token="true" data-redirect="https://medium.com/_/subscribe/user/e0e4bcb153a4" data-action-source="post_header_lockup-e0e4bcb153a4-------------------------follow_byline"><span class="button-label  button-defaultState js-buttonLabel">Follow</span><span class="button-label button-activeState">Following</span></button></span><time datetime="2019-01-16T04:39:52.453Z">Jan 15</time><span class="middotDivider u-fontSize12"></span><span class="readingTime" title="2 min read"></span>![](https://cdn-images-1.medium.com/max/1600/1*BXRspA514UGWSgkpCtS5hw.jpeg)Photo by [Henry & Co.](https://unsplash.com/photos/3coKbdfnAFg?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText) on [Unsplash](https://unsplash.com/search/photos/construction-site?utm_source=unsplash&utm_medium=referral&utm_content=creditCopyText)

_This is part of a series on Principal Components Analysis (PCA), there’s a lot more to come._

In this post we’ll construct simple implementations of PCA using spectral decomposition in the open source languages R, Python( NumPy, TensorFlow, & PyTorch) and TensorFlowJS. These matrix based languages have been chosen since they are heavily used in Machine Learning communities and free.

Other than missing some bells and whistles, this implementation is not the most efficient. Numerical stability and better memory/compute properties mean that the algorithm is coded using SVD (a different matrix factorization) for most popular implementations, more on this later.

We will add some additional operations:

*   mean centering variables
*   Scaling variables to unit variance

Zero centering

The scaling of variables to unit variance(the columns of the data matrix), reduces the information available to the PCA algorithm, but it can improve the final results, mitigating the influence of variables with much larger variance than others.

* * *

### Covariance Matrix

The covariance matrix of a zero centered data matrix is

covariance(**X**) **= XX`**, where **X`** is used to indicate the transpose of matrix **X**

### R

<pre name="987a" id="987a" class="graf graf--pre graf-after--h3 graf--trailing">
pr_comp <- function(X, k, centre=T, scale=T){
  X_center <- X - ifelse(center, mean(X), 0)
  covariance <- X_center %*% transpose(X_center)
  scaling <- ifelse(scale, sqrt(1/(diag(covariance))), 1)
  scaled_covariance <- diag(scaling) %*% covariance
  eig <- eigen(scaled_covariance)
  components <- eig['vectors']
  explained_variance <- eig['values']
  return(list(X=X, k=k, components=components,     
    explained_variance=explained_variance)
}
</pre>

* * *

### NumPy

Use pip to install the necessary python packages or use a Docker environment

<pre name="e884" id="e884" class="graf graf--pre graf-after--p graf--trailing">import numpy as np
`# shortly`</pre>

* * *

### TensorFlow

```
import tensorflow as tf# soon
```

* * *

### PyTorch

<pre name="bb92" id="bb92" class="graf graf--pre graf-after--h3 graf--trailing">import pytorch as pt
`# soon`</pre>

* * *

### **TensorFlowJS**

Use either yarn or npm to install the dependencies locally

<pre name="025b" id="025b" class="graf graf--pre graf-after--p">// Load the binding
import * as tf from '@tensorflow/tfjs-node';

// Or if running with GPU:
import * as tf from '@tensorflow/tfjs-node-gpu';</pre>

```
# soon
```