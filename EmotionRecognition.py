from keras.models import Sequential
from keras.layers import Dense

import numpy

numpy.random.seed(7)

dataset = numpy.loadtxt("fer2013_reformatted.csv", delimiter=",")
X = dataset[:,0:2305]
Y = dataset[:,2305:2306]

model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))

model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

model.fit(X, Y, epochs=150, batch_size=10)

scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_name[1], scores[1]*100))

