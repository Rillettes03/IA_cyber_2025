import re
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
import joblib
import json
import random
from tqdm import tqdm

# Step 1: Load Logs from JSON Files
print("Loading logs...")
with open(r'C:\Users\vixis\Desktop\Work\Codespython\AI ELK\logs.json', 'r') as f:
    benign_logs = json.load(f)

with open(r'C:\Users\vixis\Desktop\Work\Codespython\AI ELK\malice.json', 'r') as f:
    malicious_logs = json.load(f)
print("Logs loaded successfully.")

# Extract relevant fields
print("Extracting relevant fields from logs...")
benign_df = pd.DataFrame([{ 'message': log['message'], 'timestamp': log['@timestamp'] } for log in tqdm(benign_logs)])
malicious_df = pd.DataFrame([{ 'message': log['message'], 'timestamp': log['@timestamp'] } for log in tqdm(malicious_logs)])
print("Field extraction complete.")

# Label logs (benign = 0, malicious = 1)
print("Labeling logs...")
benign_df['label'] = 0
malicious_df['label'] = 1
print("Logs labeled.")

# Combine and shuffle logs
print("Combining and shuffling logs...")
combined_df = pd.concat([benign_df, malicious_df], ignore_index=True)
combined_df = combined_df.sample(frac=1, random_state=42).reset_index(drop=True)
print("Logs combined and shuffled.")

# Step 2: Preprocess Logs
print("Preprocessing logs...")
def preprocess_logs(logs):
    return logs.apply(lambda x: re.sub(r'[^a-zA-Z0-9 ]', '', x))

combined_df['log_message'] = preprocess_logs(combined_df['message'])
print("Preprocessing complete.")

# Step 3: Feature Extraction
print("Extracting features with CountVectorizer...")
vectorizer = CountVectorizer()
X = vectorizer.fit_transform(tqdm(combined_df['log_message']))
y = combined_df['label']
print("Feature extraction complete.")

# Step 4: Train-Test Split
print("Splitting data into train and test sets...")
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)
print("Data split complete.")

# Step 5: Model Training
print("Training the model...")
model = LogisticRegression()
model.fit(X_train, y_train)
print("Model training complete.")

# Step 6: Evaluate Model
print("Evaluating the model...")
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))

# Save Model and Vectorizer
print("Saving model and vectorizer...")
joblib.dump(model, 'syslog_classifier_model.pkl')
joblib.dump(vectorizer, 'vectorizer.pkl')
print("Model and vectorizer saved.")
