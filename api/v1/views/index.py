#!/usr/bin/python3
"""Create route"""
from flask import Blueprint
from flask import jsonify
from models import storage

app_views = Blueprint('app_views', __name__, url_prefix="/api/v1")


@app_views.route('/status', methods=['GET'], strict_slashes=False)
def status():
    """Returns json object"""
    return jsonify({"status": "OK"})


@app_views.route('/stats', methods=['GET'], strict_slashes=False)
def stats():
    """Retrieves the number of each objects by type"""
    cls = ['Amenity', 'City', 'Place', 'Review', 'State', 'User']
    idx = 0
    count = []
    while idx < len(cls):
        count.append(storage.count(cls[idx]))
        idx += 1
    return jsonify(
        {"amenities": count[0], "cities": count[1], "places": count[2],
         "reviews": count[3], "states": count[4], "users": count[5]}
    )
