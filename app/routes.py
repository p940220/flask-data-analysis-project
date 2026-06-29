from flask import Blueprint, render_template
from .models import ScrapedData
from . import db
import numpy as np

main_bp = Blueprint('main', __name__)

@main_bp.route('/')
def index():
    try:
        # 從資料庫抓取最新的 15 筆資料
        data = ScrapedData.query.order_by(ScrapedData.crawl_date.desc()).all()
        
        print(f"DEBUG: 從資料庫抓到了 {len(data)} 筆資料") # 這會印在 CMD 視窗
        
        # 數學分析邏輯
        likes = [d.like_count for d in data if d.like_count is not None]
        if likes and len(likes) >= 2:
            cv = np.std(likes) / np.mean(likes) if np.mean(likes) > 0 else 0
            label = "山型人 (爆發力強)" if cv > 0.5 else "谷型人 (穩定度高)"
            cv_score = round(cv, 2)
        else:
            label, cv_score = "資料累積中...", 0
            
        return render_template('index.html', data=data, label=label, cv_score=cv_score)
    except Exception as e:
        print(f"DEBUG: 網頁抓取資料出錯: {e}")
        return f"資料庫讀取錯誤: {e}"