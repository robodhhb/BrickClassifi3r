#####################################################
# Trainingsprogramm für das neuronale Netz des
# BrickClassifi3r Roboters mit Hilfe von TensorFlow
# 
# Autor: Detlef Heinze 
# Version: 1.2
#####################################################
import tensorflow as tf  
from numpy import loadtxt, savetxt, reshape 
import datetime as dt

#Abschalten der Warnmeldungen von TensorFlow, die
#melden, dass die TensorFlow-Library nicht 
#alle Eigenschaften dieser HW nutzt.
import os
os.environ['TF_CPP_MIN_LOG_LEVEL']='2'

print('Training eines Neuronalen Netzes(V1.2)\n')
print('TensorFlow Version: ' + tf.__version__)
start= dt.datetime.now()

# Step 1: Import Training Data (xTrain und yTrain)
print('Lese xTrain- und yTrain-Daten')
xTrain= loadtxt('xTrain_TwoCubesCylinder375-24.csv')
yTrain= loadtxt('yTrain_TwoCubesCylinder375-3.csv')

# Step 2: Import Test Data (xTest und yTest)
print('Lese xTest und yTest-Daten')
xTest= loadtxt('xTest_TwoCubesCylinder300-24.csv')
yTest= loadtxt('yTest_TwoCubesCylinder300-3.csv')

# Step 3: Definition der Lernparameter
learning_rate = 0.001
num_epochs = 250
num_examples= xTrain.shape[0]
print('Anzahl der Trainingdaten: '+repr(num_examples))
print('Anzahl der Testdaten: ' + repr(xTest.shape[0]))

#Parameter für das 24 - 6 - 3 neuronale Netz
n_input = 24   #24 Neuronen für die gemessene Daten
n_hidden_1 = 6 #Größe der versteckten Neuronenschicht
n_classes = 3  #Größe der ausgebenden Neuronenschicht
               #ist gleich der Anzahl der Klassen
print('NN-Architektur: ' + repr(n_input) +' - ' 
      + repr(n_hidden_1) + ' - ' 
      + repr(n_classes))

# Platzhalter im TensorFlow-Graph 
x = tf.placeholder("float", shape=(None, n_input))
y = tf.placeholder("float", shape=(None, n_classes))

# Step 4: Berechnungsschritte des NN festlegen
def multilayer_perceptron(x, weights, biases):
    # Die versteckte Schicht mit  RELU-Aktivierung
    layer_1 = tf.add(tf.matmul(x, weights['h1']), biases['b1'])
    layer_1 = tf.nn.relu(layer_1)
  
    # Die Ausgabeschicht mit linearer Aktivierung
    out_layer = tf.matmul(layer_1, weights['out'])+biases['out']
    return out_layer

# Step 5: Initialisiere Model mit Zufallszahlen
weights = {
    'h1': tf.Variable(tf.random_normal([n_input, n_hidden_1])),
    'out': tf.Variable(tf.random_normal([n_hidden_1,n_classes]))
}
biases = {
    'b1': tf.Variable(tf.random_normal([n_hidden_1])),
    'out': tf.Variable(tf.random_normal([n_classes]))
}

# Step 6: Maschinelles Lernen vorbereiten
# Platzhalter für x und Anfangsmodell übergeben
predict = multilayer_perceptron(x, weights, biases)

# Kosten und den Optimizer definieren 
# Ab TensorFlow Version 1.5 modifizierte softmax-Methode verwenden)
if tf.__version__ < '1.5':
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=predict, labels=y))
else:
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=predict, labels=y))

optimizer =tf.train.AdamOptimizer(learning_rate=learning_rate).minimize(cost)

# Variablen von tf initialisieren
init = tf.global_variables_initializer()

#Step 7: Training
print('\n-------------Trainingsphase-----------------')
with tf.Session() as sess:
    sess.run(init)
    for i in range(num_epochs):
        for j in range(num_examples):
            _, c = sess.run([optimizer, cost], 
                            feed_dict={x: [xTrain[j]],
                                       y: [yTrain[j]]})
        if i % 25 == 0:
            print('epoch {0}: cost = {1}'.format(i, c))
    print('epoch {0}: cost = {1}'.format(i, c))
    print('Training beendet.')
    duration = (dt.datetime.now() - start)
    print("Dauer: " + str(duration))
    
#Step 8: Berechnung der Treffsicherheit anhand der Testdaten
    correct_prediction = tf.equal(tf.argmax(predict, 1), tf.argmax(y, 1))
    accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
    print('Testergebnis:', accuracy.eval({x: xTest, 
                                          y: yTest}))
#Step 9: Ausgabe des berechneten Models
    print('\n-----------------Modelübersicht----------------------')
    print('Weights für h1')
    wh1= weights['h1'].eval(sess)
    print(wh1)
    print('\nBiases für b1')
    bb1= biases['b1'].eval(sess)
    print(bb1)
    print('\nWeights für out')
    wo= weights['out'].eval(sess)
    print(wo)
    print('\nBiases für out')
    bo= biases['out'].eval(sess)
    print(bo)

#Step 10: Sicherung des berechneten Models als csv und rtf
    print('\n--------------Model wird gespeichert(csv)-------------')
    print('Sichere Weights für h1: NNweights_h1.csv')
    savetxt('NNweights_h1.csv', wh1, fmt='%10.8f', delimiter=' ')
    print('Sichere Biases für b1: NNbiases_b1.csv')
    savetxt('NNbiases_b1.csv', bb1, fmt='%10.8f', delimiter=' ')
    print('Sichere Weights für out: NNweights_out.csv')
    savetxt('NNweights_out.csv', wo, fmt='%10.8f', delimiter=' ')
    print('Sichere Biases für out: NNbiases_out.csv')
    savetxt('NNbiases_out.csv', bo, fmt='%10.8f', delimiter=' ')

    print('\n--Model wird gespeichert(rtf für Lego Mindstorms EV3)--')
    #Format: <Anzal Zeilen>CR<Anzahl Spalten>CR<{<aReal>CR}*
    print('Sichere Weights für h1: NNweights_h1.rtf')  
    tmpArray = reshape(wh1, (wh1.shape[0] * wh1.shape[1],))
    result= [wh1.shape[0],wh1.shape[1]] + tmpArray.tolist()
    savetxt('NNweights_h1.rtf', result, fmt='%10.8f', delimiter='\r', newline='\r')
     
    print('Sichere Biases für b1: NNbiases_b1.rtf')  
    result= [1,bb1.shape[0]] + bb1.tolist()
    savetxt('NNbiases_b1.rtf', result, fmt='%10.8f', delimiter='\r', newline='\r')

    print('Sichere Weights für out: NNweights_out.rtf')  
    tmpArray = reshape(wo, (wo.shape[0] * wo.shape[1],))
    result= [wo.shape[0],wo.shape[1]] + tmpArray.tolist()
    savetxt('NNweights_out.rtf', result, fmt='%10.8f', delimiter='\r', newline='\r')

    print('Sichere Biases für out: NNbiases_out.rtf')  
    result= [1,bo.shape[0]] + bo.tolist()
    savetxt('NNbiases_out.rtf', result, fmt='%10.8f', delimiter='\r', newline='\r')

    print('Model gesichert. Programmende.')
