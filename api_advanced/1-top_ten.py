#!/usr/bin/python3
"""Module documentation."""

import requests


def top_ten(subreddit):
    """Function documentation."""
    try:
        reddit_url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
        headers = {'User-agent': 'Mozilla/5.0'}
        response = requests.get(reddit_url, headers=headers, allow_redirects=False)

        if response.status_code == 200:
            data = response.json()
            if 'data' in data and 'children' in data['data']:
                posts = data['data']['children']
                if not posts:
                    print("None")  # Print "None" if there are no posts
                else:
                    for post in posts[:10]: #Print only the first ten
                        print(post['data']['title'])  #Print only titles
            else:
                print("None") #JSON format incorrect
        else:
            print("None") #Status code is not 200
    except Exception:
        print("None") #Catch any other errors
