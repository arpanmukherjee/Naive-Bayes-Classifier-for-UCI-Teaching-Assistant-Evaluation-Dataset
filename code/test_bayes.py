import numpy as np
from sklearn import metrics
import matplotlib.pyplot as plt
from sklearn.externals import joblib


model = joblib.load('model.p')


def draw_cm(actual, predict):
    confusion_matrix = np.zeros((2, 2))
    for a, p in zip(actual, predict):
        confusion_matrix[0 if a == 3 else a][0 if p == 3 else p] += 1
    plt.matshow(confusion_matrix)
    plt.colorbar()
    plt.show()
    accuracy = (actual == predict).sum() / float(len(actual))
    print(accuracy)


def draw_roc(actual, predict):
    

def test_model(testing_data):
    predict = []
    for feature in testing_data:
        class1 = class2 = 1.0
        for i in range(5):
            if i == 4:
                class1 *= (model[0][i][feature[i] / 10] + 1)
                class2 *= (model[1][i][feature[i] / 10] + 1)
            else:
                class1 *= (model[0][i][feature[i]-1] + 1)
                class2 *= (model[1][i][feature[i]-1] + 1)
        class1 /= 5
        class2 /= 5
        if class1 > class2:
            predict.append(1)
        else:
            predict.append(3)
    actual = np.array([i[5] for i in testing_data])
    predict = np.array(predict)
    # draw_cm(actual, predict)
    draw_roc(actual, predict)
