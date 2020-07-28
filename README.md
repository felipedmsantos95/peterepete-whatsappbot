# Pete & Repete - WhatsApp Bot

## Sobre

Um bot para WhatsApp que conta a piada "É a história de dois cachorros: Pete e Repete. Pete morreu, quem ficou vivo?" até o usuário perder a paciência.

Uma piada genuinamente brasileira 🇧

## Prévia

<p align="center">
  <img src="https://github.com/felipedmsantos95/peterepete-whatsappbot/blob/master/img/peterepete.gif"/>
</p>

## Requisitos

-   Plataforma [Twilio](https://www.twilio.com/) para gerenciar bots de envio e recebimento de mensagens no Whatasapp
-   [Python 3.6](https://www.python.org/) ou superior
-   [Flask](https://palletsprojects.com/p/flask/) para criar uma aplicação web que responde mensagens Whatsapp
-   [Ngrok](https://ngrok.com/) para criar URL pública de acesso ao serviço na sua máquina (Podem ser utilizados também outros serviços ex: AWS ou Heroku)

## Executando o projeto

### Clonando o projeto

```bash
$ git clone https://github.com/felipedmsantos95/peterepete-whatsappbot
$ cd peterepete-whatsappbot
```

### Configurar WhatsApp no Twilio

Na seção ["Configure the Twilio WhatsApp Sandbox"](https://www.twilio.com/blog/build-a-whatsapp-chatbot-with-python-flask-and-twilio) é mostrado como configurar o ["WhatsApp Sandbox"](https://www.twilio.com/console/sms/whatsapp/learn) no Twillio, desta forma é possível prosseguir nos passos seguintes.

## Criar ambiente virtual Python

É necessário ter instalado o pacote `virtualenv` no sistema, que pode ser obtido pelo comando seguinte:

```bash
$ sudo pip install virtualenv
```
Feito isso, dentro do diretório do projeto, podemos executar o seguinte: 

```bash
$ virtualenv --python='/usr/bin/python3' whatsapp-bot-venv
$ source whatsapp-bot-venv/bin/activate
(whatsapp-bot-venv) $ pip install twilio flask requests
```
NOTA: para verificar o diretório correto do Python 3 em seu sistema, pode-se executar `which python3`

## Rodando o Chatbot

Para executar o chatbot, basta executar `python bot.py`, a saída será a seguinte:

```bash
(whatsapp-bot-venv) $ python bot.py
 * Serving Flask app "bot" (lazy loading)
 * Environment: production
   WARNING: This is a development server. Do not use it in a production deployment.
   Use a production WSGI server instead.
 * Debug mode: off
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

Em um segundo terminal, no diretório do Flask instalado, podemos executar

```bash
./ngrok http 5000
```

Um endereço de domínio público temporário será alocado. A saída será a seguinte:

<p align="center">
  <img src="https://github.com/felipedmsantos95/peterepete-whatsappbot/blob/master/img/flask.png"/>
</p>

Copie no painel do Twilio o endereço fornecido e acrescente o `\bot` ao final dele:

<p align="center">
  <img src="https://github.com/felipedmsantos95/peterepete-whatsappbot/blob/master/img/twilio_url.png"/>
</p>

Agora pode testar sua paciência com o nosso Pete&Repete Bot!
