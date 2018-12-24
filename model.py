import numpy as np
from keras.layers import Input, LSTM, Dense
from keras.layers import concatenate
from keras.models import Model

inputs = Input(240,)
h = LSTM(1)(inputs)
o = concatenate([inputs, h])
d = Dense(32, activation='relu')
r = Dense(1, activation='sigmoid')


def getModel():
    model = Model(inputs=inputs, outputs=r)
    return model


model = getModel()
model.compile(optimizer='RMSprop', loss='mean_squared_error', metrics=)