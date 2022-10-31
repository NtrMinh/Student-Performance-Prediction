import numpy as np
import pandas as pd

import tensorflow as tf

#from tensorflow import keras
#from tensorflow.keras import layers


dnn2_model = tf.keras.models.load_model('D:\documents\FRONTEND CODE\PREDICTION FLASK\DNN MODEL\dnn2_model')

x = [4. , 4 , 4 , 4. , 4 , 4. , 4, 4,1 ]

CGPA = dnn2_model.predict(x)

print(CGPA)