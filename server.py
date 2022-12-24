from app import app
from app import adminbot
from flask import request, Blueprint


@app.route('/adminbot', methods=['POST'])
def telegram_request():
    print('Got Webhook')
    json_string = request.get_data().decode('utf-8')
    tg = Blueprint('tg', __name__)
    app.register_blueprint(tg, url_prefix="/adminbot")
    req = adminbot.Webhook(json_string)
    req.update()
    

@app.route('/adminbot', methods=['GET'])
def telegram():
  
@app.route('/', methods=['GET'])

@app.route('/manychat', methods=['POST'])
def manychat_request():
    pass


@app.route('/payments', methods=['POST'])
def payment_request():
    pass


if __name__ == "__main__":
    app.run()
