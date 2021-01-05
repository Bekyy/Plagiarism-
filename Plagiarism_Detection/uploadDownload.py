from flask import Flask, request, redirect, url_for, render_template, send_from_directory
from werkzeug.utils import secure_filename
import os
#import magic
import urllib.request
# from app import app
from PyPDF2 import PdfFileReader, PdfFileWriter

app = Flask(__name__)
app.secret_key = "hello"
DOWNLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/downloads/'
app.config['DOWNLOAD_FOLDER'] = DOWNLOAD_FOLDER
UPLOAD_FOLDER = os.path.dirname(os.path.abspath(__file__)) + '/uploads/'
app.config['MAX_CONTENT_LENGTH'] = 8 * 1024 * 1024

ALLOWED_EXTENSIONS = {'pdf'}
def allowed_file(filename):
   return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'POST':
       if 'file' not in request.files:
           print('No file attached in request')
           return redirect(request.url)
       file = request.files['file']
       if file.filename == '':
           print('No file selected')
           return redirect(request.url)
       if file and allowed_file(file.filename):
           filename = secure_filename(file.filename)
           file.save(os.path.join(UPLOAD_FOLDER, filename))
           process_file(os.path.join(UPLOAD_FOLDER, filename), filename)
           # return redirect(url_for('uploaded_file', filename=filename))
   return render_template('index.html')

def process_file(path, filename):
   remove_watermark(path, filename)

def remove_watermark(path, filename):
   input_file = PdfFileReader(open(path, 'rb'))
   page = input_file.getPage(0)
   content = page.extractText()
   return content
   # output = PdfFileWriter()
   # for page_number in range(input_file.getNumPages()):
   #     page = input_file.getPage(page_number)
   #     page.mediaBox.lowerLeft = (page.mediaBox.getLowerLeft_x(), 20)
   #     output.addPage(page)
   # output_stream = open(app.config['DOWNLOAD_FOLDER'] + filename, 'wb')
   # output.write(output_stream)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
   return send_from_directory(app.config['DOWNLOAD_FOLDER'], filename, as_attachment=True)

if __name__ == "__main__":
  app.run()