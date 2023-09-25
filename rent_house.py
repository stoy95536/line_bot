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

#六都 離島 非六都
def administrative＿district(event): #找租屋對話筐_選擇縣市
    try:
        message = TemplateSendMessage(
            alt_text = '按鈕樣板',
            template = ButtonsTemplate(
                thumbnail_image_url='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.backpackers.com.tw%2Fguide%2Findex.php%2F%25E4%25B8%25AD%25E8%258F%25AF%25E6%25B0%2591%25E5%259C%258B&psig=AOvVaw1vW7SCaTEklF_LQybFbc-9&ust=1695721953579000&source=images&cd=vfe&opi=89978449&ved=0CBAQjRxqFwoTCID3ite-xYEDFQAAAAAdAAAAABAE',
                title='請問你要找哪個縣市的房子呢？',
                text='可根據按鈕點選，也可直接在對話筐輸入縣市：',
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
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!')) 


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
