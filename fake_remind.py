from linebot import LineBotApi, WebhookHandler
from linebot.models import *
import os

line_bot_api = LineBotApi(os.environ['CHANNEL_ACCESS_TOKEN'])
handler = WebhookHandler(os.environ['CHANNEL_SECRET'])

def remide_choose(event):
    message = TemplateSendMessage(
    alt_text='Confirm template',
    template=ConfirmTemplate(
        text='是否沿用最後一次查詢的條件？',
        actions=[
            MessageAction(
                label='是',
                text='沿用查詢條件'
            ),
            MessageAction(
                label='重新設定',
                text='重新設定條件'
            )
        ]
    )
    )
    line_bot_api.reply_message(event.reply_token,message)