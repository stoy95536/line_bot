from flask import Flask, request, abort 
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os,datetime,openai,threading
import pandas as pd
import rent_house , fake_house

search_flag = 0
event_data = []

app = Flask(__name__)

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])
openai.api_key = os.environ['CHATGPT_API_KEY']


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
    
    # line_bot_api.push_message(f'{event.source.user_id}', TextSendMessage(text='7414'))
    


    # usersdata = {'username': f'{User_name.display_name}',
    #              'user_id': f'{event.source.user_id}',
    #              'user_input_text':f'{event.message.text}'}
    
    
    
    # message = TextSendMessage(text=f"{type(event)} \n{event.source.user_id} \n{User_name} \n{User_name.display_name} ")
    # line_bot_api.reply_message(event.reply_token, message)
    
    if "查詢" in event.message.text :
        line_bot_api.push_message(f'{event.source.user_id}', TextSendMessage(text='請稍等...小Bee正在努力查詢中...'))
        
        try :
            Run_ChatGPT(event)
        except:
            line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))
        
        
    if '找地圖' in event.message.text:
        location = event.message.text.split(" ")[1]
        message = TextSendMessage(text=f"https://www.google.com/maps/search/?api=1&query={location}\n時間{datetime.datetime.now()}") # bot return the Message to User
        line_bot_api.reply_message(event.reply_token, message)
        
    if '提醒' in event.message.text:
        tip = event.message.text.split(" ")[1]
        message = TextSendMessage(text=f"目前有符合您的項目喔\n時間{datetime.datetime.now()}") # bot return the Message to User
        line_bot_api.reply_message(event.reply_token, message)
    
    if event.message.text == "機器人聊天":
        rent_house.Chat_bot_GPT(event)


    #以下是找租屋對話框
    if event.message.text == '找租屋':
        rent_house.administrative_district(event)
        
    if event.message.text == '六都':
        rent_house.choose_City_six(event)

    if event.message.text == '非六都':
        rent_house.choose_City_notsix(event)

    if event.message.text == '台中市':
        rent_house.choose_district_Taichung(event)

    if event.message.text in ['西屯區', '北區', '東區', '南屯區', '北屯區']:
        rent_house.choose_house_type(event)

    if event.message.text in ['整層住家', '獨立套房', '分租套房', '雅房', '車位', '其他']:
        rent_house.choose_rent(event)

    #if event.message.text in ['5000以下', '5000-10000', '10000-20000', '20000-30000', '30000-40000', '40000以上']:
        #pass
        #這裡要接爬到的資料 here
    if event.message.text == '5000-10000':
        fake_house.fake_house(event)
        

        
    
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
        line_bot_api.reply_message(event.reply_token, message)
    except:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤!'))




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
    
#                       _oo0oo_
#                      o8888888o
#                      88" . "88
#                      (| -_- |)
#                      0\  =  /0
#                    ___/`---'\___
#                  .' \\|     |// '.
#                 / \\|||  :  |||// \
#                / _||||| -:- |||||- \
#               |   | \\\  -  /// |   |
#               | \_|  ''\---/''  |_/ |
#               \  .-\__  '-'  ___/-. /
#             ___'. .'  /--.--\  `. .'___
#          ."" '<  `.___\_<|>_/___.' >' "".
#         | | :  `- \`.;`\ _ /`;.`/ - ` : | |
#         \  \ `_.   \_ __\ /__ _/   .-` /  /
#     =====`-.____`.___ \_____/___.-`___.-'=====
#                       `=---='
#
#
#     ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#
#               佛祖保佑         永無BUG