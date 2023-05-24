from keras.models import Sequential
from keras.layers import Dense
from keras.optimizers import Adam

# Define your model
model = Sequential()

# Add a Dense layer with 768 input neurons (matching the input dimension)
# We use 'relu' as the activation function.
model.add(Dense(1024, input_dim=768, activation='relu'))

# Add more layers as needed - you can tweak the number of neurons
# The more complex the transformation between input and output, the more layers you will likely need
model.add(Dense(2048, activation='relu'))

# Add a Dense output layer with 1536 neurons (matching the output dimension)
model.add(Dense(1536, activation='linear'))  # Using 'linear' activation because this seems to be a regression problem

# Compile the model with mean squared error loss function, because you want to measure loss by difference
# Adam is a good default choice for optimizer
model.compile(loss='mean_squared_error', optimizer=Adam())

# You can print a summary of the model like this:
model.summary()