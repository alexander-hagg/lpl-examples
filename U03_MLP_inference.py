# Importiere benötigte Bibliotheken
import sklearn.datasets as skl_data
import sklearn.neural_network as skl_nn
import pickle
import matplotlib.pyplot as plt

# Datenimport (MNIST Datensatz)
data, labels = skl_data.fetch_openml('mnist_784', version=1, return_X_y=True)

# Normalisierung
data = data / 255.0
# print(data.describe)

# Datensplit
data_train = data[0:63000]
labels_train = labels[0:63000]
data_test = data[63001:]
labels_test = labels[63001:]

# INFERENZ auf RASPBERRY
# Trainiertes Netzwerk wieder einlesen
mlp = pickle.load(open("MLP_classifier", 'rb'))

# Inferenz mit MLP Modell
test_digit = data_test.iloc[0].to_numpy()
test_digit_prediction = mlp.predict(test_digit.reshape(1,784))
print("Predicted value",test_digit_prediction)
print("Actual value",labels_test.iloc[0])

fig, ax = plt.subplots(nrows=1, ncols=1, figsize=(28, 28))
ax.imshow(test_digit.reshape(28,28), cmap='gray')
ax.axis('off')
plt.show()
