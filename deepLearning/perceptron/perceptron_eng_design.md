# Perceptron Engineering Design Document

## Overview

This document outlines the design and implementation of a Perceptron classifier, a fundamental binary classification algorithm based on the original model proposed by Frank Rosenblatt in 1957.


## Class Design

### Class Name: Perceptron

A binary classifier implementation that learns a decision boundary through iterative weight updates.

### Attributes

#### Input Parameters
- `eta` (float): Learning rate between 0.0 and 1.0
  - Default: 0.01
  - Controls step size for weight updates
- `n_iter` (int): Number of passes over training dataset
  - Default: 50
  - Controls training duration
- `random_state` (int): Random seed for reproducibility
  - Default: 1
  - Used for weight initialization

#### Instance Variables
- `w_`: 1D NumPy array storing feature weights
- `b_`: Scalar storing bias unit
- `errors_`: List tracking misclassifications per epoch

### Methods

#### __init__(self, eta=0.01, n_iter=50, random_state=1)
Purpose: Initialize Perceptron object with hyperparameters
Inputs: eta, n_iter, random_state
Returns: None

#### net_input(X)
Purpose: Calculate linear combination of inputs
Inputs: X (feature vector)
Returns: dot product of weights and features plus bias
Implementation: np.dot(X, w_) + b_

#### predict(X)
Purpose: Classify input patterns
Inputs: X (feature vector to classify)  
Returns: Class label (0 or 1)
Implementation: Step function on net_input

#### fit(X, y)
Purpose: Train the perceptron classifier
Inputs:
- X: Training vectors [n_examples, n_features]
- y: Target values [n_examples]
Returns: self (trained model)
Process:
1. Initialize weights randomly using random_state
2. For n_iter epochs:
   - For each training example:
     - Compute prediction
     - Calculate update value
     - Update weights and bias
     - Track mistakes
3. Store error history



## Algorithm Details

### Training Process
1. Initialize weights to small random numbers
2. For each epoch:
   - For each training example (x_i, y_i):
     - Calculate: y_pred = step(w^T * x + b)
     - Update w = w + eta * (y_i - y_pred) * x_i
     - Update b = b + eta * (y_i - y_pred)
     - keep track on errors

### Weight Updates
- Update magnitude proportional to:
  - Learning rate (eta)
  - Prediction error (y_i - y_pred)
  - Input features (x_i)

### Convergence
- Guaranteed if classes are linearly separable
- For non-separable case, will oscillate
- Number of epochs limits training time

## Usage Example

```python
# Create classifier
ppn = Perceptron(eta=0.1, n_iter=10)

# Train
ppn.fit(X_train, y_train)

# Make predictions
y_pred = ppn.predict(X_test)
```

## Implementation Notes

1. Uses NumPy for efficient array operations
2. Implements online learning (example-by-example updates)
3. Stores error history for convergence analysis
4. Input validation not implemented - assumes proper data format

## Limitations

1. Binary classification only
2. Requires linearly separable classes for convergence
3. Sensitive to feature scaling
4. No regularization implemented
5. Basic implementation without optimization

## Future Improvements

1. Add input validation
2. Implement minibatch updates
3. Add regularization options
4. Support multiclass classification
5. Add feature scaling preprocessing
6. Optimize for large datasets

## Testing Strategy

1. Unit tests for individual methods
2. Integration tests with simple datasets
3. Verify convergence on linearly separable data
4. Test error handling
5. Benchmark performance

## References

1. Rosenblatt, F. (1957). The Perceptron: A Perceiving and Recognizing Automaton
2. McCulloch-Pitts Neuron Model (1943)