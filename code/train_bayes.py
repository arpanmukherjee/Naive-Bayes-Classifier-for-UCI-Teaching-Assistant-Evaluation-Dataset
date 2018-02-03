import pickle
import numpy as np


feature_len = [2, 25, 26, 2, 7]


def train_model(training_data):
    training_model = []
    class1 = []
    class2 = []
    for i in feature_len:
        class1.append([0.0]*i)

    for i in feature_len:
        class2.append([0.0]*i)

    for features in training_data:
        if features[5] == 3:
            for i in range(5):
                if i == 4:
                    class2[i][features[i] / 10] += 1
                else:
                    class2[i][features[i]-1] += 1
        else:
            for i in range(5):
                if i == 4:
                    class1[i][features[i] / 10] += 1
                else:
                    class1[i][features[i]-1] += 1

    for feature in class1:
        total = sum(feature)
        for i in range(len(feature)):
            feature[i] /= total

    for feature in class2:
        total = sum(feature)
        for i in range(len(feature)):
            feature[i] /= total

    training_model.append(class1)
    training_model.append(class2)
    pickle.dump(training_model, open("model.p", "wb"))