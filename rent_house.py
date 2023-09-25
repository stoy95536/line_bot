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
def administrative_district(event): 
    try:
        message = TemplateSendMessage(
            alt_text = '按鈕樣板',
            template = ButtonsTemplate(
                thumbnail_image_url='https://a.bbkz.net/guide/images/2/2d/%E5%8F%B0%E7%81%A3%E8%A1%8C%E6%94%BF%E5%8D%80%E5%9C%96.png',
                imageAspectRatio='square',
                title='請問你要找哪個區域的房子呢？',
                text='也可直接在對話筐輸入區域',
                actions=[
                    MessageTemplateAction(
                        label='六都',
                        text='六都'
                    ),
                    MessageTemplateAction(
                        label='非六都',
                        text='非六都'
                    ),
                    MessageTemplateAction(
                        label='離島',
                        text='離島'
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!')) 

#六都選擇
def choose_City_six(event): 
    try:
        message = TemplateSendMessage(
            alt_text='城市選擇',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://img1.591.com.tw/house/2023/09/08/169414163003871703.jpg!510x400.jpg',
                        imageAspectRatio='square',
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
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
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

#非六都選擇
def choose_City_notsix(event): 
    try:
        message = TemplateSendMessage(
            alt_text='城市選擇',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        thumbnail_image_url='https://img1.591.com.tw/house/2023/09/08/169414163003871703.jpg!510x400.jpg',
                        title='基隆市、新竹市、新竹縣',
                        text='也可直接在對話筐輸入縣市',
                        actions=[
                            MessageTemplateAction(
                                label='基隆市',
                                text='基隆市'
                            ),
                            MessageTemplateAction(
                                label='新竹市',
                                text='新竹市'
                            ),
                            MessageTemplateAction(
                                label='新竹縣',
                                text='新竹縣'
                            ),
                        ]
                        
                    ),

                    CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                        title='苗栗縣、彰化縣、南投縣',
                        text='也可直接在對話筐輸入縣縣',
                        actions=[
                            MessageTemplateAction(
                                label='苗栗縣',
                                text='苗栗縣'
                            ),
                            MessageTemplateAction(
                                label='彰化縣',
                                text='彰化縣'
                            ),
                            MessageTemplateAction(
                                label='南投縣',
                                text='南投縣'
                            )
                        ]   
                    ), 

                    CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                        title='雲林縣、嘉義市、嘉義縣',
                        text='也可直接在對話筐輸入縣市',
                        actions=[
                            MessageTemplateAction(
                                label='雲林縣',
                                text='雲林縣'
                            ),
                            MessageTemplateAction(
                                label='嘉義市',
                                text='嘉義市'
                            ),
                            MessageTemplateAction(
                                label='嘉義縣',
                                text='嘉義縣'
                            )
                        ]   
                    ), 
                    
                    CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                        title='雲林縣、花蓮縣、台東縣',
                        text='也可直接在對話筐輸入縣市',
                        actions=[
                            MessageTemplateAction(
                                label='雲林縣',
                                text='雲林縣'
                            ),
                            MessageTemplateAction(
                                label='花蓮縣',
                                text='花蓮縣'
                            ),
                            MessageTemplateAction(
                                label='台東縣',
                                text='台東縣'
                            )
                        ]   
                    ), 

                    CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                        title='屏東縣',
                        text='也可直接在對話筐輸入縣市',
                        actions=[
                            MessageTemplateAction(
                                label='屏東縣',
                                text='屏東縣'
                            )
                        ]   
                    )
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
