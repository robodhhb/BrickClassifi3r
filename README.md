# BrickClassifi3r
Software for the BrickClassifi3r Lego Mindstorms EV3 robot

Willkommen beim BrickClassifi3r Roboter!
(see English version below)

Dieser Lego Mindstorms EV3 Roboter verwendet ein neuronales Netz, um ein Kubus, ein Zylinder oder ein kleinen Kubus
zu erkennen, der auf ein Transportband gelegt wurde. Ein Video zeigt, wie der Roboter funktioniert. Jedes Objekt, das 
auf das Transportband gelegt wird, wird von einem IR-Sensor für eine Sekunde alle 40ms gescannt. 
Dabei entstehen 24 Entfernungsmesswerte, die eines der drei Objekte repräsentieren.  Diese Daten werden
von einem neuronalen Netz des Roboters innerhalb von ca. 180ms klassifiziert. 
In einem Test mit 300 Testdaten erreichte das neuronale Netz eine Erkennungsquote von 95,6%.
Das neuronale Netz wurde mit der Technik des maschinellen Lernens auf einem PC mit 375 Trainingsdaten 
(125 pro Objekt) trainiert. 
Für weitere Informationen siehe die zwei Ordner in diesem Repository.  

Welcome to the BrickClassifi3r robot!

This Lego Mindstorms EV3 robot uses a neural network to recognize a cube, a cylinder or a small cube put on a conveyor belt. 
See the video how it works. Each object on the conveyor belt is scanned by an IR-sensor every 40ms for about a second. 
The resulting data are 24 distance values representing one of the three objects. 
This data is fed into the neural network on the robot to classify the object within 180ms.
In a test with 300 objects it reaches 95,6% accuracy.
The neural network has been trained before by a machine learning algorithm on a PC using a set of 
375 training examples - 125 examples for each object. 
 
For more information have a look at the two folders: One for the Lego Mindstorms project and the other
for the neural network training on the PC.
 
