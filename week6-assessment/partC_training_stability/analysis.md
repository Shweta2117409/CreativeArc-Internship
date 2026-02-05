## Training Stability Analysis

### Effect of Learning Rate
In the learning rate experiment, different learning rates showed different training behaviors. When a very small learning rate was used, the loss decreased slowly, indicating slow learning. With a moderate learning rate, the loss decreased smoothly and training was stable. However, when a very large learning rate was used, the loss fluctuated heavily, showing unstable training behavior.

### Role of Batch Normalization
Batch normalization was applied after the hidden layer to normalize the activations. This helped reduce internal covariate shift and made the training process more stable. It also allowed the model to converge faster compared to a model without batch normalization.

### Role of Dropout
Dropout was used to randomly deactivate neurons during training. This prevented the model from depending too much on specific neurons and reduced overfitting. As a result, the model showed better generalization and more stable behavior during training.

### Conclusion
Training stability depends on proper hyperparameter selection and regularization techniques. Choosing an appropriate learning rate along with batch normalization and dropout improves convergence, reduces instability, and results in a more reliable neural network model.
