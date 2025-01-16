import numpy as np

class Adaline:
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        self.eta = eta
        self.n_iter = n_iter 
        self.random_state = random_state
    
    def fit(self, X, y):
        # Random values for our weights
        #  W is a column vector of (m, 1) where n is the number of features
        #  X is a matrix (n, m) where n is the number of samples and m the number of input features. 
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(
                    loc=0.0, 
                    scale=0.01,
                    size=X.shape[1] # Take the m value of X's shape, which is the number of features.
                  )
        self.b_ = np.float_(0.)
        self.losses_  = []

        for _ in range(self.n_iter):
            # get the net input
            z = self.net_input(X)
            # get the error 
            errors = y - z 
            # update the weights 
            # W(m,1), X.T(m,n)  , error(n, 1)
            self.w_ +=  self.eta * 2.0 * X.T.dot(errors) / X.shape[0]
            # update the bias
            # b(1,1), error(n, 1)
            self.b_ += self.eta * 2.0 * errors.mean()
            loss = (errors**2).mean()
            self.losses_.append(loss)
        return self







    def net_input(self, X):
        #  W is a column vector of (m, 1) where n is the number of features
        #  X is a matrix (n, m) where n is the number of samples and m the number of input features. 
        # z is a column vector of (n, 1) 
        z = np.dot(X, self.w_) + self.b_
        return z

    def activation(self, X):
        return X

    def predict(self, X):
        return np.where(self.activation(self.net_input(X))>= 0.5, 1, 0)
