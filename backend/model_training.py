```python
from sklearn.model_selection import GridSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import f1_score, precision_score, recall_score
from sklearn.model_selection import cross_val_score
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense
from tensorflow.keras.wrappers.scikit_learn import KerasClassifier
import numpy as np
import pandas as pd

def create_cnn_model():
    model = Sequential()
    model.add(Conv2D(32, (3, 3), activation='relu', input_shape=(64, 64, 3)))
    model.add(MaxPooling2D(pool_size=(2, 2)))
    model.add(Flatten())
    model.add(Dense(128, activation='relu'))
    model.add(Dense(1, activation='sigmoid'))
    model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])
    return model

def trainModel():
    # Load preprocessed data
    data = pd.read_csv('preprocessed_data.csv')
    X = data.drop('label', axis=1)
    y = data['label']

    # Decision Tree
    dt_params = {'max_depth': [10, 20, 30, None], 'min_samples_split': [2, 5, 10]}
    dt_grid = GridSearchCV(DecisionTreeClassifier(), dt_params, cv=10, scoring='accuracy')
    dt_grid.fit(X, y)

    # Random Forest
    rf_params = {'n_estimators': [10, 50, 100, 200], 'max_depth': [10, 20, 30, None], 'min_samples_split': [2, 5, 10]}
    rf_grid = GridSearchCV(RandomForestClassifier(), rf_params, cv=10, scoring='accuracy')
    rf_grid.fit(X, y)

    # CNN
    cnn_model = KerasClassifier(build_fn=create_cnn_model, epochs=10, batch_size=10)
    cnn_scores = cross_val_score(cnn_model, X, y, cv=10, scoring='accuracy')

    # Evaluation
    dt_f1 = f1_score(y, dt_grid.predict(X))
    dt_precision = precision_score(y, dt_grid.predict(X))
    dt_recall = recall_score(y, dt_grid.predict(X))

    rf_f1 = f1_score(y, rf_grid.predict(X))
    rf_precision = precision_score(y, rf_grid.predict(X))
    rf_recall = recall_score(y, rf_grid.predict(X))

    cnn_f1 = f1_score(y, np.round(cnn_model.predict(X)))
    cnn_precision = precision_score(y, np.round(cnn_model.predict(X)))
    cnn_recall = recall_score(y, np.round(cnn_model.predict(X)))

    print('Decision Tree - F1: {}, Precision: {}, Recall: {}'.format(dt_f1, dt_precision, dt_recall))
    print('Random Forest - F1: {}, Precision: {}, Recall: {}'.format(rf_f1, rf_precision, rf_recall))
    print('CNN - F1: {}, Precision: {}, Recall: {}'.format(cnn_f1, cnn_precision, cnn_recall))

    # Save models
    joblib.dump(dt_grid.best_estimator_, 'decision_tree_model.pkl')
    joblib.dump(rf_grid.best_estimator_, 'random_forest_model.pkl')
    cnn_model.model.save('cnn_model.h5')

if __name__ == "__main__":
    trainModel()
```