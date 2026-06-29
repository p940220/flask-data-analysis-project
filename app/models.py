from . import db
from datetime import datetime

class ScrapedData(db.Model):
    __tablename__ = 'scraped_data' 
    
    # ✨ 修改這裡：暫時把 title 當作 primary_key，並移除 id
    title = db.Column(db.String(200), primary_key=True)
    like_count = db.Column(db.Integer)
    url = db.Column(db.String(500))
    crawl_date = db.Column(db.DateTime, default=datetime.utcnow)