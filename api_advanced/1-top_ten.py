#!/usr/bin/python3
import requests

def recurse(subreddit, hot_list=[], after=None):
    """Recursively queries Reddit API to get the titles of hot posts for a given subreddit."""
    
    # Reddit API URL with parameters to get hot posts
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    
    # Adding 'after' if it exists to handle pagination
    params = {'after': after} if after else {}
    
    # Send a GET request to Reddit API
    headers = {'User-Agent': 'python3:redditapi:v1.0 (by /u/yourusername)'}
    response = requests.get(url, headers=headers, params=params, allow_redirects=False)
    
    # Check for valid response
    if response.status_code != 200:
        return None  # Return None if the subreddit is invalid or any error occurs
    
    data = response.json()
    
    # Check if data contains 'data' and 'children' (list of posts)
    if 'data' in data and 'children' in data['data']:
        for post in data['data']['children']:
            hot_list.append(post['data']['title'])
        
        # Check if there is another page of posts (pagination)
        after = data['data'].get('after', None)
        
        # If 'after' exists, recursively call the function with the new 'after' value
        if after:
            return recurse(subreddit, hot_list, after)
    
    # Return the final hot list when no further pages exist
    return hot_list if hot_list else None

