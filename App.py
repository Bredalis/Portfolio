
from flask import Flask, render_template

def portafolio()

	app = Flask(__name__)

	# Asignar las rutas de la página

	@app.route("/")
	def index():
		return render_template("index.html")

	@app.errorhandler(404)
	def error_404(e):
		return render_template("404.html"), 404

	return app

if __name__ == "__main__":
	app = portafolio()
	app.run()