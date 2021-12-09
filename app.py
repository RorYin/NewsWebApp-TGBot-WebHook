from flask.wrappers import Request
import telebot
from flask import Flask, json ,request

token="5002606701:AAFt2QcHWaEgqW0T63dXmTIQYglYX2Dw1bM"
secret=""
# url="https://roryin.pythonanywhere.com/"
url="https://webapppbot.herokuapp.com/"

bot = telebot.TeleBot(token,threaded=False)
bot.remove_webhook()
bot.set_webhook(url=url)


app = Flask(__name__)
@app.route('/',methods=['POST'])
def webhook():
    update = telebot.types.Update.de_json(request.stream.read().decode('utf-8'))
    bot.process_new_updates([update])
    return ('ok',200)


@bot.message_handler(commands=['start'])
def start(msg):
    bot.send_message(msg.chat.id,"Hello user")

