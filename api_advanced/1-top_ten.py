#!/usr/bin/python3

import requests

def top_ten(subreddit):
    """Queries the Reddit API and prints the titles of the first 10 hot posts for a given subreddit."""

    # Reddit API URL for getting hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"

    # Send GET request to Reddit API
    headers = {'User-Agent': 'python3:redditapi:v1.0 (by /u/yourusername)'}
    response = requests.get(url, headers=headers, allow_redirects=False)

    # If the subreddit is invalid or response code is not 200 (OK)
    if response.status_code != 200:
        print(None)
        return

    # Parse the JSON response
    data = response.json()

    # Check if data contains the 'children' key, which holds the posts
    if 'data' in data and 'children' in data['data']:
        # Loop through the first 10 posts and print their titles
        for i in range(min(10, len(data['data']['children']))):
            print(data['data']['children'][i]['data']['title'])
    else:
        # If no posts are found, print None
        print(None)

