import numpy as np
from keras.layers import Input, LSTM, Dense, Reshape
from keras.layers import concatenate
from keras.models import Model
import keras.backend as K
import tensorflow as tf

inputs = Input((480,))
reshape = Reshape((480, 1))(inputs)
h = LSTM(1)(reshape)
o = concatenate([inputs, h])
d = Dense(32, activation='relu')(o)
r = Dense(1, activation='sigmoid')(d)


def getModel():
    model = Model(inputs=inputs, outputs=r)
    return model

def acc(y_true, y_pred):
    d = K.abs(tf.add(y_true, tf.negative(y_pred)))
    return K.mean(K.cast(K.greater(0.1, d), K.floatx()))

model = getModel()
model.compile(optimizer='RMSprop', loss='mean_squared_error', metrics=[acc])


# --------------------------- train --------------------------------
import pickle
with open('data/27', mode='rb') as f:
    (train_x, test_x, train_y, test_y) = pickle.load(f)

model.fit(x=[train_x], y=[train_y], batch_size=32, epochs=64, validation_data=([test_x], [test_y]))