from . import db
from datetime import datetime
class ScrapedData(db.Model):
    __tablename__ = 'scraped_data'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    content = db.Column(db.Text)
    url = db.Column(db.String(255))
    crawl_date = db.Column(db.DateTime, default=datetime.utcnow)
    category = db.Column(db.String(100))
class AnalysisResult(db.Model):
    __tablename__ = 'analysis_results'
    id = db.Column(db.Integer, primary_key=True)
    scraped_data_id = db.Column(db.Integer, db.ForeignKey('scraped_data.id'))
    analysis_type = db.Column(db.String(100))
    result_label = db.Column(db.String(100))
    score = db.Column(db.Float)
    analysis_date = db.Column(db.DateTime, default=datetime.utcnow)
