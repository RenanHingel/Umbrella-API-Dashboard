from flask import render_template, redirect, Flask
from controller.controller import *

app = Flask(__name__)

################################################################
# Landing page the reason I'm redirecting to INDEX is a place holder to the future / route that will require AD log on
################################################################
@app.route('/')
def redirect_to_index():
    return redirect('/devices', code=302)

# @app.route('/login',methods = ['GET'])
# def index():
# 	return render_template('login.html')
################################################################


################################################################
# Routes to navbar items
################################################################
@app.route('/devices',methods = ['GET'])
def route_devices():
	return render_template('devices.html', result=get_devices("all"))

@app.route('/virtual_appliances',methods = ['GET'])
def route_virtual_appliances():
	return render_template('virtual_appliances.html', result=get_devices("va"))

@app.route('/connectors',methods = ['GET'])
def route_connectors():
	return render_template('ad_connectors.html', result=get_devices("ad"))

@app.route('/domain_controllers',methods = ['GET'])
def route_domain_controllers():
	return render_template('domain_controllers.html', result=get_devices("dc"))

@app.route('/audit',methods = ['GET'])
def route_audit():
	return render_template('audit.html')
################################################################


################################################################
# Error handling
################################################################
@app.errorhandler(500)
def route_errorhandler(e):
    return render_template('500.html'), 500

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080)
