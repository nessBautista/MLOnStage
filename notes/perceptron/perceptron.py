import numpy as np 

class Perceptron:
    """A Perceptron classifier implementation.

    Parameters
    ----------
    eta : float, default=0.1
        Learning rate (between 0.0 and 1.0).
        Controls how much to adjust the weights with each update.
    
    n_iter : int, default=50
        Number of passes (epochs) over the training dataset.
    
    random_state : int, default=1
        Random number generator seed for random weight initialization.
    """

    def __init__(self, eta=0.1, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state


    def fit(self, X, y):
        """Fit training data.

        Parameters
        ----------
        X : shape = [n_samples, n_features]
            n_samples is the number of data points we have for training
            n_features is the number of features that decribes our data, for example for a 2D dataset representing points in a plane
            n_features is the number of dimensions of the data.
        """
        rgen = np.random.RandomState(self.random_state)
        
        # For initialization we need to set random weights for each feature.
        # Other wise the learning rule will produce increments of 0 and the perceptron will not learn anything.
        self.w_ =rgen.normal( # generates a random numbers from a normal distribution
            loc=0.0, # mean of the normal distribution
            scale=0.01, # standard deviation of the normal distribution
            size = X.shape[1] # number of features
        )
        # bias is a scalar, it is ok to have it as zero initially.
        # The initial linear separator is a hyperplane that passes through the origin.
        self.b_ = np.float_(0.)
        self.errors_ = []

        # let's iterate over the number of epochs for our training (learning)
        for _ in range(self.n_iter):
            errors = 0

            for  xi, target in zip(X, y):
                # update will contain the error by the learning rate
                # we calculate it in a separate variable so it can be user later for tracking the error
                update = self.eta * (target - self.predict(xi))
                self.w_ += update * xi 
                self.b_ += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input"""
        return np.dot(X, self.w) + self.b_
    
    def predict(self, X):
         """Return class label after unit step"""
         return np.where(self.net_input(X) >= 0.0, 1, 0)
    

    
        
