"""
Filename        :   instagram.py
Description     :   This file has a method that returns instagram followers
Author          :   Legacy Dev Team
Email           :   [muhammad.sesay@legacynetwork.io, ]
Started writing :   30.08.2023
Completed on    :   in progress
"""

import json
import datetime


def fetch_instagram_followers():
    """
    This method reads the followers file, iterate over it, get the data and return the list.

    Parameters: None
    a (int): The first number.
    b (int): The second number.

    Returns:
    followers_list: The list of followers.
    """

    # Opening JSON file
    with open('src/app/data/instagram_followers.json') as followers_file:
        file_contents = followers_file.read()

    # parse the json file into python dictionary
    parsed_json = json.loads(file_contents)

    # will hold the list that will be return
    followers_list = []

    # iterate over the parsed json
    for data in parsed_json:
        # get the first item from the list
        follower = data["string_list_data"][0]

        # convert the followed timestamp into a string
        follower["timestamp"] = f'{datetime.datetime.fromtimestamp(follower["timestamp"])}'

        # append the object to the returning list
        followers_list.append(follower)

    return followers_list
