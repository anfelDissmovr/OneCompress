import os 
from flask import Blueprint,render_template,request,session
from app.form import PdfUploadForm
from werkzeug.utils import secure_filename
from app.config import Config
from flask import jsonify
from app.functions.functionPdf import convertir_pdf_a_jpg

compressPdf = Blueprint('CompressPdf',__name__)

@compressPdf.route('', methods=['GET', 'POST'])
def index():
    form = PdfUploadForm()
    SplitBotton = False
    
    if form.validate_on_submit():
        file = form.Pdf.data  
        filename = secure_filename(file.filename)
        filepath = os.path.join(Config.UPLOAD_FOLDER_PDF, filename)
        file.save(filepath)
        SplitBotton = True
        session['pdfPath'] = filepath
        return render_template('compressPdf/compressPdf.html', pdfForm=form, SplitBotton=SplitBotton, titulo="Compress PDF Files")
    
    
    return render_template('compressPdf/compressPdf.html', pdfForm=form, titulo="Compress PDF Files")


@compressPdf.route('/spliting', methods=['POST'])
def splitPdf():
    PdfCompletes = session.get('pdfPath')
    ImgList = convertir_pdf_a_jpg(PdfCompletes)
    if ImgList:
        form = False
    return jsonify({"message": "PDF dividido exitosamente",
                    "form": form}) 