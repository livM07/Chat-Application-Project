# TravelBot

TravelBot is a flask app that allows users to ask it travel-related questions through ChatGPT. The app provides users with recommendations for travel destinations through a conversational interface. The travel bot provides personalised recommendations and adjusts them to the user’s preferences.

## Features

- User account registration and authentication
- ChatGPT API for Travel bot conversational interface
- Access to past conversations
- Search function to search past conversations
- Responsive design

# Set Up

## Prerequisites

Requires python3, flask, venv, sqlite, JavaScript, OpenAI account and ChatGPT API key.

## Create your own ChatGPT API Key

[Follow this link to create your own ChatGPT API Key](https://auth0.openai.com/u/login/identifier?state=hKFo2SB4amoycmY2RFFBSk5iY2dMckN2QWlpLURSdTAxeFlGZ6Fur3VuaXZlcnNhbC1sb2dpbqN0aWTZIEFselJkQnZ4aFc4blQyVTRONDU1dXlWQjVobXQ0OVVUo2NpZNkgRFJpdnNubTJNdTQyVDNLT3BxZHR3QjNOWXZpSFl6d0Q)

## Set Up

To start the server via localhost: 
1. Clone the GitHub repository
2. Create a virtual environment:
  -  use pip to create a virtual environment: 
      ```python3 -m venv venv```
  -  activate the environment: 
      ```source venv/bin/activate```
  -  install the requirements: 
       ```pip install -r requirements.txt```
3. Set flask app variable: 
        ```export FLASK_APP=app/routes.py```
4. Input your own ChatGPT API Key into route.py file (in the app folder) on line 11:
        ```openai.api_key = '<PUT YOUR KEY HERE>'```
6. Run the app: 
        ```flask run```

# Usage

1. In your web browser open localhost:
    ```http://127.0.0.1:5000```
2. Once you have reached the home page click on the "Log In" button to either log in or create an account (note: once you create an account you will be redirected to the home page to log in)
4. Once logged in, you will be redirected to the history page. This page will allow you to start a new chat, search/see past conversations and logout.
5. To start a new chat click on the "new chat" button and enter a destination. To chat, use the message input form and the submit button. The "back" button saves your conversation and redirects you back to your history/user home page.

# Authors

Olivia Morrison, Lachie Jones & Safeer Karim
        
# Acknowledgments
- [Flask Mega Tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-i-hello-world) by Miguel Grinberg
- [ChatGPT](https://openai.com/)
- [How To Create Your First Web Application Using Flask and Python 3](https://www.digitalocean.com/community/tutorials/how-to-create-your-first-web-application-using-flask-and-python-3) by Abdelhadi Dyouri
- [Bootstrap](https://getbootstrap.com/)
- [Flask Pallet Projects](https://flask.palletsprojects.com/en/1.1.x/quickstart/)
- [SQLAlchemy — Python Tutorial](https://towardsdatascience.com/sqlalchemy-python-tutorial-79a577141a91) by Vinay Kudari
- [wtforms](https://wtforms.readthedocs.io/en/3.0.x/)
