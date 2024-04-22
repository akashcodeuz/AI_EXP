#code for nerual network
import numpy as np
from keras.models import Sequential
from keras.layers import Dense

# Define the training data
X_train = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_train = np.array([0, 1, 1, 0])

# Create a Sequential model
model = Sequential()

# Add a Dense layer with 2 units and ReLU activation function for the input layer
model.add(Dense(units=2, input_dim=2, activation='relu'))

# Add a Dense layer with 1 unit and sigmoid activation function for the output layer
model.add(Dense(units=1, activation='sigmoid'))

# Compile the model with binary cross-entropy loss and Adam optimizer
model.compile(loss='binary_crossentropy', optimizer='adam', metrics=['accuracy'])

# Fit the model to the training data for 1000 epochs
model.fit(X_train, y_train, epochs=1000)

# Define the test data
X_test = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
y_test = np.array([0, 1, 1, 0])

# Evaluate the model on the test data and get the accuracy
_, accuracy = model.evaluate(X_test, y_test)

# Print the accuracy
print("Accuracy: %.2f%%" % (accuracy * 100))
