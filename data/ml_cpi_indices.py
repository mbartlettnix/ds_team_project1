import pandas as pd
import numpy as np
import os
from sklearn import model_selection
from sklearn.linear_model import LinearRegression
from sklearn.externals import joblib

"""
for using this machine learning classifier you will need to input three features into the model. Those features are 'restaurant_price_index', 'rent_index', 'groceries_index'
"""

df = pd.read_csv('numbeo_ds_indices.csv')

for filename in os.listdir('./indices/nearby_cities/'):
    df_append = pd.read_csv('./indices/nearby_cities/{}'.format(filename))
    df = df.append(df_append, ignore_index=True)

ml_df = df[['cpi_index', 'restaurant_price_index', 'rent_index', 'groceries_index']]

ml_df.dropna(inplace=True)

X = np.array(ml_df.drop(['cpi_index'], axis=1))
y = np.array(ml_df['cpi_index'])

X_train, X_test, y_train, y_test = model_selection.train_test_split(X, y)

clf = LinearRegression()
clf.fit(X_train, y_train)

# r_squared value when tested on 20180114 23:45PCT was 0.961318689059 PASSED
r_squared = clf.score(X_test, y_test)

# to save model pickle
joblib.dump(clf, 'cpi_index.pkl')

# to load and use model pickle
clf = joblib.load('cpi_index.pkl')
check = 'insert the 3 required features, read __doc__'

clf.predict(check)
