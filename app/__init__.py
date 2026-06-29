from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    # ✨ 暴力法：直接寫死網址
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://my_project_db_m7qy_user:Q9YGyKC8AtCYFyebVmyHdUtWFEOa6Yq6@dpg-d900fq80697c73egdne0-a.ohio-postgres.render.com/my_project_db_m7qy"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'dev_secret_key'

    db.init_app(app)


    from .routes import main_bp
    app.register_blueprint(main_bp)

    return app
