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

# Instantiiere MLP Classifier
# mlp = skl_nn.MLPClassifier(hidden_layer_sizes=(50,), max_iter=50, verbose=1, random_state=1)
# mlp = skl_nn.MLPClassifier(hidden_layer_sizes=(10,), max_iter=5, verbose=1, random_state=1)

# Training
# mlp.fit(data_train,labels_train)
# print("Training set score", mlp.score(data_train, labels_train))
# print("Testing set score", mlp.score(data_test, labels_test))

# Speichere Netzwerk auf der Platte
# pickle.dump(mlp, open("MLP_classifier", 'wb'))

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
