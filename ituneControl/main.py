import requests
from flask import Flask, request, g, redirect, url_for, render_template, jsonify
import json
from re import sub
import os

DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'


app = Flask(__name__)
app.config.from_object(__name__)


@app.route('/',methods=['GET','POST'])
def ituneControl():
	if request.method == 'POST':

		controlInput = request.get_json()
		
		if controlInput["input"] == "Play":
			os.system('/Users/shabadlamba/PythonProjects/ituneControl/itunes.sh play')
			# output = os.popen('/Users/shabadlamba/PythonProjects/ituneControl/itunes.sh status').read()
			# controlInput["output"]=output
			# print controlInput
		elif controlInput["input"] == "Pause":
			os.system('/Users/shabadlamba/PythonProjects/ituneControl/itunes.sh pause')
		
		elif controlInput["input"] == "Next":
			os.system('/Users/shabadlamba/PythonProjects/ituneControl/itunes.sh next')
		
		elif controlInput["input"] == "Previous":
			os.system('/Users/shabadlamba/PythonProjects/ituneControl/itunes.sh prev')

		elif controlInput["input"] == "Up":
			os.system('/Users/shabadlamba/PythonProjects/ituneControl/itunes.sh vol up')

		elif controlInput["input"] == "Down":
			os.system('/Users/shabadlamba/PythonProjects/ituneControl/itunes.sh vol down')

		return redirect(url_for('ituneControl'))#, jsonify(output=controlInput["output"]))
	
	return render_template('ituneControl.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5001)
