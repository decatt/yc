from dataloader import ExcelDataLoader
# pip install xgboost scikit-learn
import xgboost as xgb
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report, roc_auc_score
#回归任务，特征数量21，输出1，数据总量 893
if __name__ == "__main__":
    loader = ExcelDataLoader(file_path="data.xlsx")
    # 特征形状: (893, 21), 标签形状: (893,)
    if loader.load_data() and loader.preprocess_data():
        x, y = loader.get_train_data()  

        
