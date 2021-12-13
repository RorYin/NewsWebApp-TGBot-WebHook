from logger import logger
import os
import requests


#initializing the bot 
# token = "Bot Token HERE" #testing
token = os.environ.get('token')  #production
bot=logger(token)

def handletgbotquery(text,chat_id,msg_id,query):
    headers = {'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.93 Safari/537.36"}
    url="http://roryin-newsapi.herokuapp.com/?q="
    try:
        response=requests.get(url+text[1:],headers).json()
        j=0
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

_{date}_
*@tg_new_news_bot*"""
                bot.sendPhoto(image_url,tosend,chat_id,-1,"Markdown")
                j+=1
        bot.deleteMessage(chat_id,msg_id+1)
        return
    except:
        bot.sendMsgTo(chat_id,"Something went wrong while handling commands",msg_id,"Markdown")
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
/topnews
/india
/karnataka
/bengaluru
/covid
/world
/technoboty
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