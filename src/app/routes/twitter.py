"""
Filename        :   routes.py
Description     :   This file contains the whole all the routes
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""
from datetime import timedelta
import time
from flask import (jsonify, request, make_response, Blueprint)
from app.fetchers.twitter import fetch_twitter_followers

twitter = Blueprint('twitter', __name__, url_prefix='/api/v1/twitter')

@twitter.route("/followers", methods=['GET'])
def get_twitter_followers():
    """
    Fetches data from the twitter account
    :params keyword: this is the keyword to query
    :return : the response from the invoked function
    """
    response = fetch_twitter_followers()

    print("responsee::: ", response)
    return jsonify({
            "status": 200,
            "data": "response"
        })
