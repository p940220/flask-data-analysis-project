from flask import Blueprint, render_template
main_bp = Blueprint('main', __name__)
@main_bp.route('/')
def index():
    return render_template('index.html')
@main_bp.route('/analysis')
def analysis():
    return render_template('analysis.html')
