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

def sendCarousel_City(event): 
    try:
        message = TemplateSendMessage(
            alt_text='城市選擇',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://img1.591.com.tw/house/2023/09/08/169414163003871703.jpg!510x400.jpg',
                        title='請問你要找哪個縣市的房子呢？',
                        text='也可直接在對話筐輸入縣市',
                        actions=[
                            MessageTemplateAction(
                                label='台北市',
                                text='台北市'
                            ),
                            MessageTemplateAction(
                                label='新北市',
                                text='新北市'
                            ),
                            MessageTemplateAction(
                                label='桃園市',
                                text='桃園市'
                            ),
                        ]
                        
                    ),

                    CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                        title='請問你要找哪個縣市的房子呢?',
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