from flask import Flask, redirect, url_for, render_template, request, session
from datetime import timedelta
import PyPDF2
from PyPDF2 import PdfFileReader, PdfFileWriter
from werkzeug.utils import secure_filename
from werkzeug.datastructures import  FileStorage
import similarity
import os

UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))
app = Flask(__name__)
app.secret_key = "hello"
app.config["ALLOWED_EXTENSIONS"] = ["pdf", "html", "ppt", "xml"]

@app.route("/", methods=["POST", "GET"])
def my():
	return render_template("mypage.html")

# ALLOWED_EXTENSIONS = {'pdf'}
# def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/SimilarityReport',methods = ['POST', 'GET'])
def result():
	if request.method == 'POST':
		result = request.form['text']

		if result:
			sim = (similarity.Table(similarity.reports(str(result))))
			return render_template('mypage.html', tables=[sim], result = result)		
			#return (similarity.Table(similarity.reports(str(result))))

		else:
			return ('not avilable')

	# if request.method == 'POST': 
	# 	result = request.form['text']

		# file = request.files['myfile']
		# if file:
		# 	filename = secure_filename(file.filename)
		# 	pdfFileObj = file.save(os.path.join(UPLOAD_FOLDER,filename))
		# 	text = open(UPLOAD_FOLDER + '\\' + filename , 'rb')
		# 	pdfReader = PyPDF2.PdfFileReader(text)
		# 	pageObj = pdfReader.getPage(0)
		# 	result = pageObj.extractText()
		# 	text.close()
		# 	os.remove(UPLOAD_FOLDER + '\\' + filename)
		# 	return (similarity.Table(similarity.reports(str(result))))									
			# return render_template('report.html', reports = similarity.Table(similarity.reports(str(result))))				

			# filename = secure_filename(file.filename)
			# file.save(os.path.join(UPLOAD_FOLDER,filename))
			# with open(UPLOAD_FOLDER) as f:
			# 	result = f.read()
				

		# else:
		# 	return (similarity.Table(similarity.reports(str(result))))
	else:
		return render_template("mypage.html")


	
if __name__ == "__main__":
    app.run(debug=True)