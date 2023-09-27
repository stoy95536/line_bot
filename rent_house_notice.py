from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import *
import os
import datetime
import openai
import pandas as pd


line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

#六都 離島 非六都選擇
def notice(event): 
    try:
        message = TemplateSendMessage(
            alt_text='租屋須知',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        # thumbnail_image_url="https://www.hbtamsui.com.tw/images/ewp/23/%E7%A7%9F%E5%B1%8B%E7%B0%BD%E7%B4%84%E8%A6%81%E5%B8%B6%E4%BB%80%E9%BA%BC.jpg",
                        # imageAspectRatio='square',
                        title='租屋應該要準備什麼',
                        text='租屋簽約時，要記得帶身份證正本、影本、工作證及錢，方便房東認明身份：\n身份證：證明自己是要租屋的本人，所提供的身份證影本，常會附在租約上作為簽約證明，若擔心個人資料遭冒用，可以先在影本上註記「僅供xxx年租屋簽約使用」。\
                        \n在以前常常還會加上個人印章，作為正式合約的身份認定，但現在大多不會這麼正式，僅需簽名即可，也可避免個人重要印鑑外流。',
                        actions=[
                            MessageTemplateAction(
                                label='台中市',
                                text='台中市'
                            ),
                            MessageTemplateAction(
                                label='台南市',
                                text='台南市'
                            ),
                            MessageTemplateAction(
                                label='高雄市',
                                text='高雄市'
                            )
                        ]   
                    ),

                    CarouselColumn(
                        #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                        title='台中市、台南市、高雄市',
                        text='也可直接在對話筐輸入縣市',
                        actions=[
                            MessageTemplateAction(
                                label='台中市',
                                text='台中市'
                            ),
                            MessageTemplateAction(
                                label='台南市',
                                text='台南市'
                            ),
                            MessageTemplateAction(
                                label='高雄市',
                                text='高雄市'
                            )
                        ]   
                    ) 
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
