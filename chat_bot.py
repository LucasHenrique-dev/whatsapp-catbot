from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)


@app.route('/bot', methods=['POST'])
def bot():
    saudacoes = ["bom dia", "boa tarde", "boa noite"]
    resp = MessagingResponse()
    msg = resp.message()

    incoming_msg = request.values.get('Body', '').lower()

    if 'gato' in incoming_msg:
        msg.media('https://cataas.com/cat')
    elif incoming_msg in saudacoes:
        incoming_msg = '%20'.join(incoming_msg.split(' ')).title() + "!"
        url = f'https://cataas.com/cat/says/{incoming_msg}?size=80&color=white'
        msg.media(url)
    elif 'segredo' in incoming_msg:
        msg.media('https://cataas.com/cat?filter=sepia')
    elif 'meow' in incoming_msg or 'miau' in incoming_msg:
        msg.body('🐱')
    else:
        msg.body('Meow')

    return str(resp)


if __name__ == '__main__':
    app.run()
