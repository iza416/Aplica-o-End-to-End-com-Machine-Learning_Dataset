import pandas as pd
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
import joblib

print("[1] Carregando o Credit Card Fraud Dataset...")
df = pd.read_csv("card_transdata.csv")
print(f"[2] Dataset carregado com sucesso!")

df_clean = df.dropna().copy()

features = [
    'distance_from_home',
    'distance_from_last_transaction',
    'ratio_to_median_purchase_price',
    'repeat_retailer',
    'used_chip',
    'used_pin_number',
    'online_order'
]

X = df_clean[features]  # variáveis independentes
y = df_clean['fraud']   # Target: 0 = legítima ou 1 = fraude

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

model = DecisionTreeClassifier(
    max_depth=5, 
    min_samples_leaf=20, 
    random_state=42
)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)
acc = accuracy_score(y_test, y_pred)
print(f"Árvore treinada! Acurácia de teste: {acc * 100:.2f}%\n")

print("Relatório detalhado de métricas:")
print(classification_report(y_test, y_pred, target_names=["Legítima (0)", "Fraude (1)"]))

model_filename = 'fraud_model.pkl'
joblib.dump(model, model_filename)
print(f" Modelo salvo com sucesso em '{model_filename}'!")