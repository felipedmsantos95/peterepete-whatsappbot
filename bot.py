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
    incoming_msg = normalizeWords(incoming_msg)
    resp = MessagingResponse()
    msg = resp.message()
    sendDogImage = False
    intro = 'Legal o que você falou, acho interessante a maneira que se você se expressa. Agora eu tenho uma historia pra ti...\n'

    if any(word in incoming_msg for word in greetings):
        sendDogImage = True
        intro = 'Olá! Vou lhe contar uma história...\n'
    elif any(word in incoming_msg for word in goodbyes):
        sendDogImage = True
        intro = 'Antes de você ir, gostaria de contar uma história...\n'
    elif any(word in incoming_msg for word in laughs):
        sendDogImage = True
        intro = 'Engraçado kkk, mas você já viu essa história?\n'
    elif 'repete' in incoming_msg or 'repeti' in incoming_msg:
        print(incoming_msg)
        intro = ''
    elif 'pete' in incoming_msg:
        intro = 'Resposta errada! Vou explicar de novo...\n'  
    else:
        sendDogImage = True

    if(sendDogImage):
        r = requests.get('https://dog.ceo/api/breeds/image/random')
        data = r.json()
        dogImage = data['message']
        msg.media(dogImage) 

    msg.body(intro)
    msg.body(history)
    return str(resp)


if __name__ == '__main__':
    app.run()