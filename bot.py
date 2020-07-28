from flask import Flask, request
from utils import *
import requests
from twilio.twiml.messaging_response import MessagingResponse

app = Flask(__name__)
greetings = ['ola', 'tudo bem', 'oi', 'hello', 'welcome', 'bem vindo', 'blz', 'eaew', 'e aí', 'como esta', 'boa', 'tarde', 'noite', 'bom dia']
goodbyes = ['tchau', 'flw', 'embora', 'bye', 'adeus', 'goodbye', 'xau', 'fui', 'indo']
laughs = ['kk', 'asuah', 'hasuah', 'rsrs', 'lol', 'apoaks' ]
history = 'É a história de dois cachorros: Pete e Repete. Pete morreu, quem ficou vivo?'

@app.route('/bot', methods=['POST'])
def bot():
    incoming_msg = request.values.get('Body', '')
    incoming_msg = normalize_words(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    send_dog_image = False
    intro = 'Legal o que você falou. Agora eu tenho uma historia...\n'

    if any(word in incoming_msg for word in greetings):
        send_dog_image = True
        intro = 'Olá! Vou lhe contar uma história...\n'
    elif any(word in incoming_msg for word in goodbyes):
        send_dog_image = True
        intro = 'Antes de você ir, gostaria de contar uma história...\n'
    elif any(word in incoming_msg for word in laughs):
        send_dog_image = True
        intro = 'Engraçado kkk, mas você já viu essa história?\n'
    elif 'repete' in incoming_msg or 'repeti' in incoming_msg:
        intro = ''
    elif 'pete' in incoming_msg:
        intro = 'Resposta errada! Vou explicar de novo...\n'  
    else:
        send_dog_image = True

    if(send_dog_image):
        r = requests.get('https://dog.ceo/api/breeds/image/random')
        data = r.json()
        dog_image = data['message']
        msg.media(dog_image) 

    msg.body(intro)
    msg.body(history)
    return str(resp)


if __name__ == '__main__':
    app.run()