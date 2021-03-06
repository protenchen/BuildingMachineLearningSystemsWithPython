# This code is supporting material for the book
# Building Machine Learning Systems with Python
# by Willi Richert and Luis Pedro Coelho
# published by PACKT Publishing
#
# It is made available under the MIT License

from matplotlib import pyplot as plt
import numpy as np
from sklearn.datasets import load_iris
from threshold import learn_model, apply_model, accuracy

data = load_iris()
features = data['data']
labels = data['target_names'][data['target']]


setosa = (labels == 'setosa')
features = features[~setosa]
labels = labels[~setosa]
virginica = (labels == 'virginica')

testing = np.tile([True, False], 50)
training = ~testing

model = learn_model(features[training], virginica[training])
train_error = accuracy(features[training], virginica[training], model)
test_error = accuracy(features[testing], virginica[testing], model)

print('''\
Training error was {0:.1%}.
Testing error was {1:.1%} (N = {2}).
'''.format(train_error, test_error, testing.sum()))
