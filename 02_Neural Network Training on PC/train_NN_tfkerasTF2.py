#####################################################
#This program uses the internal Keras library of 
#TensorFlow for the training of the neural network.
#The architecture of the NN is 24-6-3. 
# Autor: Detlef Heinze 
# Version: 1.0    Use TensorFlow Version >= 2.0.0
# Tested with Tensorflow 2.3.0
# This programm needs the following installation for 
# saving the checkpoints: pip3 install h5py
#####################################################
#### Load dependencies
import tensorflow as tf
from tensorflow.keras import layers
from numpy import loadtxt, savetxt, reshape
import datetime as dt
print("TensorFlow Version: " + tf.__version__)
print("TF Keras Version: " + tf.keras.__version__)

#### Load data

start= dt.datetime.now() 
# Step 1: Import Training Data (xTrain und yTrain)
print('Lese xTrain- und yTrain-Daten')
xTrain= loadtxt('xTrain_TwoCubesCylinder375-24.csv')
yTrain= loadtxt('yTrain_TwoCubesCylinder375-3.csv')

# Step 2: Import Test Data (xTest und yTest)
print('Lese xTest und yTest-Daten')
xTest= loadtxt('xTest_TwoCubesCylinder300-24.csv')
yTest= loadtxt('yTest_TwoCubesCylinder300-3.csv')

#Parameter für das 24 - 6 - 3 neuronale Netz
n_input = 24   #24 Neuronen für die gemessene Daten
n_hidden_1 = 6 #Größe der versteckten Neuronenschicht
n_classes = 3  #Größe der ausgebenden Neuronenschicht
               #ist gleich der Anzahl der Klassen
print('NN-Architektur: ' + repr(n_input) +' - ' 
      + repr(n_hidden_1) + ' - ' 
      + repr(n_classes))

# Design neural network architecture

model = tf.keras.Sequential() #One layer after the other
model.add(layers.Dense(n_hidden_1, activation='relu', input_shape=(n_input,))) #Dense= fully connected
model.add(layers.Dense(n_classes, activation='softmax'))
model.summary()

# Configure model
model.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(0.001), metrics=['accuracy'])

# Create a Callback for checking the model's value accuracy after each epoch
# If the accuracy has improved the model is saved (overwriten) for later use

filepath= 'bestModel.hdf5'
checkpoint = tf.keras.callbacks.ModelCheckpoint(filepath, monitor='val_accuracy', verbose=1, save_best_only=True, mode='max')
callbacks_list = [checkpoint]

# Training

#Adapt number of epochs to get eventually better results (recommended: 100 to 300)
model.fit(xTrain, yTrain, batch_size=1, epochs=150, verbose=0, validation_data=(xTest, yTest), callbacks=callbacks_list)
duration = (dt.datetime.now() - start)
print("\nDuration: " + str(duration))

# Load best model of training to evaluate it

model.load_weights(filepath)
# Compile model (required to evaluate the model)
model.compile(loss='categorical_crossentropy', optimizer=tf.optimizers.Adam(0.001), metrics=['accuracy'])

# Evaluation

model.evaluate(xTest, yTest)

# Access model

result= model.get_weights()
weights_h1 = result[0]
biases_b1= result[1]
weights_out= result[2]
biases_out= result[3]

# Save model files (csv)

print('\n--------------Saving model(csv)-------------')
print('Saving NNweights_h1.csv')
savetxt('NNweights_h1.csv', weights_h1, fmt='%10.8f', delimiter=' ')
print('Saving NNbiases_b1.csv')
savetxt('NNbiases_b1.csv', biases_b1, fmt='%10.8f', delimiter=' ')
print('Saving NNweights_out.csv')
savetxt('NNweights_out.csv', weights_out, fmt='%10.8f', delimiter=' ')
print('Saving NNbiases_out.csv')
savetxt('NNbiases_out.csv', biases_out, fmt='%10.8f', delimiter=' ')

# Save model files for Lego Mindstorms robot (rtf)

print('\n--Saving model (rtf for Lego Mindstorms EV3)--')
#Format: <number of rows>CR<number of columns>CR<{<aReal>CR}*
print('Saving NNweights_h1.rtf')  
tmpArray = reshape(weights_h1, (weights_h1.shape[0] * weights_h1.shape[1],))
result= [weights_h1.shape[0],weights_h1.shape[1]] + tmpArray.tolist()
savetxt('NNweights_h1.rtf', result, fmt='%10.8f', delimiter='\r', newline='\r')
     
print('Saving NNbiases_b1.rtf')  
result= [1,biases_b1.shape[0]] + biases_b1.tolist()
savetxt('NNbiases_b1.rtf', result, fmt='%10.8f', delimiter='\r', newline='\r')

print('Saving NNweights_out.rtf')  
tmpArray = reshape(weights_out, (weights_out.shape[0] * weights_out.shape[1],))
result= [weights_out.shape[0],weights_out.shape[1]] + tmpArray.tolist()
savetxt('NNweights_out.rtf', result, fmt='%10.8f', delimiter='\r', newline='\r')

print('Saving NNbiases_out.rtf')  
result= [1,biases_out.shape[0]] + biases_out.tolist()
savetxt('NNbiases_out.rtf', result, fmt='%10.8f', delimiter='\r', newline='\r')

print('Model saved.')