Tools und Daten für das neuronale Netzwerk des BrickClassifi3r Lego Mindstorms EV3 roboter
(see English version below)

Voraussetzungen auf dem PC
1. Ein 64bit Windows PC mit Windows 7 oder höher.

2. Python 3.5.2 (64 bit Version) (Click "Add Python 3.5 to path" im installation dialog)
   Download-Adresse: 
   https://www.python.org/ftp/python/3.5.2/python-3.5.2-amd64.exe

3. Library "TensorFlow" (1.1 oder höher)
   Installation mit der Eingabeaufforderung:
   pip3 install --ignore-installed --upgrade tensorflow

Das Trainingsprogramm:  train_NN.py (Version 1.1)
Dieses Programm dient zum Training des neuronalen Netzes auf dem PC. 
Es muss im gleichen Ordner liegen wie die folgenden 4 Dateien:
   xTrain_TwoCubesCylinder375-24.csv
   yTrain_TwoCubesCylinder375-3.csv
   xTest_TwoCubesCylinder300-24.csv
   yTest_TwoCubesCylinder300-3.csv
Das Programm wird gestartet mit: : python train_NN.py
Folgende Modelldateien werden erzeugt: 
   NNbiases_b1.csv
   NNbiases_out.csv
   NNweights_h1.csv
   NNweights_out.csv
sowie die Modelldateien für den Lego Mindstorm EV3 roboter
   NNbiases_b1.rtf
   NNbiases_out.rtf
   NNweights_h1.rtf
   NNweights_out.rtf
Vorhandene Dateien werden überschrieben.

Installation der Modelldateien auf dem BrickClassifi3r EV 3 Lego Roboter: 
Verwenden sie den Speicher-Browser der Lego-Entwicklungsumgebung, um die 
4 rtf-Dateien in das Projektverzeichnis der BrickClassifi3r-Anwendung zu kopieren.
Die Trainingsdateien wurden mit Objekten aus roten Legosteinen erstellt. 

Utility predict.py
Verwenden sie dieses Programm, um einzelne Merkmalsvektoren mit dem neuronlen Netz
mit Hilfe des Modells (CSV-Dateien) auf dem PC zu klassifizieren. 
   
--Englsh version--
Tools and data for the neural network of the BrickClassifi3r Lego Mindstorms EV3 roboter. 

Prerequisites on the PC
1. A 64bit Windows PC with Windows 7 or higher.

2. Python 3.5.2 (64 bit Version) (Click "Add Python 3.5 to path" on the installation dialog)
   Download-Address: 
   https://www.python.org/ftp/python/3.5.2/python-3.5.2-amd64.exe

3. Library "TensorFlow" (1.1 or higher)
   Installation with a console dialog:
   pip3 install --ignore-installed --upgrade tensorflow

The training program:  train_NN.py (Version 1.1)
This program is used for the training of the neural network. 
It has to be in the same directory of the PC like the following 4 files:
   xTrain_TwoCubesCylinder375-24.csv
   yTrain_TwoCubesCylinder375-3.csv
   xTest_TwoCubesCylinder300-24.csv
   yTest_TwoCubesCylinder300-3.csv
Run it with: python train_NN.py
The resulting model files are: 
   NNbiases_b1.csv
   NNbiases_out.csv
   NNweights_h1.csv
   NNweights_out.csv
as well as the model files for the  Lego Mindstorm EV3 roboter
   NNbiases_b1.rtf
   NNbiases_out.rtf
   NNweights_h1.rtf
   NNweights_out.rtf
Existing files are deleted.

Installation of the model on the BrickClassifi3r EV 3 Lego roboter: 
Use the memory-browser to put the 4 rtf-Files into the project directory of
the BrickClassifi3r_V1 application. 
The training data was created with objects built with red lego bricks.
   

Utility predict.py
Use this program to classify single feature vectors with the neural network 
using the *.csv model files on the PC. 
 

