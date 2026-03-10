import torch
import torch.nn as nn
import torch.nn.functional as F

class AptamerNet(nn.Module):

    def __init__(self):

        super().__init__()

        self.fc1=nn.Linear(3,32)
        self.fc2=nn.Linear(32,64)
        self.fc3=nn.Linear(64,32)
        self.out=nn.Linear(32,1)

    def forward(self,x):

        x=F.relu(self.fc1(x))
        x=F.relu(self.fc2(x))
        x=F.relu(self.fc3(x))

        return self.out(x)


def predict_dl(features):

    model=AptamerNet()

    x=torch.tensor([
        features["contacts"],
        features["avg_distance"],
        features["interface_density"]
    ],dtype=torch.float32)

    x=x.unsqueeze(0)

    pred=model(x)

    return pred.detach().cpu().item()
