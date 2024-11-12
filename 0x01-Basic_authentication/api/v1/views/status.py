from flask import jsonify
from . import app_views  # Assuming app_views is defined in __init__.py in the same directory

@app_views.route('/api/v1/status', methods=['GET'])
def status():
    """Return API status"""
    return jsonify({"status": "OK"})
