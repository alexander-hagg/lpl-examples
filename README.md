# lpl-examples

Montag:
U01_Kameradaten.py
U02_Segmentierung.py

Dienstag:
U03_MLP_training.py > Ausführen auf PC, Laptop, Cloud
U03_MLP_inference.py > Ausführen auf Raspberry PI

## Verwendete Bibliotheken:
Zeitoperationen (Schlafmodus für Loops)
from time import sleep

Kameraimport für Raspberry Camera Module
from picamera import PiCamera

Plottingbibliothek, ähnelt Matlab's Plots
import matplotlib.pyplot as plt

Scikit image Segmentierungsalgorithmen
import skimage.segmentation as seg

Scikit image Farboperationen
import skimage.color as color

Scikit image Interaktion mit Daten auf Disk (input, output)
from skimage import io

Datensätze laden von scikit-learn
import sklearn.datasets as skl_data

Neuronale Netzwerke mit scikit-learn
import sklearn.neural_network as skl_nn

Saving and loading objects to disk from Python
import pickle 
