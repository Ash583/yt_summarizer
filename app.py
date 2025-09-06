from flask import Flask, render_template, request
from summarizer import get_summary

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    summary = ""
    url = ""
    if request.method == "POST":
        url = request.form.get("url")
        if url != "":
            summary = get_summary(url)
    return render_template("index.html", summary=summary, url=url)

if __name__ == "__main__":
    app.run(debug=True)
