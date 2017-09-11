##################################################
# Anwendung des neuronalen Netzes zu Testzwecken.
# Eingabe ist der feature vektor mit 24 Werten.
#
# Autor: Detlef Heinze
# Version: 1.0
##################################################
import tensorflow as tf
from numpy import loadtxt, savetxt, dtype

# Abschalten der Warnmeldungen von TensorFlow, die
# melden, dass die Tensorflow-Library nicht 
# alle Eigenschaften dieser HW nutzt.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

print('Test eines neuronalen Netzes')

# Step 1: Modell mit Eingabe-, versteckter und 
#         Ausgabeschicht importieren.
#         Importiere 32bit floats.
print('Import des Modells\n')
weights_h1= loadtxt('NNweights_h1.csv', dtype=dtype('f4'))
print('Weights h1: ' + repr(weights_h1.shape))
biases_b1= loadtxt('NNbiases_b1.csv', dtype=dtype('f4'))
print('Biases b1: ' + repr(biases_b1.shape))
weights_out= loadtxt('NNweights_out.csv', dtype=dtype('f4'))
print('Weights out: ' + repr(weights_out.shape))
biases_out= loadtxt('NNbiases_out.csv', dtype=dtype('f4'))
print('Biases out: ' + repr(biases_out.shape))

#Parameter für das 24 - 6 - 3 neuronale Netz
n_input = weights_h1.shape[0]   
n_hidden_1 = weights_h1.shape[1] 
n_classes = weights_out.shape[1]  

print('\nNN-Architektur: ' + repr(n_input) +' - ' 
      + repr(n_hidden_1) + ' - ' 
      + repr(n_classes))

# Platzhalter für den Tensorflow-Graph 
x = tf.placeholder("float", shape=(1, n_input))
y = tf.placeholder("float", shape=(None, n_classes))

# Step 2: Berechnungsschritte des NN festlegen
def multilayer_perceptron(x, weights, biases):
    # Die versteckte Schicht mit  RELU-Aktivierung
    layer_1 = tf.add(tf.matmul(x, weights['h1']),biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
  
    # Die Ausgabeschicht mit linearer Aktivierung
    out_layer = tf.matmul(layer_1,  weights['out']) + biases['out']
    return out_layer

# Step 3: Initialisiere weight & bias mit gelesenem Modell
weights = {
    'h1': tf.Variable(weights_h1),
    'out': tf.Variable(weights_out)
}
biases = {
    'b1': tf.Variable(biases_b1),
    'out': tf.Variable(biases_out)
}

#Step 4 Definiere Beispiele zum Testen
#Example class 0 (Cube)
example= [[24, 24, 21, 18, 16, 14, 14, 12, 10, 9, 7, 6, 6, 6, 6, 6, 7, 7, 8, 8, 10, 12, 14, 14]]

#Example class 1 (Cylinder)
#example= [[23, 23, 21, 18, 16, 15, 15, 14, 13, 13, 13, 12, 12, 12, 12, 13, 13, 13, 14, 15, 16, 18, 21, 21]]

#Example class 2 (Small Cube)
#example= [[24, 24, 21, 19, 18, 17, 17, 15, 14, 14, 13, 13, 13, 14, 15, 15, 18, 18, 20, 23, 26, 31, 36, 36]]

print('Testbeispiel: ' + repr(example))

# Step 5: Setup Modell und initialisiere Variablen
predict = multilayer_perceptron(x, weights, biases)
init = tf.global_variables_initializer()

#Step 6: Klassifiziere das Beispiel mit dem NN
print('\n---------------Klassifizierung------------------')
with tf.Session() as sess:
    sess.run(init)
    #Das Beispiel durch das NN klassifizieren lassen 
    #Ergebnis: Index der größten Zahl ist die Klasse des Beispiel.
    print('Ergebnis: ' + repr(sess.run( [predict],feed_dict={ x: example})))
    #print(sess.run(tf.argmax(predict, 1), feed_dict={x: example}))
