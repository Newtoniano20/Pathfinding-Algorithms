import tensorflow as tf
import pandas as pd
import numpy as np

column_names = ['Point1_X', 'Point1_Y', 'Point2_X', 'Point2_Y', 'Point3_X', 'Point3_Y', 'Distance1', 'Distance2', 'Distance3', 'Unknownx', 'Unknowny']

model = tf.keras.models.load_model('model.keras')

to_predict = pd.DataFrame([[20, 10, -15, 0, 0, -80, 19, 17.52, 86.28]], columns=column_names[:9])
# to_predict = pd.DataFrame([[1, 1, 3, 4, 4, 3, np.sqrt(2), 5, 5]], columns=column_names[:9])
print(model.predict([to_predict]))