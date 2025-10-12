from flask import Flask
import os
app = Flask(__name__)
app.run(debug=True)

@app.route('/')
def hello_world():
    return 'Hello, my < argocd - 111  postgres  > images! ' + os.getenv("HOSTNAME") + ''
