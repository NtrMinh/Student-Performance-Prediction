import numpy as np
import pandas as pd

import tensorflow as tf

#from tensorflow import keras
#from tensorflow.keras import layers


dnn_model = tf.keras.models.load_model('D:\documents\FRONTEND CODE\PREDICTION FLASK\DNN MODEL\dnn_model')

x = [4. , 4. , 4. , 4. , 4. , 4. , 4, 4 ]

FYP = dnn_model.predict(x)

print(FYP)