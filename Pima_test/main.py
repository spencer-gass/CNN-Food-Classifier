#
#   Introductory Three Layer Fully Connected Neural Net
#
from keras.models import Sequential
from keras.layers import Dense
import numpy 
# fix random seed for repordicibility
numpy.random.seed(7)

# load pima indians dataset
dataset = numpy.loadtxt("pima-indians-diabetes.csv", delimiter=",")
# split data into input (X) and output (Y) variables
X = dataset[:,0:8]
Y = dataset[:,8]
# create a three layer neural net
model = Sequential()
model.add(Dense(12, input_dim=8, activation='relu'))
model.add(Dense(8, activation='relu'))
model.add(Dense(1, activation='sigmoid'))
# compile the NN model
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])
# Fit the model
model.fit(X, Y, epochs=500, batch_size=20)
# evaluate the model
scores = model.evaluate(X, Y)
print("\n%s: %.2f%%" % (model.metrics_names[1], scores[1]*100))