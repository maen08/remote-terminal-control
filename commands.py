from flask import Flask, request, redirect
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)

@app.route("/")
def home():
    return 'hello world'

@app.route("/command", methods=['GET', 'POST'])
def incomming_command():
    """Send a dynamic reply to an incoming text message"""
    # Get the message the user sent our Twilio number
    body = request.values.get('Body', None)

    # Start our TwiML response
    resp = MessagingResponse()

    # Determine the right reply for this message
    if body == 'hello':
        resp.message("Hi!, naitwa Elsa(but i'm bot, not human),nipo kukuondolea stress za covid-19\n"
                     "\n\nchagua taarifa:\n"
                     "1. kujikinga dhidi ya corona\n"
                     "2. kutoa stress kutokana na taarifa za corona\n"
                     "3. ushauri katika kipindi hiki cha mpito\n"
                     
                     "\n\n\ncoded by @maen"
                     
                     )
    elif body == '1':
        resp.message("mkuu, we nawa tu mikono na maji mengi na sabuni,"
                     "usiogope bill ya maji, wacha iyo tutalipa!!"
                     "\npia fuata ushauri wa wataalamu wa afya"
                     
                     )

    elif body == '2':
        resp.message(
            "bofya hapa: https://youtu.be/45LoVxf612Y"
        )
    
    elif body == '3':
        resp.message(
            "Muombe sana Mungu, tafuta hela, nawa sana mikono..haha\n"
            "\npia kuna online courses za bure kibao, ni muda wako tu"
       
        )
        
    else:
        resp.message("Aisee!! fuata maelekezo boss,!! me sio binadamu")   
         
    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
 