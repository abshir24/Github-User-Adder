from github import Github
import docparse
import requests
import json

username = 'abshir24'

# from https://github.com/user/settings/tokens
token = '9c2da613793e376e281be9f362225977b697da05'
follow_url = 'https://api.github.com/user/following/Kobe'

gh_session = requests.Session()
gh_session.auth = (username, token)

h = {'Content-Length' : '0'}

follow = gh_session.put(follow_url,headers = h).text


