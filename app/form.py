from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import NumberRange
from wtforms import IntegerField, SubmitField

class ImageUploadForm(FlaskForm):
    images = FileField('Seleccionar Imagen', validators=[
        FileRequired('No se ha seleccionado ningún archivo'),
        FileAllowed(['png', 'jpg', 'jpeg', 'gif'], '¡Solo se permiten archivos de imagen!')
    ],render_kw={"multiple": True})
    Weight = IntegerField("Weight", default=500)
    Quality = IntegerField("Quality", default=20, validators=[
        NumberRange(min=1, max=99, message="El valor de Quality debe estar entre 1 y 99.")
    ])
    Width = IntegerField("Width", default=2200)
    Height = IntegerField("Height", default=1238)
    submit = SubmitField('Subir Imágenes') 
    
class PdfUploadForm(FlaskForm):
    Pdf = FileField('Seleccionar Archivo PDF', validators=[
        FileRequired('No se ha seleccionado ningún archivo'),
        FileAllowed(['pdf'], '¡Solo se permiten archivos PDF!')
    ])
    submit = SubmitField("Subir Archivo")