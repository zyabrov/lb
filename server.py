from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
  return "Hello World!"

@app.route('/', methods=['GET'])
def sample():
    response = {"status": "200}
    response = response.json()
    return response
  

if __name__ == "__main__":
  app.run()
