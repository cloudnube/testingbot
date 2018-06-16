 #!/usr/bin/env python3
# """Example bot that returns a synchronous response."""
# 
# from flask import Flask, request, json
# 
# app = Flask(__name__)
# 
# @app.route('/', methods=['POST'])
# def on_event():
#   """Handles an event from Hangouts Chat."""
#   event = request.get_json()
#   print(json.dumps(event, indent=4))
#   if event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
#     text = 'Thanks for adding me to "%s"!' % event['space']['displayName']
#   elif event['type'] == 'MESSAGE':
#     text = 'You said: `%s`' % event['message']['text']
#   else:
#     return json.jsonify({'text', 'not of type added to space or message'})
#   return json.jsonify({'text': text})
# 
# if __name__ == '__main__':
#   app.run(port=8080, debug=True)

#import logging
from flask import Flask, render_template, request, json, make_response
#from google.cloud import translate

app = Flask(__name__)
#translate_client = translate.Client()

@app.route('/', methods=['POST'])
def home_post():
    """Respond to POST requests to this endpoint.
    All requests sent to this endpoint from Hangouts Chat are POST
    requests.
    """

    data = request.get_json()

    resp = None

#    if data['type'] == 'REMOVED_FROM_SPACE':
#        logging.info('Bot removed from a space')

    resp_dict = format_response(data)
    resp = json.jsonify(resp_dict)

    print(resp)
    return resp

def format_response(event):
    """Determine what response to provide based upon event data.
    Args:
      event: A dictionary with the event data.
    """

    text = ""

    # Case 1: The bot was added to a room
    if event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'ROOM':
        text = 'Thanks for adding me to "%s"!' % event['space']['displayName']

    # Case 2: The bot was added to a DM
    elif event['type'] == 'ADDED_TO_SPACE' and event['space']['type'] == 'DM':
        text = 'Thanks for adding me to a DM, %s!' % event['user']['displayName']

    elif event['type'] == 'MESSAGE':
        text = 'Your message: "%s"' % event['message']['text']
       # translation = translate_client.translate(event['message']['text'], 
        #        target_language = 'ru') 
       # text = u'Translation: {}'.format(translation['translatedText'])

    return { 'text': text }
