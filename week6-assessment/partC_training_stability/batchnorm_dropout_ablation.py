import torch
import torch.nn as nn

# MLP with Batch Normalization and Dropout
class StableMLP(nn.Module):
    def __init__(self):
        super().__init__()
        self.model = nn.Sequential(
            nn.Flatten(),
            nn.Linear(28 * 28, 256),
            nn.BatchNorm1d(256),
            nn.ReLU(),
            nn.Dropout(p=0.5),
            nn.Linear(256, 10)
        )

    def forward(self, x):
        return self.model(x)

# Run check
if __name__ == "__main__":
    model = StableMLP()
    print("Stable MLP with BatchNorm and Dropout:")
    print(model)
