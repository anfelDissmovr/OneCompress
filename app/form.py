from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileRequired, FileAllowed
from wtforms.validators import NumberRange
from wtforms import IntegerField, SubmitField

class ImageUploadForm(FlaskForm):
    images = FileField('Seleccionar Imagen', validators=[
        FileRequired('No se ha seleccionado ningún archivo'),
        FileAllowed(['png', 'jpg', 'jpeg', 'gif'], '¡Solo se permiten archivos de imagen!')
    ],render_kw={"multiple": True})
    Weight = IntegerField("Weight", default=300)
    Quality = IntegerField("Quality", default=10, validators=[
        NumberRange(min=1, max=99, message="El valor de Quality debe estar entre 1 y 99.")
    ])
    Width = IntegerField("Width", default=1920)
    Height = IntegerField("Height", default=1080)
    submit = SubmitField('Subir Imágenes') 
    
class RenameImagen(FlaskForm):
    images = FileField('Seleccionar Imagen', validators=[
        FileRequired('No se ha seleccionado ningún archivo'),
        FileAllowed(['png', 'jpg', 'jpeg', 'gif'], '¡Solo se permiten archivos de imagen!')
    ],render_kw={"multiple": True}) 
    submit = SubmitField("Subir Imagen")