import pandas as pd
import numpy as np

def classify_person_type(data):
    """
    基於數學特徵的分類演算法
    谷型人 (Valley-type): 行為模式呈現週期性低谷或穩定性
    山型人 (Mountain-type): 行為模式呈現突發性高峰或高活躍度
    """
    # 假設 data 是一個包含活躍度分數的 Series
    mean_val = data.mean()
    std_val = data.std()
    
    # 簡單邏輯：變異係數較大的為山型人，較穩定的為谷型人
    cv = std_val / mean_val if mean_val != 0 else 0
    
    if cv > 0.5:
        return "山型人", cv
    else:
        return "谷型人", cv

def process_analysis_results(scraped_df):
    # 範例處理邏輯
    results = []
    for index, row in scraped_df.iterrows():
        # 模擬一些數學特徵
        mock_series = pd.Series(np.random.rand(10))
        label, score = classify_person_type(mock_series)
        results.append({
            "scraped_data_id": row.get('id'),
            "analysis_type": "人格行為分類",
            "result_label": label,
            "score": float(score)
        })
    return pd.DataFrame(results)
