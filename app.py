import requests
from flask import Flask, render_template,request,jsonify
from scrap import scrapweb


app = Flask(__name__)

@app.route("/espace_client", methods=["GET"])
def home():
	return render_template('index.html')

@app.route("/", methods=["POST"])
def extract():
	# Get link page
	link = request.form['link']
	if "en.aptoide.com" not in link:
		return jsonify([])

	# Get page content
	page_html = requests.get(link,timeout=10)
	info_extracted = scrapweb.getApplicationInfo(page_html)
	#return data au format json
	return jsonify(info_extracted)

if __name__ == '__main__':
    app.run(host='0.0.0.0')