from flask import Flask
from flasgger import Swagger

app = Flask(__name__)
swagger = Swagger(app)

@app.route('/')
def home():
    """
    Home Endpoint
    ---
    get:
      description: Welcome to Flask Swagger!
      responses:
        200:
          description: Returns a welcome message
    """
    return "Hello, Swagger in Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
