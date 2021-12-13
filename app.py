import os
from logger import logger
from flask.templating import render_template_string,render_template
import requests

from flask import Flask,jsonify,request,Response


#for webapp
from webapphandler import *
#for tgbot
from bothandler import *

#Setting the flask app
app = Flask(__name__)
app.url_map.strict_slashes=False


#initializing the bot 
# token = "Bot Token HERE" #testing
token = os.environ.get('token')  #production
bot=logger(token)







        







@app.route('/',methods=['POST','GET'])
def home():
    query=request.args.get('q')
    
    if query == None:
        return render_template("index.html")
    else:
        print(query)
        data=getdata(query)
 
        
    return render_template_string(data)

@app.route('/botupdates',methods=['POST','GET'])
def handlebot():
    if request.method == "POST":
        
        try:
            msg=request.get_json()
        except:
            bot.sendMsgTo(887572477,"Something went wrong in bot while getting updates",55,"Markdown")
            print("Something went wrong while getting updates")
            return Response("Ok",status=200)
            
        try:
            #get all normal text messages
            chat_id=msg['message']['chat']['id']
            text=msg['message']['text']
            message_id=msg['message']['message_id']
        except:
            bot.sendMsgTo(887572477,"Something went wrong in bot while parsing json data",55,"Markdown")
            print("Something went wrong while parsing json data")
            return Response("Ok",status=200)
            

        if (text[0]=="/"):
                handlecommands(text,chat_id,message_id)
                return Response("Ok",status=200)
        else:
            bot.sendMsgTo(chat_id,"Help message here",message_id,"Markdown")
            return Response("Ok",status=200)

        





if __name__ == '__main__':
    app.debug=True
    app.run()    