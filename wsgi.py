from flask import Flask, render_template,request,jsonify
import scrapweb

app = Flask(__name__)


@app.route("/", methods=["GET"])
def home():
	return render_template('index.html')

@app.route("/scrapp_web", methods=["POST"])
def extract():
	# Get link page
	link = request.form['link']
	if "en.aptoide.com" not in link:
		return jsonify([])

	# instanciate object Scrapweb
	scrap_web = scrapweb.Scrapweb(link)
	info_extracted = scrap_web.getApplicationInfo()
	#return data au format json
	return jsonify(info_extracted)

if __name__ == '__main__':
    app.run(host='0.0.0.0')