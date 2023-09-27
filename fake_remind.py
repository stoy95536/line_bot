from linebot import LineBotApi, WebhookHandler
from linebot.models import *
import os

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def choose(event): 
    try:
        message = TemplateSendMessage(
            alt_text = '按鈕樣板',
            template = ButtonsTemplate(
                #thumbnail_image_url='https://a.bbkz.net/guide/images/2/2d/%E5%8F%B0%E7%81%A3%E8%A1%8C%E6%94%BF%E5%8D%80%E5%9C%96.png',
                imageAspectRatio='square',
                title='請問您是否要沿用上一筆設定呢？',
                text='上筆設定\n台中市/西屯區/獨立套房/5000-10000',
                actions=[
                    MessageTemplateAction(
                        label='是',
                        text='沿用設定條件'
                    ),
                    MessageTemplateAction(
                        label='重新設定條件',
                        text='重新設定條件'
                    ),

                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!')) 

def set_time(event):

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    imageAspectRatio='square',
                    title='若是有符合條件的房源，您希望我們多久提醒您呢？',
                    text='請選擇',
                    actions=[
                        MessageTemplateAction(
                            label='3小時',
                            text='設定_3小時'
                        ),
                        MessageTemplateAction(
                            label='6小時',
                            text='設定_6小時'
                        ),
                        MessageTemplateAction(
                            label='12小時',
                            text='設定_12小時'

                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='若是有符合條件的房源，您希望我們多久提醒您呢？',
                    text='請選擇',
                    actions=[
                        MessageTemplateAction(
                            label='24小時',
                            text='設定_24小時'
                        ),
                        MessageTemplateAction(
                            label='48小時',
                            text='設定_48小時'
                        ),
                        MessageTemplateAction(
                            label='72小時',
                            text='設定_72小時'

                        ),
                    ]
                ),
    
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)
