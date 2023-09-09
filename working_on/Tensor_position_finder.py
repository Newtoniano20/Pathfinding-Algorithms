import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3' 
import tensorflow as tf
import pandas as pd
import numpy as np

column_names = ['Point1_X', 'Point1_Y', 'Point2_X', 'Point2_Y', 'Point3_X', 'Point3_Y', 'Distance1', 'Distance2', 'Distance3', 'Unknownx', 'Unknowny']
                      
raw_dataset = pd.read_csv('./working_on/trilateration_training_data.csv', names=column_names, skiprows=1)
dataset = raw_dataset.astype('float32')

train_dataset = dataset.sample(frac=0.9, random_state=0)
test_dataset = dataset.drop(train_dataset.index)
train_features = train_dataset.copy()
test_features = test_dataset.copy()
train_labels = pd.concat([train_features.pop(x) for x in ['Unknownx', 'Unknowny']], axis=1)
test_labels = pd.concat([test_features.pop(x) for x in ['Unknownx', 'Unknowny']], axis=1)
print(test_labels.tail())

model = tf.keras.Sequential([
    tf.keras.layers.Normalization(axis=-1),
    tf.keras.layers.Dense(512, activation='relu', input_shape=(9,)),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(512, activation='relu'),
    tf.keras.layers.Dense(2)
])

optimizer = tf.keras.optimizers.Adam(learning_rate=0.0001)
model.compile(optimizer=optimizer, loss='mean_squared_error', metrics=["accuracy"])
model.fit(train_features, train_labels, epochs=10, batch_size=512)

test_loss, mse = model.evaluate(test_features, test_labels)
model.save('model.keras')