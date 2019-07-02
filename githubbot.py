# the following 2 libraries handle the request respond cycle for this script
import requests
import json
# importing the docparse file so that usernames can be retrieved
import docparse
import time

# Jachi imports
from tqdm import tqdm, trange  # Progress Bar
import sys  # Try/except
# Images
# Thanks to StackOverflow for resources and information
from colorama import init, Fore
from termcolor import cprint  # provides color print
from pyfiglet import figlet_format  # creates the ASCII art


# ADD GITHUB USERNAME
username = 'JachiOnuoha'

# Add API token from https://github.com/settings/tokens
token = '56261ff1594ca7f6f7a8a6a29fd4f172b1ce71a5'


# # create a re-usable session object with the user credits in-built
gh_session = requests.Session()
# authenticate user
gh_session.auth = (username, token)

# this is needed when passing in the request header on the api call
h = {'Content-Length': '0'}

users = docparse.usernames
addedUsers = []
# Prints initial Message
init(strip=not sys.stdout.isatty())
cprint(figlet_format('Adding Users . . .', font='big'), 'red')

# iterate through the list of usernames from the docparse file
# also makes the progress bar GREEN
for i in trange((len(users)), bar_format="{l_bar}%s{bar}%s{r_bar}" % (Fore.GREEN, Fore.RESET)):
    # this line allows us to follow the respected amount of users without throwing any red flags to github
    # idicating that there is something attacking their website
    try:
        if users[i] != "" and users[i] != username:  # Removes empty spaces from the list to avoid errors
            time.sleep(1.2)
            # this url will be used to make the PUT request that will follow the user from your account
            follow_url = 'https://api.github.com/user/following/'+users[i]
            # this is the function that makes the PUT request to follow the user
            # an empty response indicates that the follow was successful
            follow = gh_session.put(follow_url, headers=h).text
            addedUsers.append(users[i])

    except RuntimeError:
        sys.exit()

# End sequence
# Prints ASCI art at the end of the program
cprint(figlet_format('Process Completed !', font='big'), 'green', attrs=['bold'])
