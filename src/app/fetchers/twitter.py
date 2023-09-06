"""
Filename        :   fetcher.py
Description     :   This file has a function that make request to the external api
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""

import requests
from requests.exceptions import Timeout
from flask import jsonify
from app.secrets import secrets

token = secrets.get('TWITTER_API_BEARER_KEY')
access_token = secrets.get('TWITTER_API_ACCESS_TOKEN')
twitter_base_api = 'https://api.twitter.com'
headersAuth = {
  'Authorization': f'Bearer {token}',
}


def fetch_twitter_followers():
    """
    Fetches the list of followers from twitter
    :param params: this is the keyword to query
    :return : the json data response if available or an error
    """
    print(headersAuth)
    try:
      # make a call to the external api and get the response
      response = requests.get(f'{twitter_base_api}/2/users/@DeeMaejor/followers', headers=headersAuth, timeout=4).json()

      # validate we got available result and return it otherwise 
      # if response['Result']['Total'] > 0:
      #   return jsonify({
      #       "status": 200,
      #       "data": {
      #         "records": response['Result']['Resources']['Resource'],
      #         "totalRecordsCount": response['Result']['Total']
      #       }
      #   })
      # else:
      return response
    # jsonify({
    #     "status": 200,
    #     "data": response
    #   })
    except Timeout:
      return jsonify({
            "status": 408,
            "data": "The request has timeout"
        })