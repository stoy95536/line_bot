from linebot import LineBotApi, WebhookHandler
from linebot.models import *
import os

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])


def fake_compare(event):
    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://img1.591.com.tw/house/2023/09/03/169371681244317506.jpg!fit.1000x.water2.jpg',
                    imageAspectRatio='square',
                    title='9,999元/月\n押金二個月',
                    text='獨立套房|8坪|6F/8F|透天厝\n西屯區青海路二段193巷\n來源:591租屋網',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://rent.591.com.tw/home/15182030'
                        ), 
                        MessageTemplateAction(
                            label='取消關注',
                            text='取消關注'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問西屯區青海路二段193巷'
                        ),
                    ]
                ),

                CarouselColumn(
                    thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                    imageAspectRatio='square',
                    title='6,500元/月\n押金二個月',
                    text='獨立套房|8坪|6F/12F|電梯大樓\n西屯區河南路二段259號\n來源:591租屋網',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://rent.591.com.tw/home/15226936'
                        ), 
                        MessageTemplateAction(
                            label='取消關注',
                            text='取消關注'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問西屯區河南路二段259號'
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)