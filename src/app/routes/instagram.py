"""
Filename        :   instagram.py
Description     :   This file contains the whole all the routes
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""
from datetime import timedelta
import time

from flask import (jsonify, request, make_response, Blueprint)
from ..fetchers.platforms.instagram import fetch_instagram_followers

instagram = Blueprint('instagram', __name__, url_prefix='/api/v1/instagram')


@instagram.route("/followers", methods=['GET'])
def get_twitter_followers():
    """
    This route invoke the fetch_instagram_followers and returns the list of followers data.

    Returns:
    followers_list: The list of followers.
    """
    response = fetch_instagram_followers()

    return jsonify({
        "data": response,
        "status": 200
    })
