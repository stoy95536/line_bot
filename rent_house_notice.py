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

#六都 離島 非六都選擇
def notices(event): 
    try:
        message = TemplateSendMessage(
            alt_text='租屋小撇步',
            template=CarouselTemplate(
                columns=[
                    CarouselColumn(
                        # thumbnail_image_url="https://www.hbtamsui.com.tw/images/ewp/23/%E7%A7%9F%E5%B1%8B%E7%B0%BD%E7%B4%84%E8%A6%81%E5%B8%B6%E4%BB%80%E9%BA%BC.jpg",
                        # imageAspectRatio='square',
                        title='租客簽約時需要攜帶什麼？',
                        text='租客簽約時，要帶筆、印章與身分證影本，並可請親友陪同簽約。',
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
                            ),
                        ]   
                    ),

                    CarouselColumn(
                        #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                        title='租約中提到押金超過2個月是否合法？',
                        text='根據《住宅租賃契約應約定及不得約定事項》第四點規定，租屋押金不可以超過兩個月租金的金額。',
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
                            ),
                        ]   
                    ), 

                    CarouselColumn(
                        #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                        title='租客簽約時應該注意哪些事項？',
                        text='對租客來說，首要條件就是要先確認房東身份，以免簽約簽錯對象白花錢。\n其次，在租屋前必須先確認房屋狀況、租金、解約規定與租約是否合理等等。',
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
                            ),
                        ]   
                    ), 

                    # CarouselColumn(
                    #     #thumbnail_image_url='https://img2.591.com.tw/house/2023/06/05/168596855727457664.jpg!510x400.jpg',
                    #     title='租屋租約公證的用意是？',
                    #     text='公證可有效達到保存證據用途，當其中一方違約時，\n例如：惡意欠租、拒絕搬遷、不退還押金等等，可向法院聲請強制執行，而不用經過訴訟程序。',
                    #     actions=[
                    #         MessageTemplateAction(
                    #             label='台中市',
                    #             text='台中市'
                    #         ),
                    #         MessageTemplateAction(
                    #             label='台南市',
                    #             text='台南市'
                    #         ),
                    #         MessageTemplateAction(
                    #             label='高雄市',
                    #             text='高雄市'
                    #         ),
                    #     ]   
                    # ), 
                ]
            )
        )
        line_bot_api.reply_message(event.reply_token, message)
    except :
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text='發生錯誤！'))
