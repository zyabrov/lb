from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/', methods=['GET'])
def sample():
    response = "status 200"
    
    return 'Был получен GET-запрос.'
  

if __name__ == "__main__":
  app.run()
