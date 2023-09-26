from flask import Flask, request, abort 
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os,datetime,openai,threading
import pandas as pd
import rent_house


search_flag = 0
event_data = []


app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])
openai.api_key = os.environ['CHATGPT_API_KEY']

# @app.route("/")
# def home():
#   try:
#     # 網址被執行時，等同使用 GET 方法發送 request，觸發 LINE Message API 的 push_message 方法
#     line_bot_api.push_message('Uce078b5f96c3f0c0e76a9f0315f5b843', TextSendMessage(text='Hello World!!!'))
#     return 'OK'
#   except:
#     print('error')
    
@app.route("/")
def home():
    global event_data
    global search_flag
    try:
        if search_flag == 1:
            event = event_data[0]
            line_bot_api.push_message('Uce078b5f96c3f0c0e76a9f0315f5b843', TextSendMessage(text=search_flag))
            Run_ChatGPT(event)
            search_flag = 0
            
        msg = request.args.get('msg')   # 取得網址的 msg 參數
        if msg != None:
            # 如果有 msg 參數，觸發 LINE Message API 的 push_message 方法
            line_bot_api.push_message('Uce078b5f96c3f0c0e76a9f0315f5b843', TextSendMessage(text=msg))
            return msg
        else:
            return 'OK'

    except:
        print('error')
        return 'error'
        


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
    
    global event_data
    event_data = []
    event_data.append(event)
     
    # user_id = event.source.userId
    # profile = line_bot_api.get_profile(event.source.userId)
    
    
    User_name = line_bot_api.get_profile(event.source.user_id)
    
    line_bot_api.push_message(f'{event.source.user_id}', TextSendMessage(text='7414'))
    


    # usersdata = {'username': f'{User_name.display_name}',
    #              'user_id': f'{event.source.user_id}',
    #              'user_input_text':f'{event.message.text}'}
    
    
    
    # message = TextSendMessage(text=f"{type(event)} \n{event.source.user_id} \n{User_name} \n{User_name.display_name} ")
    # line_bot_api.reply_message(event.reply_token, message)
    
    
    
    if "查詢" in event.message.text :
        global search_flag
        search_flag = 1
        
        try :
            message = TextSendMessage(text=f"請稍等...小Bee正在努力查詢中...")
            line_bot_api.reply_message(event.reply_token, message) 
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
        

        
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

    #以下是找租屋對話框
    if event.message.text == '找租屋':
        rent_house.administrative_district(event)
        
    if event.message.text == '六都':
        rent_house.choose_City_six(event)

    if event.message.text == '非六都':
        rent_house.choose_City_notsix(event)
        

        
    
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
        
        
def Run_ChatGPT(event):
    try:
        ask = event.message.text.split(" ")[1]
        
        completion = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "user", "content": f"{ask}請用繁體字回答"}
            ]
        )
        result = completion.choices[0].message.content
        message = TextSendMessage(text=f"{result}\n時間{datetime.datetime.now()}") # bot return the Message to User
        line_bot_api.push_message(f'{event.source.user_id}', TextSendMessage(text=message))
    except:
        line_bot_api.push_message(f'{event.source.user_id}', TextSendMessage(text='發生錯誤!'))




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
    
