from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os


"""
Current version: Only for UBUNTU terminals
"""


app = Flask(__name__)

@app.route("/")
def home():
    # Just to make sure if flask server runs successfully
    return 'Hello, the server is running...'



@app.route("/command", methods=['GET', 'POST'])
def command():

    """
        Send a dynamic reply to an incoming text message
        Get the message the user sent our Twilio number

     """
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'command':
        resp.message('What command do you want to run on your machine?')

    # You can send any command
    elif body == 'init 0':
        resp.message('Shutting down your machine...')
        os.system('init 0')

    elif body != 'command':
        os.system(body)
  
    return str(resp)

 
if __name__ == "__main__":
    # Run the script on port 5000
    app.run(debug=True, host='0.0.0.0', port='5000')
 