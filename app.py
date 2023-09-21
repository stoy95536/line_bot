from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import datetime
import openai



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


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event): # event.message.text 使用者輸入內容
    
    # profile = line_bot_api.get_profile('<user_id>')
    if event.message.text == '查詢':
        message = TextSendMessage(text=f"您好，要問什麼問題呢？\n時間{datetime.datetime.now()}") # bot return the Message to User
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

import os
if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)
    
