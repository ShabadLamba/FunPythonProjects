import os
from flask import Flask, request, session, g, redirect, url_for, \
     abort, render_template, flash,jsonify
from werkzeug import secure_filename
import subprocess
from re import sub

DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'admin'
PASSWORD = 'default'
UPLOAD_FOLDER = '/Users/shabadlamba/PythonProjects/pdfReaderApp'

app = Flask(__name__)
app.config.from_object(__name__)

@app.route('/',methods=['GET','POST'])
def uploadPdf():
	if request.method == 'POST':
		file = request.files['file']
		if file:	
			filename = secure_filename(file.filename)
			file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))
			flash('File Uploaded')
			print filename
			return redirect(url_for('readAndPrintPdf',filename=filename))
		# file.save(os.path.join(config['UPLOAD_FOLDER']),"sample")
	return render_template('pdfUpload.html')

@app.route('/result/<filename>',methods=['GET','POST'])
def readAndPrintPdf(filename):
	print filename
	filePath = "pdf2txt.py /Users/shabadlamba/PythonProjects/pdfReaderApp/" + filename
	Data = subprocess.check_output(filePath,shell=True)
	return render_template('pdfResult.html',Data=(sub(r"[^\x00-\x7F]+","",Data)))



if __name__ == '__main__':
	app.run(host='0.0.0.0',port=5008)
