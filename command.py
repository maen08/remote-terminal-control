from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse
import os


"""
current version: only for UBUNTU terminals

"""


app = Flask(__name__)

@app.route("/")
def home():
    return 'hello world'

@app.route("/command", methods=['GET', 'POST'])
def incomming_command():

    """
        Send a dynamic reply to an incoming text message
        Get the message the user sent our Twilio number

     """
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'maen':
        resp.message('What command do you want to run on your machine?')
    
    elif body == 'init 0':
        resp.message('Shutting down your machine...')
        
        os.system('init 0')
 
         
    return str(resp)

    """
    Run the script on port 5000
    """

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port='5000')
 