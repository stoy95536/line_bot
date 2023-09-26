from linebot import LineBotApi, WebhookHandler
from linebot.models import *
import os

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def fake_house1(event):

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    thumbnail_image_url='https://img1.591.com.tw/house/2023/09/03/169371681244317506.jpg!fit.1000x.water2.jpg',
                    imageAspectRatio='square',
                    title='9,999元/月\n押金二個月',
                    text='獨立套房|8坪|6F/8F|透天厝\n西屯區青海路二段193巷',
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
                            text='詢問西屯區青海路二段193巷'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img2.591.com.tw/house/2023/09/18/169501899725655103.jpg!750x588.water2.jpg',
                    imageAspectRatio='square',
                    title='6,500元/月\n押金二個月',
                    text='獨立套房|8坪|6F/12F|電梯大樓\n西屯區河南路二段259號',
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
                            text='詢問西屯區河南路二段259號'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img2.591.com.tw/house/2023/08/08/169149535003070801.jpg!750x588.water2.jpg',
                    imageAspectRatio='square',
                    title='8,000元/月\n押金二個月',
                    text='獨立套房|7坪|4F/4F|電梯大樓\n西屯區朝馬一街22號',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://rent.591.com.tw/home/15309639'
                        ), 
                        MessageTemplateAction(
                            label='地理位置',
                            text='找地圖 西屯區朝馬一街22號'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img2.591.com.tw/house/2018/10/30/154085826271038606.jpg!750x588.water2.jpg',
                    imageAspectRatio='square',
                    title='9,300元/月\n押金二個月',
                    text='獨立套房|10坪|10F/10F|電梯大樓\n西屯區重慶路',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://rent.591.com.tw/home/12831413'
                        ), 
                        MessageTemplateAction(
                            label='地理位置',
                            text='找地圖 西屯區重慶路'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://img2.591.com.tw/house/2023/09/25/169564310332228103.jpg!750x588.water2.jpg',
                    imageAspectRatio='square',
                    title='9,000元/月\n押金二個月',
                    text='獨立套房|9坪|6F/6F|公寓\n西屯區西屯路二段',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://rent.591.com.tw/home/15313071'
                        ), 
                        MessageTemplateAction(
                            label='地理位置',
                            text='找地圖 西屯區西屯路二段'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://static.rakuya.com.tw/r2/n912/d4/98/23682912_1_b.jpeg?1695735092',
                    imageAspectRatio='square',
                    title='6,999元/月\n押金二個月',
                    text='獨立套房|13坪|1樓/2樓|透天厝\n台中市西屯區西屯路二段惠北巷',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://www.rakuya.com.tw/rent_item/info?ehid=0162a523682912a'
                        ), 
                        MessageTemplateAction(
                            label='地理位置',
                            text='找地圖 台中市西屯區西屯路二段惠北巷'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://static.rakuya.com.tw/r2/n731/0b/23/23682731_1_b.jpeg?1695731056',
                    imageAspectRatio='square',
                    title='6,799元/月\n押金二個月',
                    text='獨立套房|12坪|4樓/7樓|電梯大廈\n台中市西屯區烈美街',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://www.rakuya.com.tw/rent_item/info?ehid=0b5152236827315'
                        ), 
                        MessageTemplateAction(
                            label='地理位置',
                            text='找地圖 台中市西屯區烈美街'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://static.rakuya.com.tw/r2/n769/91/f0/23682769_1_b.jpeg?1695732330',
                    imageAspectRatio='square',
                    title='7,699元/月\n押金二個月',
                    text='獨立套房|13坪|2樓/4樓|透天厝\n台中市西屯區四川路',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://www.rakuya.com.tw/rent_item/info?ehid=011a9223682769b'
                        ), 
                        MessageTemplateAction(
                            label='地理位置',
                            text='找地圖 台中市西屯區四川路'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://static.rakuya.com.tw/r1/n419/02/8a/23673419_1_b.jpeg?1695660603',
                    imageAspectRatio='square',
                    title='5,499元/月\n押金二個月',
                    text='獨立套房|10坪|5樓/6樓|透天厝\n台中市西屯區西安街',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://www.rakuya.com.tw/rent_item/info?ehid=0f8e9123673419e'
                        ), 
                        MessageTemplateAction(
                            label='地理位置',
                            text='找地圖 台中市西屯區西安街'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問'
                        ),
                    ]
                ),
                CarouselColumn(
                    thumbnail_image_url='https://static.rakuya.com.tw/r2/n521/bd/11/23662521_1_b.jpeg?1695541579',
                    imageAspectRatio='square',
                    title='6,499元/月\n押金二個月',
                    text='獨立套房|11坪|4樓/5樓|透天厝\n台中市西屯區河南路二段',
                    actions=[
                        URIAction(
                            label='更多資訊',
                            uri='https://www.rakuya.com.tw/rent_item/info?ehid=0ae9a123662521e'
                        ), 
                        MessageTemplateAction(
                            label='地理位置',
                            text='找地圖 台中市西屯區河南路二段'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問'
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)