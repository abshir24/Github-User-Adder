# the following 2 libraries handle the request respond cycle for this script
import requests
import json
#importing the docparse file so that usernames can be retrieved
import docparse
import time

# ADD GITHUB USERNAME
username = 'USERNAME'

# Add API token from https://github.com/settings/tokens
token = 'API TOKEN'


# # create a re-usable session object with the user credits in-built
gh_session = requests.Session()
#authenticate user
gh_session.auth = (username, token)

# this is needed when passing in the request header on the api call
h = {'Content-Length' : '0'}

users = docparse.usernames

# iterate through the list of usernames from the docparse file
for user in users:
    # this line allows us to follow the respected amount of users without throwing any red flags to github
    # idicating that there is something attacking their website
    time.sleep(2)
    #this url will be used to make the PUT request that will follow the user from your account
    follow_url = 'https://api.github.com/user/following/'+user
    # this is the function that makes the PUT request to follow the user
    # an empty response indicates that the follow was successful
    follow = gh_session.put(follow_url,headers = h).text
    print(follow)





