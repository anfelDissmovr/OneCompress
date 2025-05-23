from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed,DataRequired
from wtforms.validators import NumberRange
from wtforms import IntegerField, SubmitField,SelectField,StringField

class ImageUploadForm(FlaskForm):
    images = FileField('Seleccionar Imagen', validators=[
        FileRequired('No se ha seleccionado ningún archivo'),
        FileAllowed(['png', 'jpg', 'jpeg', 'gif', 'webp'], '¡Solo se permiten archivos de imagen!')
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
    
class FormStorage(FlaskForm):
    idproject = StringField('Enter project ID', validators=[DataRequired()])
    idUser = StringField('Enter User ID', validators=[DataRequired()])
    rol = SelectField('Role', choices=[('Owner', 'Owner')])
    folder = StringField('Enter the folder')
    submit = SubmitField('Upload files')