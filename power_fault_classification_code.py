
# Power System Fault Detection and Classification

## Step 1: Import Libraries
```python
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler, LabelEncoder
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, confusion_matrix, accuracy_score
```

## Step 2: Load Dataset
```python
df = pd.read_csv('/kaggle/input/power-system-faults-dataset/power_system_faults_dataset.csv')
df = df.dropna()
```

## Step 3: Prepare Features and Labels
```python
X = df.drop(columns=["Fault ID"])
y = df["Fault ID"]

# Encode non-numeric columns
for col in X.columns:
    if X[col].dtype == 'object':
        X[col] = LabelEncoder().fit_transform(X[col])

# Encode the labels
label_encoder = LabelEncoder()
y_encoded = label_encoder.fit_transform(y)
```

## Step 4: Train-Test Split and Scaling
```python
X_train, X_test, y_train, y_test = train_test_split(X, y_encoded, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)
```

## Step 5: Train Model
```python
model = RandomForestClassifier(random_state=42)
model.fit(X_train_scaled, y_train)
```

## Step 6: Evaluate
```python
y_pred = model.predict(X_test_scaled)
print(confusion_matrix(y_test, y_pred))
print(classification_report(y_test, y_pred, target_names=label_encoder.classes_))
print("Accuracy:", accuracy_score(y_test, y_pred))
```
