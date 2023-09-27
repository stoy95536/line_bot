from linebot import LineBotApi, WebhookHandler
from linebot.models import *
import os

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def remide_choose(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ButtonsTemplate(
        text='是否沿用最後一次查詢的條件？',
        actions=[
            MessageAction(
                label='是',
                text='沿用上一筆設定'
            ),
            MessageAction(
                label='重新設定',
                text='重新設定條件'
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,message)

def test(event):
    message = TemplateSendMessage(
        alt_text='Confirm template',
        template=ConfirmTemplate(
            text='iThome鐵人2021',
            actions=[
                PostbackAction(
                    label='postback',
                    display_text='postback text',
                    data='action=buy&itemid=1'
                ),
                MessageAction(
                    label='message',
                    text='message text'
                )
            ]
        )
    )
    line_bot_api.reply_message(event.reply_token,message)


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
