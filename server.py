from app import app
from app import adminbot
from flask import Flask, request



@app.route('/adminbot', methods=['POST'])
def telegram_request():
    print('Got Webhook')
    json_string = request.get_data().decode('utf-8')
    req = adminbot.Webhook(json_string)
    req.update()
    

@app.route('/adminbot', methods=['GET'])
def telegram():
  'telegram get'
  
@app.route('/', methods=['GET'])
def sample():
  'get request'

@app.route('/manychat', methods=['POST'])
def manychat_request():
    pass


@app.route('/payments', methods=['POST'])
def payment_request():
    pass


if __name__ == "__main__":
    app.run()
