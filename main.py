import os
from flask import Flask, render_template
import requests
from dotenv import load_dotenv

app = Flask(__name__)

load_dotenv()


@app.route("/")
def index():
    api = os.getenv("API")
    url = f"https://emoji-api.com/emojis?access_key={api}"
    response = requests.get(url)

    if response.status_code == 200:
        emojis = response.json()
    else:
        emojis = []
    return render_template("index.html", emojis=emojis)


if __name__ == "__main__":
    app.run(debug=True)
