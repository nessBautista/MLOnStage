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
