from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.exceptions import InvalidSignatureError
from linebot.models import MessageEvent, TextMessage, TextSendMessage

TOKEN = "TZvX2e2N777ZZWUbxIZ0N5/4sVkGKVMyVzJ0hBuPUN3VXWu750bWrwhbQzoRy4nx24H1Sa38knAssjl/lYJVUbseTor9jK1UnQOAEYOFAW1j+bq2D1ae213zuMeOWc5YfPz3OSK1CNOhNspkxeuQGAdB04t89/1O/w1cDnyilFU="
SECRET = "d6d87ccdad6f7b412cc6ce0bccd92186"
app = Flask(__name__)

line_bot_api = LineBotApi(TOKEN)
handler = WebhookHandler(SECRET)

@app.route("/", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)
    return 'OK'

@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text)
    )

if __name__ == "__main__":
    app.run()
