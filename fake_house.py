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
                        title='9,999元/月',
                        text='★可寵★捷運★新光★獨洗獨曬★',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15182030'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區青海路二段193巷'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),

                    CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                        imageAspectRatio='square',
                        title='6,500元/月',
                        text='好屋台中市-西屯區_西屯區逢甲商圈台水台電~',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15226936'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區河南路二段259號'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),
                    CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/08/08/169149535003070801.jpg!750x588.water2.jpg',
                        imageAspectRatio='square',
                        title='8,000元/月',
                        text='有電梯近,新光三越、老虎城、秋紅谷、逢甲',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15226936'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區朝馬一街22號'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),
                                        CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                        imageAspectRatio='square',
                        title='好屋台中市-西屯區_西屯區逢甲商圈台水台電~',
                        text='.',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15226936'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區河南路二段259號'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),
                                        CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                        imageAspectRatio='square',
                        title='好屋台中市-西屯區_西屯區逢甲商圈台水台電~',
                        text='.',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15226936'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區河南路二段259號'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),
                                        CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                        imageAspectRatio='square',
                        title='好屋台中市-西屯區_西屯區逢甲商圈台水台電~',
                        text='.',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15226936'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區河南路二段259號'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),
                                        CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                        imageAspectRatio='square',
                        title='好屋台中市-西屯區_西屯區逢甲商圈台水台電~',
                        text='.',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15226936'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區河南路二段259號'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),
                                        CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                        imageAspectRatio='square',
                        title='好屋台中市-西屯區_西屯區逢甲商圈台水台電~',
                        text='.',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15226936'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區河南路二段259號'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),
                                        CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                        imageAspectRatio='square',
                        title='好屋台中市-西屯區_西屯區逢甲商圈台水台電~',
                        text='.',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15226936'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區河南路二段259號'
                            ),
                            MessageTemplateAction(
                                label='詢問',
                                text='請輸入:詢問 想問的問題'
                            ),
                        ]
                        
                    ),
                                        CarouselColumn(
                        thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                        imageAspectRatio='square',
                        title='好屋台中市-西屯區_西屯區逢甲商圈台水台電~',
                        text='.',
                        actions=[
                            URIAction(
                                label='更多資訊',
                                uri='https://rent.591.com.tw/home/15226936'
                            ), 
                            MessageTemplateAction(
                                label='地理位置',
                                text='找地圖 西屯區河南路二段259號'
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