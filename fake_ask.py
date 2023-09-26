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
                            text='詢問 西屯區青海路二段193巷附近有學校或教育機構嗎?'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近有學校或教育機構嗎?'
                        ),
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近有學校或教育機構嗎?'
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
                            text='詢問 西屯區青海路二段193巷附近的公共交通工具方便嗎?'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q3',
                    text='附近有公園或是娛樂設施嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近有公園或是娛樂設施嗎?'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q4',
                    text='附近有運動地點或是健身中心嗎?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近有運動地點或是健身中心嗎?'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q5',
                    text='附近是否有停車場或停車位？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近是否有停車場或停車位?'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q6',
                    text='附近是否有醫院?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近是否有醫院?'
                        )
                    ]
                ),
                CarouselColumn(
                    #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    title='Q7',
                    text='附近有購物中心或商場嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近有購物中心或商場嗎?'
                        )
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
                            text='詢問 西屯區青海路二段193巷附近有超市或商店嗎?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q2',
                    text='附近的公共交通工具方便嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近的公共交通工具方便嗎?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q3',
                    text='附近有公園或是娛樂設施嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近有公園或是娛樂設施嗎?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q4',
                    text='附近有運動地點或是健身中心嗎?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近有運動地點或是健身中心嗎?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q5',
                    text='附近是否有停車場或停車位？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近是否有停車場或停車位?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q6',
                    text='附近是否有醫院?',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近是否有醫院?'
                        ),
                    ]
                ),
                CarouselColumn(
                    imageAspectRatio='square',
                    title='Q7',
                    text='附近有購物中心或商場嗎？',
                    actions=[
                        MessageTemplateAction(
                            label='詢問',
                            text='詢問 西屯區青海路二段193巷附近有購物中心或商場嗎?'
                        ),
                    ]
                ),
    
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)

def test(event): 
    try:
        message = TemplateSendMessage(
            alt_text='台中行政區',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        #thumbnail_image_url='https://img1.591.com.tw/house/2023/09/08/169414163003871703.jpg!510x400.jpg',
                        imageAspectRatio='square',
                        title='90%的人都點擊了以下區域',
                        text='西屯區、北屯區、南屯區',
                        actions=[
                            MessageTemplateAction(
                                label='西屯區',
                                text='西屯區'
                            ),
                            MessageTemplateAction(
                                label='北屯區',
                                text='北屯區'
                            ),
                            MessageTemplateAction(
                                label='南屯區',
                                text='南屯區'
                            ),
                        ]
                        
                    ),

                    CarouselColumn(
                        #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                        title='若所選行政區不在選項中',
                        text='可直接在對話筐輸入',
                        actions=[
                            MessageTemplateAction(
                                label='北區',
                                text='北區'
                            ),
                            MessageTemplateAction(
                                label='西區',
                                text='西區'
                            ),
                            MessageTemplateAction(
                                label='東區',
                                text='東區'
                            )
                        ]   
                    ) 
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))        