import torch
import torch.nn as nn

INPUT_LENGHT = 14
OUTPUT_LENGHT = INPUT_LENGHT


class NeuralNetwork(nn.Module):
    def __init__(self):
        super(NeuralNetwork, self).__init__()
        self.layer1 = nn.Linear(INPUT_LENGHT, 50)  # Input layer with 10 features and 50 outputs
        self.relu = nn.ReLU()            # ReLU activation function
        self.layer2 = nn.Linear(50, 50)
        self.layer3 = nn.Linear(50, OUTPUT_LENGHT)   # Output layer with 1 output

    def forward(self, x):
        x = self.layer1(x)
        x = self.relu(x)
        x = self.layer2(x)
        x = self.relu(x)
        x = self.layer3(x)
        return x

# load the model
model = NeuralNetwork()
model.load_state_dict(torch.load('model.pth'))
model.eval() # set the model to evaluation mode
print('Model loaded')


chr_to_index = {chr(i): i + 1 - ord('a') for i in range( ord('a'), ord('z')+1 )}
index_to_chr = {i + 1- ord('a'): chr(i) for i in range( ord('a'), ord('z')+1 )}
chr_to_index[' '] = 0
index_to_chr[0] = ' '
for i in range(10):
    chr_to_index[str(i)] = i + 27
    index_to_chr[i + 27] = str(i)

def str_to_tensor(word):
    tensor = torch.zeros(INPUT_LENGHT)
    for c, char in enumerate(word):
        if c >= INPUT_LENGHT:
            break
        if char.lower() not in chr_to_index:
            value = 0
        else:
            value = (chr_to_index[char.lower()] + 0.5) / 36
        #print(value)
        tensor[c] = value
    return tensor

def tensor_to_str(tensor):
    s = ''
    for i in tensor:
        index = int(i.item() * 36)
        index = max(0, min(35, index))
        s += index_to_chr[index]
    return s


# get the output of the model
def get(input_str):
    input_tensor = str_to_tensor(input_str)
    output = model(input_tensor)
    str_output = tensor_to_str(output)
    return str_output


if __name__ == '__main__':
    print('Enter a string to get the output')
    while True:
        input_str = input('Enter a string: ')
        if input_str == 'exit' or input_str == '':
            break
        str_output = get(input_str)
        print(f"> {str_output}")
        
    