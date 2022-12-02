
import os
from flask.templating import render_template_string,render_template
import requests
from flask import Flask,jsonify,request,Response

from logger import logger

#Setting the flask app
app = Flask(__name__)
app.url_map.strict_slashes=False

# token = "Bot TOKEN HERE" #testing

token = os.environ.get('token')  #production
bot=logger(token)

#for webapp
def getdata(query):
    url="http://roryin-newsapi.herokuapp.com/?q="
    headers = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36'}
    try:
        response=requests.get(url+query,headers=headers).json()
        output=""
        if len(response)==0:
            return render_template("display.html",output="No results found ,try with other topic")
        for i in response:
            image_url = i['image url']
            headline = i['headline']
            paragraph = i['paragraph']
            date = i['date']
            source_url = i['source url']

            result=fr""" <div class="gridelement" style="align-self: center;
        display: inline-block;
        font-family: 'Raleway', sans-serif;
        width: 45%;
        border-radius: 20px;
        border-left: salmon;
        margin-bottom:5px;
        
        
        padding: 5px 5px 5px 5px;
        box-shadow: 3px 3px 3px 3px #e1eaee;">
            <body style="text-align:center">
                <center style=" font-family:arial">
                
                
                <img src="{image_url}" alt="" width="97%" height="35%" style="border-radius:12px; object-fit:cover;"><br>
                <br>
                <h2 style="color:#000000;font-size:19px;">{headline}</h2>
                <div class="text" style="width:90%;>
                
                <h2 style="width:90%; font-size:12px;">Description: {paragraph}</h2><h2>
                    <h1 style="font-size:18px; color: rgb(32, 7, 122);">{date}</h1>
                
                
                <div style="color:#0918B3">
                
                <div>
                </div>
                
                <button class="btn danger" onclick="window.location.href='{source_url}'" style="width:90%;
                    border: 2px solid black;
                    background-color: white;
                    color: black;
                    padding: 14px 28px;
                    font-size: auto;
                    cursor: pointer;
                    border-radius:15px;
                    float:center; 
                    background: hsl(214, 81%, 51%);
                    color: white;">Read More</button><br><br>
                
                    
                
                </div></div></center></body>
        </div>"""
                
                
            output=output+result
            
        
        output=f""" <html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta http-equiv="X-UA-Compatible" content="IE=edge">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <link rel="shortcut icon" type="image/x-icon" href="https://telegra.ph/file/ccba9696db89a8598b8fe.png">
        <title>Search Results</title>
        
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Kumbh+Sans&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans&display=swap');
        @import url('https://fonts.googleapis.com/css2?family=Noto+Sans&family=Raleway:wght@100;500&display=swap');
    



    </style>
    </head>
    <body>
        <center><h2>
        <div class="header" ><img src="https://telegra.ph/file/ccba9696db89a8598b8fe.png" alt="" style="max-width: 100px;"></div>
        <div class="header" style="border-radius: 20px;font-family:monospace;font-size:30px;align-self: center;vertical-align: middle;width: 50%; margin-top:2%">Search Results</div>
        </center></h2>
        <div class="gridcontainer" style="padding-top:1%;border-radius: 20px; align-self: center;vertical-align: middle;width: 100%;">
        {output}
        </div>
    </body>
    </html>"""
        #print(output)
        return output
    except :
        return render_template("display.html",output="No results found ,try with other topic")


#ForTGBot
def handletgbotquery(text,chat_id,msg_id,query):
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    url="http://roryin-newsapi.herokuapp.com/?q="
    try:
        response=requests.get(url+text[1:],headers).json()
        j=0
        if len(response)==0:
            bot.deleteMessage(chat_id,msg_id+1)
            bot.sendMsgTo(chat_id,"No results found ,try with other topic",msg_id,"Markdown")
            return

        for i in response:
            if j<10:
                image_url = i['image url']
                headline = i['headline']
                paragraph = i['paragraph']
                date = i['date']
                date=date.strip()
                source_url = i['source url']
                tosend=f"""*{headline}*
_{paragraph}..._
[Read More]({source_url})

{date}
*@tg_new_news_bot*"""
                bot.sendPhoto(image_url,tosend,chat_id,-1,"Markdown")
                j+=1
        bot.deleteMessage(chat_id,msg_id+1)
        return
    except:
        bot.sendMsgTo(chat_id,"No results found ,try with other topic",msg_id,"Markdown")
        return


def handlecommands(text,chat_id,msg_id):
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    if(text[:6]=="/start"):
        imgurl="https://telegra.ph/file/9c1f4d16da49fbf86bbeb.jpg"
        text1="""*Welcome to Indian NEWS Bot*,
_get latest NEWS of every category quicky _

To know more about bot usage /help
[API Source Code](https://github.com/RorYin/News-API)
[Bot Developped By RorYin](https://github.com/RorYin)

*Stay Safe ,Stay Home*"""
        bot.sendPhoto(imgurl,text1,chat_id,msg_id,"Markdown")
        return

    elif(text[:5]=="/help"):
        imgurl="https://telegra.ph/file/a949a494c82612f6fa2b3.jpg"
        txt="""*Get top 10 NEWS of category you wish*
_Just select the category you want from below_

/india
/karnataka
/bengaluru
/covid
/world
/technology
/entertainment
/business
/education
/viral
/lifestyle
/food

*Or simply search any topic by sending in format of "/topicname"  to bot*
*Stay Safe ,Stay Home*"""
        bot.sendPhoto(imgurl,txt,chat_id,msg_id,"Markdown")
        return

    else:
        bot.sendMsgTo(chat_id,"Please wait....",msg_id,"Markdown")
        handletgbotquery(text,chat_id,msg_id,text[1:])
        return
        







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
            handlecommands("/help",chat_id,message_id)
            return Response("Ok",status=200)

        





if __name__ == '__main__':
    app.debug=True
    app.run()    
