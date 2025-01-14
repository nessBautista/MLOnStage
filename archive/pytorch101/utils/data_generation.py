import torch
from typing import Tuple, Optional
import numpy as np

def generate_linear_data(
    weight: float = 0.7,
    bias: float = 0.3,
    start: float = 0.0,
    end: float = 1.0,
    step: float = 0.02,
) -> tuple[torch.Tensor, torch.Tensor]:
    """Generate synthetic data following a linear pattern: y = weight * x + bias.

    Args:
        weight (float, optional): The slope of the linear relationship. Defaults to 0.7.
        bias (float, optional): The y-intercept of the linear relationship. Defaults to 0.3.
        start (float, optional): Start value for x range. Defaults to 0.0.
        end (float, optional): End value for x range (exclusive). Defaults to 1.0.
        step (float, optional): Step size between x values. Defaults to 0.02.

    Returns:
        tuple[torch.Tensor, torch.Tensor]: A tuple containing:
            - X: Input features tensor of shape (n_samples, 1)
            - y: Target values tensor of shape (n_samples, 1)
    """
    # Generate evenly spaced x values and reshape to (n_samples, 1)
    X = torch.arange(start, end, step).unsqueeze(dim=1)
    
    # Generate y values following linear pattern
    y = weight * X + bias
    
    return X, y 

def fetch_mnist(return_tensors: bool = True) -> Tuple[np.ndarray | torch.Tensor, np.ndarray | torch.Tensor]:
    """Fetch MNIST dataset using multiple fallback options.
    
    Args:
        return_tensors (bool, optional): If True, returns PyTorch tensors. If False, returns numpy arrays. 
            Defaults to True.
    
    Returns:
        Tuple containing:
            - X: Features with shape (n_samples, 784) if numpy array or (n_samples, 1, 28, 28) if tensor
            - y: Labels with shape (n_samples,)
            
    Raises:
        RuntimeError: If unable to fetch MNIST data from any source
    """
    try:
        # Try fetching from scikit-learn first (most reliable)
        from sklearn.datasets import fetch_openml
        X, y = fetch_openml('mnist_784', version='active', return_X_y=True, as_frame=False)
        
    except Exception:
        try:
            # Fallback to torchvision if scikit-learn fails
            from torchvision import datasets
            from torchvision.transforms import ToTensor
            import torch.utils.data as data_utils
            
            # Download training data from open datasets
            training_data = datasets.MNIST(
                root="data",
                train=True,
                download=True,
                transform=ToTensor(),
            )
            
            # Download test data from open datasets
            test_data = datasets.MNIST(
                root="data",
                train=False,
                download=True,
                transform=ToTensor(),
            )
            
            # Combine train and test data
            X = torch.cat([
                torch.stack([sample[0] for sample in training_data]),
                torch.stack([sample[0] for sample in test_data])
            ])
            y = torch.cat([
                torch.tensor(training_data.targets),
                torch.tensor(test_data.targets)
            ])
            
            if not return_tensors:
                # For numpy arrays, we want flat features
                X = X.reshape(X.shape[0], -1).numpy()
                y = y.numpy()
                return X, y
            
            return X, y
            
        except Exception as e:
            raise RuntimeError("Failed to fetch MNIST data from any source") from e
    
    # Handle the scikit-learn path
    if return_tensors:
        X = torch.from_numpy(X).float()
        if len(X.shape) == 2:  # If flat features, reshape to image format
            X = X.reshape(-1, 1, 28, 28)
        y = torch.from_numpy(y.astype(np.int64))
    
    return X, y 