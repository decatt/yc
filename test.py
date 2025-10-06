import my_xgboost as xgb
from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, mean_squared_error
import numpy as np

# ==================== CLASSIFICATION EXAMPLE ====================
print("=== Classification Example ===")

# Load data
data = load_breast_cancer()
X, y = data.data, data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Method 1: Using XGBClassifier (scikit-learn API)
model = xgb.XGBClassifier(
    n_estimators=100,      # number of trees
    max_depth=5,           # maximum tree depth
    learning_rate=0.1,     # step size shrinkage
    objective='binary:logistic',
    random_state=42
)

# Train
model.fit(X_train, y_train)

# Predict
y_pred = model.predict(X_test)
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

# Feature importance
print("\nTop 5 Important Features:")
feature_imp = model.feature_importances_
top_features = np.argsort(feature_imp)[-5:]
for idx in reversed(top_features):
    print(f"{data.feature_names[idx]}: {feature_imp[idx]:.4f}")


# ==================== REGRESSION EXAMPLE ====================
print("\n=== Regression Example ===")

# Load data
data = load_diabetes()
X, y = data.data, data.target

# Split data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Using XGBRegressor
reg_model = xgb.XGBRegressor(
    n_estimators=100,
    max_depth=5,
    learning_rate=0.1,
    objective='reg:squarederror',
    random_state=42
)

# Train
reg_model.fit(X_train, y_train)

# Predict
y_pred = reg_model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
print(f"RMSE: {rmse:.4f}")


# ==================== USING NATIVE API (DMatrix) ====================
print("\n=== Using Native XGBoost API ===")

# Create DMatrix (XGBoost's internal data structure)
dtrain = xgb.DMatrix(X_train, label=y_train)
dtest = xgb.DMatrix(X_test, label=y_test)

# Set parameters
params = {
    'max_depth': 5,
    'eta': 0.1,  # learning rate
    'objective': 'reg:squarederror',
    'eval_metric': 'rmse'
}

# Train with evaluation
evals = [(dtrain, 'train'), (dtest, 'test')]
bst = xgb.train(
    params,
    dtrain,
    num_boost_round=100,
    evals=evals,
    early_stopping_rounds=10,
    verbose_eval=False
)

# Predict
y_pred = bst.predict(dtest)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
print(f"RMSE with native API: {rmse:.4f}")


# ==================== CROSS-VALIDATION ====================
print("\n=== Cross-Validation ===")

cv_results = xgb.cv(
    params,
    dtrain,
    num_boost_round=100,
    nfold=5,
    metrics='rmse',
    early_stopping_rounds=10,
    seed=42,
    verbose_eval=False
)

print(f"Best RMSE: {cv_results['test-rmse-mean'].min():.4f}")
print(f"Best iteration: {cv_results['test-rmse-mean'].idxmin() + 1}")
