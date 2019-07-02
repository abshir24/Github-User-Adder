# Github-User-Adder
This program takes in a list of github users from an excel file and auto adds them from the user's account (Specifically for
New Technologists Team Microsoft)

NOTE: Python's pip package-management system needs to be installed on your laptop in order to for the script to work.
Here is a link that will you help you with that --> https://www.makeuseof.com/tag/install-pip-for-python/
or type in the command "sudo easy_install pip" into your command prompt

1. Clone the repository and save it anywhere that is accessible to you

2. Use your terminal to navigate to the project directory

3. If pip is installed then pip install the following libraries from your command prompt: requests,xlrd

NOTE:If this is not working try using the sudo key word before the pip install statement. For example: "sudo pip install requests"

4. Download excel file from teams and save it in the repository that was just cloned

5. Replace the file name in the docparse.py file with the desired name of your excel file

6. Replace the user name in the githubbot.py file with your github username

7. Replace the Api Token variable with the token that you recieve from https://github.com/settings/tokens 

NOTE: when generating a new token select the 'user' option when asked to "select scopes".

8. Type the command "python githubbot.py" into your command prompt.

NOTE: This program might take at least 2 minutes to run, so feel free to open up a new tab in your terminal if you need to 
use your command prompt.

NOTE: If the message {"message":"Not Found","documentation_url":"https://developer.github.com/v3/users/followers/#follow-a-user"}
is displayed ignore it. This is just indicating that one of the empty slots parsed from the excel file does not exist.

Feel free to reach out to me if you all have any question.

