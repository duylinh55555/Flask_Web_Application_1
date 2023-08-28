from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://meme-api.herokuapp.com/gimme"
    respone = json.loads(requests.request("GET", url).text)
    meme_img = respone["preview"][-2]
    subreddit = respone["subreddit"]
    
    return meme_img, subreddit

@app.route("/")
def index():
    meme_img, subreddit = get_meme()
    
    return render_template("index.html", meme_img, subreddit)

app.run(host="0.0.0.0", port=80)