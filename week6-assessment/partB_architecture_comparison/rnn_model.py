import torch
import torch.nn as nn

class RNN(nn.Module):
    def __init__(self, input_size=28, hidden_size=128, num_classes=10):
        super().__init__()
        self.rnn = nn.RNN(input_size, hidden_size, batch_first=True)
        self.fc = nn.Linear(hidden_size, num_classes)

    def forward(self, x):
        # x shape: (batch, time_steps, features)
        out, _ = self.rnn(x)
        out = self.fc(out[:, -1, :])  # last time step
        return out

# Model check
if __name__ == "__main__":
    model = RNN()
    print(model)
