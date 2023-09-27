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

def set_time(event):

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q1',
                    text='附近有哪些公司或辦公樓？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近有哪些公司或辦公樓?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
    
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)
