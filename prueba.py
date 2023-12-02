import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

# Cargar datos
df = pd.read_csv('iris_test.csv', sep=',', header=0)

# División de datos
features = ['sepal_length', 'sepal_width', 'petal_length', 'petal_width']
label = 'species'

X = df[features]
y = df[label]

# Dividir en conjuntos de entrenamiento y prueba
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Modelo de regresión lineal
model = LinearRegression()
model.fit(X_train, y_train)

# Predicción del valor faltante
# En este ejemplo, tomo la primera fila del conjunto de prueba para ilustrar la predicción
new_data = X_test.iloc[0, :].values.reshape(1, -1)
predicted_species = model.predict(new_data)

print(f'Predicción para la primera fila: {predicted_species}')
