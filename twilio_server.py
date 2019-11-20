from threading import Thread
from flask import Flask, request
from messaging import process_msg

app = Flask(__name__)

@app.route("/sms", methods=['GET', 'POST'])
def ccq_reply():
    Thread(target=process_msg).start()
    return "You shouldn't be looking at this site!"

if __name__ == "__main__":
    app.run(debug=True)
