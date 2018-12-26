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


def precision(y_true, y_pred):
    h_true = K.greater(y_true, 0.80)
    h_pred = K.greater(y_pred, 0.80)
    all = tf.reduce_sum(K.cast(h_true, K.floatx()))
    find = tf.reduce_sum(K.cast(h_pred, K.floatx()) * K.cast(h_true, K.floatx()))
    if all == 0:
        print('-------')
    return (find+K.epsilon())/(all+K.epsilon())


model = getModel()
model.compile(optimizer='RMSprop', loss='mean_squared_error', metrics=[acc, precision])


# --------------------------- train --------------------------------
import pickle
with open('data/27', mode='rb') as f:
    (train_x, test_x, train_y, test_y) = pickle.load(f)

model.fit(x=[train_x], y=[train_y], batch_size=32, epochs=64, validation_data=([test_x], [test_y]))