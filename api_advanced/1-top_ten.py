#!/usr/bin/python3
"""
Query Reddit API for titles of top ten posts of a given subreddit
"""
import requests
import json
import sys  # Import sys to access command line arguments


def top_ten(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'alu-scripting/1.0 (by /u/my_reddit_username)'} # Replace with your info

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])  # Print the titles ONLY

    except Exception: # Catch any exception and ignore
       pass



if __name__ == "__main__":
    if len(sys.argv) > 1:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
