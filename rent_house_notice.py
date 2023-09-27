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
                        thumbnail_image_url='https://images.unsplash.com/photo-1450101499163-c8848c66ca85?ixlib=rb-4.0.3&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D&auto=format&fit=crop&w=6540&q=80',
                        # imageAspectRatio='square',
                        title='台北市、新北市、桃園市',
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
