from flask import Flask
import os
app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello, my < postgres  > images! ' + os.getenv("HOSTNAME") + ''
