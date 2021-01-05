# from flask import Flask, redirect, url_for, render_template, request, session
# from datetime import timedelta
# import PyPDF2
# from PyPDF2 import PdfFileReader, PdfFileWriter
# from werkzeug.utils import secure_filename
# from werkzeug.datastructures import  FileStorage
# import similarity
# import os

# app = Flask(__name__)
# app.secret_key = "hello"
# #app.config["ALLOWED_EXTENSIONS"] = ["pdf", "html", "ppt", "xml"]

# #allow to upload file up to 16MB
# app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024
# UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__))

# @app.route("/", methods=["POST", "GET"])
# def my():
# 	return render_template("mypage.html")

# ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])
# def allowed_file(filename):
#    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# @app.route('/SimilarityReport',methods = ['POST', 'GET'])
# def result():
# 	# if request.method == 'POST':
# 	# 	result = request.form['text']
# 	# 	if result:
# 	# 		sim = (similarity.Table(similarity.reports(str(result))))
# 	# 		return render_template('mypage.html', tables=[sim])		
# 	# 		#return (similarity.Table(similarity.reports(str(result))))

# 	# 	else:
# 	# 		return ('not avilable')

# 	if request.method == 'POST': 
# 		result = request.form['text']
# 		file = request.files['myfile']
# 		if 'file' not in request.files:
# 			flash('No file part')
# 			return redirect(request.url)
# 		if file.filename == '':
# 			flash('No file selected for uploading')
# 			return redirect(request.url)
# 		if file and allowed_file(file.filename):		
# 			if ALLOWED_EXTENSIONS == '.pdf':
# 				filename = secure_filename(file.filename)
# 				pdfFileObj = file.save(os.path.join(UPLOAD_FOLDER,filename))
# 				text = open(UPLOAD_FOLDER + '\\' + filename , 'rb')
# 				pdfReader = PyPDF2.PdfFileReader(text)
# 				pageObj = pdfReader.getPage(0)
# 				result = pageObj.extractText()
# 				text.close()
# 				sim = (similarity.Table(similarity.reports(str(result))))
# 				os.remove(UPLOAD_FOLDER + '\\' + filename)
# 				sim = (similarity.Table(similarity.reports(str(result))))
# 				return render_template('mypage.html', tables=[sim])

# 			if ALLOWED_EXTENSIONS == '.docx':
# 				filename = secure_filename(file.filename)
# 				file.save(os.path.join(UPLOAD_FOLDER,filename))
# 				text = open(UPLOAD_FOLDER + '\\' + filename , 'rb')
# 				result = docx2txt.process(text)
# 				text.close()
# 				os.remove(UPLOAD_FOLDER + '\\' + filename)
# 				return render_template('mypage.html', tables=[sim])

# 			if ALLOWED_EXTENSIONS == '.txt':
# 				filename = secure_filename(file.filename)
# 				file.save(os.path.join(UPLOAD_FOLDER,filename))
# 				with open(UPLOAD_FOLDER + '\\' + filename) as f:
# 					content = f.read().splitlines()
# 					content.close()
# 					os.remove(UPLOAD_FOLDER + '\\' + filename)
# 					sim = (similarity.Table(similarity.reports(str(content))))
# 					return render_template('mypage.html', tables=[sim])


# 			else:
# 				flash('Allowed file types are txt, pdf, png, jpg, jpeg, gif')


# 		else:
# 			sim = (similarity.Table(similarity.reports(str(result))))
# 			return render_template('mypage.html', tables=[sim])	
# 	else:
# 		return render_template("mypage.html")


	
# if __name__ == "__main__":
#     app.run(debug=True)