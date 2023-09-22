from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import datetime
import openai
import pandas as pd



app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'


def sendButton(event):
    try:
        message = TemplateSendMessage(
            alt_text = '按鈕樣板',
            template = ButtonsTemplate(
                thumbnail_image_url='https://i.imgur.com/pRdaAmS.jpg',
                title='按鈕樣板範例',
                text='請選擇：',
                actions=[
                    MessageTemplateAction(
                        label='文字訊息',
                        text='@購買披薩'
                    ),
                    URITemplateAction(
                        label='連結網頁',
                        uri='https://www.grazie.com.tw/menu#food=1&meal=1'
                    ),
                    PostbackTemplateAction(
                        label='回傳訊息',
                        data='action=buy'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))        




@handler.add(MessageEvent, message=TextMessage)
def handle_message(event): # event.message.text 使用者輸入內容
    
    
    
    # user_id = event.source.userId
    # profile = line_bot_api.get_profile(event.source.userId)
    
    
    User_name = line_bot_api.get_profile(event.source.user_id)
    
    # usersdata = {'username': f'{User_name.display_name}',
    #              'user_id': f'{event.source.user_id}',
    #              'user_input_text':f'{event.message.text}'}
    
    
    # usersdata_pd = pd.DataFrame(usersdata)
    
    
    # usersdata_pd.to_csv('user_name.csv')
    
    
    # message = TextSendMessage(text=f"{type(event)} \n{event.source.user_id} \n{User_name} \n{User_name.display_name} ")
    # line_bot_api.reply_message(event.reply_token, message)
    
    if event.message.text == '幹你娘':
        sendButton(event)
            
        
        
    
    
    
    if event.message.text == '查詢':
        message = TextSendMessage(text=f"{User_name.display_name}您好，要問什麼問題呢？\n時間{datetime.datetime.now()}") # bot return the Message to User
        line_bot_api.reply_message(event.reply_token, message) 
        
    if event.message.text == '你好':
        message = TextSendMessage(text=f"你好\n時間{datetime.datetime.now()}") # bot return the Message to User
        line_bot_api.reply_message(event.reply_token, message) 
    
    if '找地圖' in event.message.text:
        location = event.message.text.split(" ")[1]
        message = TextSendMessage(text=f"https://www.google.com/maps/search/?api=1&query={location}\n時間{datetime.datetime.now()}") # bot return the Message to User
        line_bot_api.reply_message(event.reply_token, message)
        
        
    if '提醒' in event.message.text:
        tip = event.message.text.split(" ")[1]
        message = TextSendMessage(text=f"目前有符合您的項目喔\n時間{datetime.datetime.now()}") # bot return the Message to User
        line_bot_api.reply_message(event.reply_token, message)
        



        
    
    # if event.message.text == '找地圖':
    #     message = TextSendMessage(text=f"請問要找哪裡呢\n時間{datetime.datetime.now()}") # bot return the Message to User
    #     line_bot_api.reply_message(event.reply_token, message) 
    #     while 1:
    #         location = event.message.text
    #         if location != "":
    #             message = TextSendMessage(text=f"https://www.google.com/maps/search/?api=1&query={location}\n時間{datetime.datetime.now()}") # bot return the Message to User
    #             line_bot_api.reply_message(event.reply_token, message)
    #             break 


    if event.message.text == 'test':
        message = TextSendMessage(text=f"幹你娘雞掰\n時間{datetime.datetime.now()}") # bot return the Message to User
        line_bot_api.reply_message(event.reply_token, message)
        



def sendPizza(event):
    try:
        message = TextSendMessage(
            text = '感謝您的購買，我們盡快為您製作',
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))

def sendBack_buy(event, backdata):
    try:
        text1 = '感謝您的購買，我們盡快為您製作。(action 的值為' + backdata.get('action') + ')'

        message = TextSendMessage(
            text = text1
        )
        
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))



import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
