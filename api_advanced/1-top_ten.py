#!/usr/bin/python3
"""
This script retrieves the titles of the top 10 hot posts from a given
subreddit. It prints the titles, one per line.
If the subreddit is invalid or an error occurs, it prints "None".
"""

import json
import requests
import sys  # Required to get command line arguments


def top_ten(subreddit):
    """
    Queries the Reddit API and prints the titles of the first 10 hot posts
    for the given subreddit. If the subreddit is not valid, prints "None".
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json?limit=10"
    headers = {'User-Agent': 'alu-scripting/1.0 (by /u/YourRedditUsername)'}  #  REPLACE with your Reddit username

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx status codes)
        data = response.json()

        if 'data' in data and 'children' in data['data']:
            for post in data['data']['children']:
                print(post['data']['title'])  # Print titles only
        else:
            print("None")  # Handle no posts found (valid but empty subreddits)

    except requests.exceptions.RequestException:
        print("None")  # Handle request errors (e.g., 404 for invalid subreddit)
    except json.JSONDecodeError:
        print("None")  # Handle JSON decoding errors
    except Exception:
        print("None")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        subreddit_name = sys.argv[1]
        top_ten(subreddit_name)
    else:
        print("Please pass an argument for the subreddit to search.")
