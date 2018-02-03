import numpy as np
from test_bayes import test_model
from train_bayes import train_model
path = '/home/arpn/Semester2/SML/SML-Assignment1/'

data = np.genfromtxt(path+'dataset.txt', delimiter=',', dtype=int)
np.random.shuffle(data)

margin = int(len(data)*0.7)

training_data = data[:margin]
testing_data = data[margin:]


# print(data.max(axis=0))
# train_model(training_data)
test_model(testing_data)