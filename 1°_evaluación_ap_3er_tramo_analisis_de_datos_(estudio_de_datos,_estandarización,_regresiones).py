"""1°_Evaluación_AP_3er_tramo_Analisis_de_datos_(Estudio_de_datos,_Estandarización,_regresiones).ipynb


**Carga de Datos**
Usaremos el Dataset `housing.csv` de [Censo California](https://www.kaggle.com/datasets/camnugent/california-housing-prices)
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from google.colab import drive

drive.mount('/content/drive')
pathCurso = '/content/drive/MyDrive/AP_UNdeC/Data/'
ruta_archivo = pathCurso + "housing.csv"

df = pd.read_csv(ruta_archivo)

"""**Acciones necesarias**

   - Rellenar los valores faltantes con la media de la variable. (OK)

  - Estandarizar las variables numéricas con StandardScaler(). Recuerda dropear la variable categórica. (OK)

  - Codificar la variable categórica con OneHotEncoder(). (OK)

  - Unificar los datos en un único dataframe distinto del original. (OK)
"""

df.isna().sum()

valor_promedio = int(df['total_bedrooms'].mean())
df['total_bedrooms'].fillna(valor_promedio, inplace = True)

df.isna().sum()

df_copy = df.copy()

del df_copy['ocean_proximity']

from sklearn.preprocessing import StandardScaler
escalador = StandardScaler()
df_copy.iloc[:,:] = escalador.fit_transform(df_copy)

from sklearn.preprocessing import OneHotEncoder
codificador = OneHotEncoder()
matriz = codificador.fit_transform(df[['ocean_proximity']]).toarray()
matriz_codificada = pd.DataFrame(matriz,columns = codificador.categories_[0],dtype = int)
data = pd.concat([df_copy, matriz_codificada],axis = 1)

del data['latitude']
del data['longitude']

"""**Entrenamiento y Testeo**

Considera dividir el dataset, con un 20 % de elementos para el testeo, como así también usar una semilla con valor de 42 para la aleatoriedad.
"""

y = data['median_house_value']
x = data.loc[::, data.columns != 'median_house_value']

from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test = train_test_split(x,y,test_size = 0.2, random_state = 42)

from sklearn.metrics import r2_score, mean_squared_error, mean_absolute_error
results_test = pd.DataFrame(columns = ['Modelo',"root_mean_squared_error",'mean_absolute_error',"r2_score"])

"""**DecisionTreeRegressor**

Crea un árbol de decisión que permita realizar una regresión que tenga como máximo 5 de profundidad del árbol y el número mínimo de muestras necesarias para dividir un nodo interno sea de 20, además considera que la semilla de aleatoriedad tenga un valor de 20.
"""

from sklearn.tree import DecisionTreeRegressor
arbol_de_decision = DecisionTreeRegressor(max_depth = 5, min_samples_split = 20, random_state = 42)

arbol_de_decision.fit(x_train, y_train)

preds_tree = arbol_de_decision.predict(x_test)
print(r2_score(y_test, preds_tree))

resultado_parcial = {"Modelo":"DecisionTreeRegressor",
"root_mean_squared_error":mean_squared_error(y_test, preds_tree, squared=False),
"mean_absolute_error":mean_absolute_error(y_test, preds_tree),
"r2_score":r2_score(y_test, preds_tree)
}
results_test = results_test.append(resultado_parcial,
            ignore_index = True)

results_test

"""**LinearRegressor**

Crea un Regresor Lineal, con valores por defecto, para poder aproximar el valor de la vivienda
"""

from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)
print(r2_score(y_test, y_pred))

resultado_parcial = {"Modelo":"LinearRegression",
"root_mean_squared_error":mean_squared_error(y_test, y_pred, squared=False),
"mean_absolute_error":mean_absolute_error(y_test, y_pred),
"r2_score":r2_score(y_test, y_pred)
}
results_test = results_test.append(resultado_parcial,
            ignore_index = True)

results_test

model.intercept_

len(model.coef_)

model.coef_

"""**Máquina de Soporte Vectorial**

Crea un SVR con valores por defecto
"""

from sklearn.svm import  SVR
model = SVR()
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

resultado_parcial = {"Modelo":"SVR",
"root_mean_squared_error":mean_squared_error(y_test, y_pred, squared=False),
"mean_absolute_error":mean_absolute_error(y_test, y_pred),
"r2_score":r2_score(y_test, y_pred)
}
results_test = results_test.append(resultado_parcial,
            ignore_index = True)

results_test

"""**Random Forest Regressor**

Crea un bósque aleatorio, con un máximo de 15 en el parámetro max_depth, y una semilla con valor de 20
"""

from sklearn.ensemble import RandomForestRegressor
model = RandomForestRegressor(max_depth = 15, random_state = 20)
model.fit(x_train,y_train)
y_pred = model.predict(x_test)

print(r2_score(y_test, y_pred))
print(mean_squared_error(y_test, y_pred, squared=False))
print(mean_absolute_error(y_test, y_pred))

resultado_parcial = {"Modelo":"RandomForestRegressor",
"root_mean_squared_error":mean_squared_error(y_test, y_pred, squared=False),
"mean_absolute_error":mean_absolute_error(y_test, y_pred),
"r2_score":r2_score(y_test, y_pred)
}
results_test = results_test.append(resultado_parcial,
            ignore_index = True)

results_test