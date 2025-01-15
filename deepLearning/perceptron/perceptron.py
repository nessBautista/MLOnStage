import numpy as np

class Perceptron:
    """A Perceptron classifier implementation.

    Parameters
    ----------
    eta : float, default=0.01
        Learning rate (between 0.0 and 1.0).
        Controls how much to adjust the weights with each update.
    
    n_iter : int, default=50
        Number of passes (epochs) over the training dataset.
        Controls training duration.
    
    random_state : int, default=1
        Random number generator seed for reproducibility.
        Used for weight initialization.

    Attributes
    ----------
    w_ : ndarray of shape (n_features,)
        Weights vector after fitting.
    
    b_ : float
        Bias unit after fitting.
    
    errors_ : list
        Number of misclassifications (updates) in each epoch.
    """
    def __init__(self, eta=0.01, n_iter=50, random_state=1):
        """Initialize Perceptron object.

        Parameters
        ----------
        eta : float, default=0.01
            Learning rate (between 0.0 and 1.0)
        n_iter : int, default=50
            Number of passes over the training dataset
        random_state : int, default=1
            Random number generator seed for reproducibility
        """
        if not (0.0 <= eta <= 1.0):
            raise ValueError('Learning rate must be between 0.0 and 1.0')
        if not isinstance(n_iter, int) or n_iter <= 0:
            raise ValueError('n_iter must be a positive integer')
            
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        """Train the perceptron classifier.
        
        Parameters
        ----------
        X : {array-like}, shape = [n_examples, n_features]
            Training vectors
        y : array-like, shape = [n_examples]
            Target values
        
        Returns
        -------
        self : object
        """
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=X.shape[1])
        self.b_ = 0.0
        self.errors_ = []

        for _ in range(self.n_iter):
            errors = 0
            for xi, target in zip(X, y):
                update = self.eta * (target - self.predict(xi.reshape(1, -1)))
                self.w_ += update * xi
                self.b_ += update
                errors += int(update != 0.0)
            self.errors_.append(errors)
        return self

    def net_input(self, X):
        """Calculate net input.
        
        Parameters
        ----------
        X : array-like, shape = [n_examples, n_features]
            Training vectors
        
        Returns
        -------
        float
            Net input calculated as: X * W + b
        """
        return np.dot(X, self.w_) + self.b_
    
    def predict(self, X):
        """Return class label after unit step.
        
        Parameters
        ----------
        X : array-like, shape = [n_examples, n_features]
            Training vectors
            
        Returns
        -------
        ndarray, shape = [n_examples]
            Predicted class labels
        """
        return np.where(self.net_input(X) >= 0.0, 1, 0)
