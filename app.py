import os
from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage
from linebot.models import ImageMessage, ImageSendMessage
from reservation import Reservation

TOKEN = "TZvX2e2N777ZZWUbxIZ0N5/4sVkGKVMyVzJ0hBuPUN3VXWu750bWrwhbQzoRy4nx24H1Sa38knAssjl/lYJVUbseTor9jK1UnQOAEYOFAW1j+bq2D1ae213zuMeOWc5YfPz3OSK1CNOhNspkxeuQGAdB04t89/1O/w1cDnyilFU="
SECRET = "d6d87ccdad6f7b412cc6ce0bccd92186"
app = Flask(__name__)

line_bot_api = LineBotApi(TOKEN)
handle = WebhookHandler(SECRET)
reservation = Reservation()

# endpoint
@app.route("/")
def test():
    return "It Works!"

# endpoint from linebot
@app.route("/callback", methods=['GET', 'POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handle.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handle.add(MessageEvent, message=TextMessage)
def handle_message(event):
    input = event.message.text
    if not reservation.check(input[4:6], input[6::]):
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="空きがないよー")
        )
    else:
        line_bot_api.reply_message(
            event.reply_token,
            TextSendMessage(text="空いているよー")
        )

# if __name__ == "__main__":
#     # app.run(port=int(os.getenv('PORT', 5002)))
#     app.run()