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


#六都選擇
def fake_house(event): 
    try:
        message = TemplateSendMessage(
            alt_text='房屋591',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://img1.591.com.tw/house/2023/09/03/169371681244317506.jpg!fit.1000x.water2.jpg',
                        imageAspectRatio='square',
                        title='★可寵★捷運★新光★獨洗獨曬★',
                        text='.',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15182030'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='查詢 西屯區青海路二段193巷'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),

                    CarouselColumn(
                        thumbnail_image_url='https://img1.591.com.tw/house/2023/09/03/169371681244317506.jpg!fit.1000x.water2.jpg',
                        imageAspectRatio='square',
                        title='★可寵★捷運★新光★獨洗獨曬★',
                        text='.',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15182030'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='查詢 西屯區青海路二段193巷'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))