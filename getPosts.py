"""
Gets all posts on a user's timeline
"""
import facebook
import requests


def post_action(post):
    """ todo, process fb status message ot other content
    """
    print(post['created_time'])


# temporary access token here https://developers.facebook.com/tools/explorer/
access_token = ''
# Fill in a public user by using their Facebook id as user.
user = ''

graph = facebook.GraphAPI(access_token)
profile = graph.get_object(user)
posts = graph.get_connections(profile['id'], 'posts')

# Wrapped in a while loop to keep processing requests until done
while True:
    try:
        # Perform some action for post
        [post_action(post=post) for post in posts['data']]
        # Make a request to the next page of data, if exists.
        posts = requests.get(posts['paging']['next']).json()
    except KeyError:
        # If there are no more pages (['paging']['next']), break the loop and end the script.
        break