from flask import Flask
from flask import redirect, url_for, render_template


app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found(error):
	return redirect(url_for('index'))

if __name__ == "__main__":
    app.run()
 
