from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

def get_meme():
    url = "https://random.imagecdn.app/v1/image?category=buildings&format=json"
    respone = json.loads(requests.request("GET", url).text)
    meme_img_url = respone["url"]
    
    return meme_img_url

@app.route("/")
def index():
    meme_img_url = get_meme()
    
    return render_template("index.html", meme_img_url=meme_img_url)

app.run(host="0.0.0.0", port=80)