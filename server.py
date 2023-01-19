from flask import Flask, request, jsonify, render_template
app = Flask(__name__)
import warnings
warnings.filterwarnings("ignore")
import scraper
import summarizer
link = ""

@app.route("/", methods=["GET"])
def home():
    return render_template("ArticleSummarizer.html")


@app.route("/search", methods=["POST"])
def search():
        link = request.form.get("url")
        y = scraper.scrape(link)
        x = summarizer.summarize(y)
        return render_template("Summary.html", summary = x)

if __name__ == "__main__":
    app.run(debug=True)