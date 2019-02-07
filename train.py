import torch
import torch.nn as nn
import torch.nn.functional as F

input_feature = 5
out_policy_number = 4

class Net(nn.Module):

    def __init__(self):
        super(Net, self).__init__()
        # 1 input image channel, 6 output channels, 5x5 square convolution
        # kernel

        # an affine operation: y = Wx + b
        self.fc1 = nn.Linear(input_feature, 120)
        self.fc2 = nn.Linear(120, 84)
        self.fc3 = nn.Linear(84, out_policy_number)

    def forward(self, x):
        # Max pooling over a (2, 2) window

        x = F.relu(self.fc1(x))
        x = F.relu(self.fc2(x))
        x = self.fc3(x)
        return x

net = Net()
learning_rate=0.1
criterion = nn.CrossEntropyLoss()


def train(epochnumber):
    for epoch in range(epochnumber):
        with torch.no_grad():
            inputs,labels,rewards = get_data_test(net)
        loss = 0.0
        for i in range(len(inputs)):
            input = inputs[i]
            label = labels[i].long()
            reward = rewards[i]
            output = net(input)
            loss += criterion(output, label)*reward
        net.zero_grad()
        loss.backward()
        for f in net.parameters():
            f.data.sub_(f.data.data*learning_rate)

def agent(net,input):

    output = net(input.unsqueeze(0))
    _,predicted = torch.max(output,1)
#    print(predicted)
    return predicted[0]



def get_data_test(net):
    inputs = torch.rand(10,10,5)
    labels = torch.zeros(10,10)
    for i in range(10):
        for j in range(10):
            result = agent(net,inputs[i,j])
            labels[i,j] = result
  #      outputs = net(inputs[i])
   #     _, predicted = torch.max(outputs,1)
  #      labels[i] = predicted
    rewards = torch.rand(10)
    return inputs, labels, rewards

train(10)


