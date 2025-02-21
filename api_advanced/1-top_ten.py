#!/usr/bin/python3
"""
This module retrieves the titles of the top 10 hot posts
from a specified subreddit using the Reddit API.
If the subreddit is invalid, it prints None.
"""

import json
import requests
import sys  # Required to get command line arguments


def top_ten(subreddit):
    """
    Prints the titles of the top 10 hot posts from a subreddit.
    Prints None if the subreddit is invalid.
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'alu-scripting/1.0 (by /u/YourRedditUsername)'} # Replace with your Reddit username

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx status codes)
        data = response.json()


        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title']) # ONLY print titles
        else:
            print("None")  # Print None if no posts are found (possible for valid, but empty subreddits)

    except requests.exceptions.RequestException as e:
        print("None") # Print None if there is a request exception (eg. 404)
    except json.JSONDecodeError as e:
        print("None")  # Print None if the JSON is invalid
    except Exception:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
    else:
        print("Please pass an argument for the subreddit to search.")
