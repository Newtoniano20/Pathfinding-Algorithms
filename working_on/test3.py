import tensorflow as tf
import numpy as np

# Define the architecture of the neural network
model = tf.keras.Sequential([
    tf.keras.layers.Input(shape=(9,)),    # Input layer with 9 neurons
    tf.keras.layers.Dense(16, activation='relu'),  # Hidden layer with 16 neurons and ReLU activation
    tf.keras.layers.Dense(2)              # Output layer with 2 neurons (no activation function for regression)
])

# Compile the model
model.compile(optimizer='adam', loss='mean_squared_error')

# Generate some random training data (replace this with your actual data)
X_train = np.random.rand(100, 9)  # 100 samples with 9 features each
y_train = np.random.rand(100, 2)  # 100 samples with 2 target values each

# Train the model
model.fit(X_train, y_train, epochs=50, batch_size=32)  # Adjust the number of epochs and batch size as needed

# Make predictions
X_new = np.random.rand(10, 9)  # 10 samples for prediction
predictions = model.predict(X_new)

print("Predictions:")
print(predictions)