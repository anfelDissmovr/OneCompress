import os 
from flask import Blueprint,render_template,request
from app.form import PdfUploadForm
from werkzeug.utils import secure_filename
from app.config import Config
import PyPDF2

compressPdf = Blueprint('CompressPdf',__name__)

@compressPdf.route('', methods=['GET', 'POST'])
def index():
    form = PdfUploadForm()
    
    if form.validate_on_submit():
        file = form.Pdf.data  
        filename = secure_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER_PDF, filename)
   
       
    return render_template('compressPdf/compressPdf.html', pdfForm=form, titulo="Compress PDF Files")