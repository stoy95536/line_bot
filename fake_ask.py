from linebot import LineBotApi, WebhookHandler
from linebot.models import *
import os

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])
'''
def ask(event):
    message = TemplateSendMessage(
    alt_text='ImageCarousel template',
    template=ImageCarouselTemplate(
        columns=[
            ImageCarouselColumn(
                image_url='https://i03piccdn.sogoucdn.com/ab1afd2701878c6e',
                action=PostbackAction(
                    label='區域交通搜尋',
                    display_text='區域交通搜尋',
                    data='區域交通搜尋'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i03piccdn.sogoucdn.com/ab1afd2701878c6e',
                action=PostbackAction(
                    label='吃飯搜尋',
                    display_text='吃飯搜尋',
                    data='吃飯搜尋'
                )
            ),
            ImageCarouselColumn(
                image_url='https://i03piccdn.sogoucdn.com/ab1afd2701878c6e',
                action=PostbackAction(
                    label='工作搜尋',
                    display_text='工作搜尋',
                    data='工作搜尋'
                )
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,message)
'''
def ask(event):

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    imageAspectRatio='square',
                    title='詢問該房屋資訊',
                    text='附近有哪些公司或辦公樓？',
                    actions=[
                        MessageTemplateAction(
                            label='地理位置',
                            text='找地圖 西屯區青海路二段193巷'
                        ),
                        MessageTemplateAction(
                            label='區域交通搜尋',
                            text='區域交通搜尋'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='詢問該房屋資訊',
                    text='請選擇',
                    actions=[
                        MessageTemplateAction(
                            label='吃飯搜尋',
                            text='吃飯搜尋'
                        ),
                        MessageTemplateAction(
                            label='工作搜尋',
                            text='工作搜尋'
                        ),
                    ]
                ),
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)

def ask_old(event):
    try:
        message = TemplateSendMessage(
            alt_text = '按鈕樣板',
            template = ButtonsTemplate(
                title='詢問該房屋資訊',
                text='請選擇：',
                actions=[
                    MessageTemplateAction(
                        label='區域交通搜尋',
                        text='區域交通搜尋'
                    ),
                    MessageTemplateAction(
                        label='吃飯搜尋',
                        text='吃飯搜尋'
                    ),
                    MessageTemplateAction(
                        label='工作搜尋',
                        text='工作搜尋'
                    ),
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token,message)
    except:
        line_bot_api.reply_message(event.reply_token,TextSendMessage(text='發生錯誤!'))     


def ask_Q1(event):

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q1',
                    text='附近有學校或教育機構嗎?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近有學校或教育機構嗎?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q2',
                    text='附近的公共交通工具方便嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近的公共交通工具方便嗎?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q3',
                    text='附近有公園或是娛樂設施嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近有公園或是娛樂設施嗎?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q4',
                    text='附近有運動地點或是健身中心嗎?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近有運動地點或是健身中心嗎?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q5',
                    text='附近是否有停車場或停車位？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近是否有停車場或停車位?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q6',
                    text='附近是否有醫院?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近是否有醫院?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q7',
                    text='附近有購物中心或商場嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近有購物中心或商場嗎?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
    
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)

def ask_Q2(event):

    message = TemplateSendMessage(
        alt_text='Carousel template',
        template=CarouselTemplate(
            columns=[
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q1',
                    text='附近有超市或商店嗎?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近有超市或商店嗎?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q2',
                    text='附近有素食或特殊飲食需求的餐廳嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近有素食或特殊飲食需求的餐廳嗎?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q3',
                    text='附近是否有夜市或街頭小吃？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近是否有夜市或街頭小吃?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q4',
                    text='附近附近是否有咖啡廳?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近附近是否有咖啡廳?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q5',
                    text='附近有哪些餐廳和食品選擇?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近有哪些餐廳和食品選擇?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
    
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)

def ask_Q3(event):

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
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q2',
                    text='附近是否有咖啡廳或共享工作空間？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近是否有咖啡廳或共享工作空間?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q3',
                    text='附近是否有圖書館或研究場所？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近是否有圖書館或研究場所?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q4',
                    text='附近是否有工作相關的社交活動或職業發展機會?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近是否有工作相關的社交活動或職業發展機會?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q5',
                    text='需要一間辦公室/工作室空間，有推薦的地點嗎?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='查詢 西屯區青海路二段193巷附近需要一間辦公室/工作室空間，有推薦的地點嗎?走路，騎車距離多遠呢?'
                        ),
                    ]
                ),
    
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)
